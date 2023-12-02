

from fastapi import FastAPI
from app.routers.prediction import router as prediction_router

app = FastAPI()

# Incluir el router de predicciones en la aplicación
app.include_router(prediction_router)

