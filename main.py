from fastapi import FastAPI
import joblib
import numpy as np

model= joblib.load('app/model.pkl')
class_names=np.array(['setosa','versicolor','virginica'])
app= FastAPI()

@app.get("/")
def read_root():
    return{"message":"Hi how are you?"}
@app.post("/predict")
def predict(data:dict):
    features=np.array(data['features']).reshape(1,-1)
    predicton=model.predict(features)
    class_name = class_names[predicton[0]]
    return {"predicton is:" ,class_name}