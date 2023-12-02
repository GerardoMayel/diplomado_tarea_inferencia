from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.dependencies import get_model, get_preprocessor
import pandas as pd

router = APIRouter()

class PassengerInfo(BaseModel):
    # Define aquí los campos de tu modelo Pydantic
    pclass: int
    sex: str
    age: float
    sibsp: int
    parch: int
    fare: float
    cabin: str
    embarked: str
    # Agrega más campos si es necesario

@router.post("/prediction")
async def make_prediction(passenger: PassengerInfo, model=Depends(get_model), preprocessor=Depends(get_preprocessor)):
    # Convertir los datos Pydantic en DataFrame
    passenger_df = pd.DataFrame([passenger.dict()])

    # Preprocesar los datos
    preprocessed_data = preprocessor.transform(passenger_df)

    # Realizar la predicción
    prediction = model.predict(preprocessed_data)

    # Devolver la predicción
    return {"prediction": prediction[0]}
