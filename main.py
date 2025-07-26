from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel, Field

# Load model
model = joblib.load('app/model.pkl')
class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI(
    title="Iris Classifier API",
    description="Predict iris flower species based on sepal/petal measurements.",
    version="1.0.0"
)

# Input schema
class FeaturesInput(BaseModel):
    features: list[float] = Field(
        ...,
        description="A list of 4 numerical feature values: [sepal_length, sepal_width, petal_length, petal_width].",
        json_schema_extra={"example": [5.1, 3.5, 1.4, 0.2]}
    )

@app.get("/", summary="Root Endpoint", tags=["General"])
def read_root():
    return {"message": "Hi, how are you?"}

@app.post("/predict", summary="Predict Iris Flower Species", tags=["Prediction"])
def predict(data: FeaturesInput):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction[0]]
    return {"input_features": data.features, "prediction": class_name}
