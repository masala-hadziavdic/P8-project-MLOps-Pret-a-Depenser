from fastapi import FastAPI
import pandas as pd
import joblib
import json
import numpy as np
import os 

app = FastAPI()

@app.get("/")
def home():
    return {"status": "OK"}
# ======================
# LOAD MODEL
# ======================
model = joblib.load("model/model.joblib")

# ======================
# LOAD FEATURES 
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "..", "model", "features.json"), "r") as f:
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