from fastapi import FastAPI
import pandas as pd
import joblib
import json
import numpy as np

app = FastAPI()

# load model
model = joblib.load("model.joblib")

# load features
with open("features.json", "r") as f:
    FEATURES = json.load(f)


@app.post("/predict")
def predict(data: dict):

    # convert input -> dataframe
    df = pd.DataFrame([data])

    # align features (VERY IMPORTANT)
    df = df.reindex(columns=FEATURES, fill_value=0)

    # prediction
    proba = model.predict_proba(df)[:, 1][0]
    pred = int(proba >= 0.69)

    return {
        "probability": float(proba),
        "prediction": pred
    }