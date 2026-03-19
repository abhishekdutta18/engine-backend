from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "working"}

@app.post("/predict")
def predict(data: dict):
    x1 = data["x1"]
    x2 = data["x2"]
    x3 = data["x3"]

    mean = x1 + x2 + x3
    variance = np.var([x1, x2, x3])

    return {
        "mean": mean,
        "variance": float(variance)
    }
