

import joblib

def get_model():
    model_path = "app/ar/model.pkl"  # Actualiza con la ruta correcta
    model = joblib.load(model_path)
    return model


