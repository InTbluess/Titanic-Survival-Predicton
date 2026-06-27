import joblib
import pandas as pd

pipeline = joblib.load(
    "models/trained/best_model.pkl"
)

pclass = int(input("Passenger Class (1-3): "))

sex = input("Sex (male/female): ")

age = float(input("Age: "))

sibsp = int(input("Siblings/Spouses: "))

parch = int(input("Parents/Children: "))

fare = float(input("Fare: "))

embarked = input("Embarked (C/Q/S): ")

passenger = pd.DataFrame({
    "pclass": [pclass],
    "sex": [sex],
    "age": [age],
    "sibsp": [sibsp],
    "parch": [parch],
    "fare": [fare],
    "embarked": [embarked]
})

prediction = pipeline.predict(passenger)
probability = pipeline.predict_proba(passenger)

if prediction[0] == 1:
    print("\nPrediction: Survived")
else:
    print("\nPrediction: Did Not Survive")
    
print(f"Did Not Survive: {probability[0][0]*100:.2f}%")
print(f"Survived       : {probability[0][1]*100:.2f}%")