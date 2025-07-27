from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel, Field

# Load model
model = joblib.load('app/model.pkl')
# get the class names instead of numbers
class_names = np.array(['setosa', 'versicolor', 'virginica'])
#create fastapi app
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
    )# input definition
# get request :from root
@app.get("/", summary="Root Endpoint", tags=["General"])
def read_root():
    #just return any sting
    return {"message": "Hi, how are you?"}
# post request
@app.post("/predict", summary="Predict Iris Flower Species", tags=["Prediction"])
def predict(data: FeaturesInput):
    features = np.array(data.features).reshape(1, -1)# reshape to match the input size
    prediction = model.predict(features)
    # mapping from numbers to flower type:str
    class_name = class_names[prediction[0]]
    return {"input_features": data.features, "prediction": class_name}

