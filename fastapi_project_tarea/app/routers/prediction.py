from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.dependencies import get_model, get_preprocessor
import pandas as pd
import numpy as np

router = APIRouter()

class PassengerInfo(BaseModel):
    # Define aquí los campos de tu modelo Pydantic
    pclass: int
    name: str = Field(default=None)
    sex: str
    age: float
    sibsp: int
    parch: int
    ticket: str = Field(default=None)
    fare: float
    cabin: str
    embarked: str
    boat: str = Field(default=None)
    body: str = Field(default=None)
    home_dest: str = Field(default=None)


@router.post("/prediction")
async def make_prediction(passenger: PassengerInfo, model=Depends(get_model), preprocessor=Depends(get_preprocessor)):
    # Convertir los datos Pydantic en DataFrame
    passenger_df = pd.DataFrame([passenger.dict()])

    print(passenger_df.columns)

    # Preprocesar los datos
    preprocessed_data = preprocessor.transform(passenger_df)
    
    print(preprocessed_data)

    # Realizar la predicción
    prediction = model.predict(preprocessed_data)

    # Convertir la predicción a un tipo nativo de Python (por ejemplo, una lista de Python)
    if isinstance(prediction, np.ndarray):
        prediction = prediction.tolist()
    elif isinstance(prediction, (np.int64, np.float64)):
        prediction = int(prediction)  # o float(prediction_result)

    return {"prediction": prediction}


