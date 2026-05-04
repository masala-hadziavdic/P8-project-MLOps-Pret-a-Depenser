import pandas as pd
import joblib
import xgboost as xgb

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("application_train.csv")

X = df.drop(columns=["TARGET", "SK_ID_CURR"])
y = df["TARGET"]

# ======================
# MODEL
# ======================
model = xgb.XGBClassifier(
    n_estimators=400,
    max_depth=3,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=(y == 0).sum() / (y == 1).sum(),
    eval_metric="auc",
    random_state=42
)

# ======================
# TRAIN
# ======================
model.fit(X, y)

# ======================
# SAVE MODEL
# ======================
joblib.dump(model, "model/model.joblib")