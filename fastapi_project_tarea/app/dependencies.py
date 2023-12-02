import joblib
import os

# Definir las rutas relativas para el modelo y el preprocesador
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "artifacts", "LogisticRegression_model.pkl")
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), "..", "artifacts", "preprocessor.pkl")

def get_model():
    # Carga el modelo desde la ruta relativa
    model = joblib.load(MODEL_PATH)
    return model

def get_preprocessor():
    # Carga el preprocesador desde la ruta relativa
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return preprocessor

