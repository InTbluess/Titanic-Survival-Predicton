import joblib

pipeline = joblib.load(
    "models/trained/best_model.pkl"
)
print(type(pipeline))