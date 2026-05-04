df = pd.read_csv("application_train.csv")

X = df.drop(columns=["TARGET", "SK_ID_CURR"])
y = df["TARGET"]

model.fit(X, y)

joblib.dump(model, "model.joblib")