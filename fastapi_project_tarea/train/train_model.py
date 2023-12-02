import joblib
from transformers.transformers import (
    MissingIndicator,
    CabinOnlyLetter,
    CategoricalImputerEncoder,
    NumericalImputesEncoder,
    RareLabelCategoricalEncoder,
    OneHotEncoder,
    MinMaxScaler,
    CleaningTransformer,
    DropTransformer,
)
import pandas as pd
import config
from config import *
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sys
import os

def train(model_name: str):
    numeric_transformer = Pipeline(
        steps=[
            ("missing_indicator", MissingIndicator(config.NUMERICAL_VARS)),
            ("median_imputation", NumericalImputesEncoder(config.NUMERICAL_VARS)),
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("cabin_only_letter", CabinOnlyLetter("cabin")),
            ("categorical_imputer", CategoricalImputerEncoder(config.CATEGORICAL_VARS)),
            (
                "rare_labels",
                RareLabelCategoricalEncoder(
                    tol=0.02, variables=config.CATEGORICAL_VARS
                ),
            ),
            ("one_hot", OneHotEncoder(config.CATEGORICAL_VARS)),
        ]
    )

    preprocessor = Pipeline(
        [
            ("cleaning", CleaningTransformer()),
            ("categorical", categorical_transformer),
            ("numeric", numeric_transformer),
            ("dropper", DropTransformer(config.DROP_COLS)),
            ("scaling", MinMaxScaler()),
        ]
    )

    if model_name == 'RandomForest':
        regressor = RandomForestClassifier(
            max_depth=4, class_weight="balanced", random_state=config.SEED_MODEL
        )
    else:
        regressor = LogisticRegression(
            C=0.0005, class_weight="balanced", random_state=config.SEED_MODEL
        )

    titanic_pipeline = Pipeline(
        [("preprocessor", preprocessor), (f"{model_name}_regressor", regressor)]
    )

    df = pd.read_csv(config.URL).rename(columns={'home.dest':'home_dest'})
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(config.TARGET, axis=1),
        df[config.TARGET],
        test_size=0.2,
        random_state=config.SEED_SPLIT,
    )

    titanic_pipeline.fit(X_train, y_train)
    preds = titanic_pipeline.predict(X_test)
    accuracy = (preds == y_test).sum() / len(y_test)
    print(f"Accuracy of the model is {accuracy}")

    # Crear carpeta artifacts si no existe
    if not os.path.exists(config.ARTIFACTS_FOLDER):
        os.makedirs(config.ARTIFACTS_FOLDER)

    # Guardar el preprocesador y el modelo por separado
    joblib.dump(titanic_pipeline.named_steps['preprocessor'], os.path.join(config.ARTIFACTS_FOLDER, "preprocessor.pkl"))
    joblib.dump(titanic_pipeline.named_steps[f'{model_name}_regressor'], os.path.join(config.ARTIFACTS_FOLDER, f"{model_name}_model.pkl"))

    print(f"Artifacts stored in {config.ARTIFACTS_FOLDER}")

if __name__ == "__main__":
    model_name = str(sys.argv[1]) if len(sys.argv) > 1 else 'LogisticRegression'
    train(model_name=model_name)

