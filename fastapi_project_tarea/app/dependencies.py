import joblib
from config import MODEL_PATH, PREPROCESSOR_PATH

def get_model():
    # Carga el modelo desde la ruta especificada en config.py
    model = joblib.load(MODEL_PATH)
    return model

def get_preprocessor():
    # Carga el preprocesador desde la ruta especificada en config.py
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    return preprocessor

