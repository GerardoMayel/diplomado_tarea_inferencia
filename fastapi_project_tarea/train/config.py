import os

BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
# Cambia la URL para que apunte a tu archivo local
URL = os.path.join(BASE_DIR, "train/data", "phpMYEkMl.csv")

SEED_SPLIT = 404
SEED_MODEL = 404
ARTIFACTS_FOLDER = os.path.join(BASE_DIR, "artifacts") # Ruta a la carpeta de artefactos
# Ajustar los nombres para reflejar tanto el modelo como el pipeline
MODEL_FILE_NAME = "model.pkl" # Nombre del archivo del modelo entrenado
PREPROCESSOR_FILE_NAME = "preprocessor.pkl" # Nombre del archivo del preprocesador
# Rutas completas para el modelo y el preprocesador
MODEL_PATH = os.path.join(ARTIFACTS_FOLDER, MODEL_FILE_NAME)
PREPROCESSOR_PATH = os.path.join(ARTIFACTS_FOLDER, PREPROCESSOR_FILE_NAME)

TARGET = "survived"
FEATURES = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "cabin",
    "embarked",
    "title",
]
NUMERICAL_VARS = ["pclass", "age", "sibsp", "parch", "fare"]
CATEGORICAL_VARS = ["sex", "cabin", "embarked", "title"]
DROP_COLS = ["boat", "body", "ticket", "name"]
