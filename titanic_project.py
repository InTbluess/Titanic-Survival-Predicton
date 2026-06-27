"""
=========================================
Titanic Survival Prediction
Author: Indranil

End-to-End Machine Learning Project

Workflow

0. Imports
1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Encoding
5. Train/Test Split
6. Train Models
7. Evaluate Models
8. Cross Validation
9. Save Best Model
=========================================
"""

# ==========================
# Imports
# ==========================

import pandas as pd
import seaborn as sns
import joblib

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from pathlib import Path

# Save Dataset before & after processes
def save_dataset(df, filepath):

    filepath = Path("data") / filepath

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        filepath,
        index=False
    )

    print(f"Saved: {filepath}")


def load_data():
    df = sns.load_dataset("titanic")

    save_dataset(
        df,
        "raw/titanic_raw.csv"
    )
    return df


def clean_data(df):
    df = df.copy()
    df = df.drop(
        columns=[
            "deck",
            "class",
            "who",
            "adult_male",
            "embark_town",
            "alive",
            "alone"
        ]
    )

    df["age"] = df["age"].fillna(
        df["age"].median()
    )

    df = df.dropna(
        subset=["embarked"]
    )

    save_dataset(
        df,
        "processed/titanic_clean.csv"
    )   

    return df


def engineer_features(df):
    df = df.copy()
    df["family_size"] = (
        df["sibsp"] +
        df["parch"] +
        1
    )

    df["is_alone"] = (
        df["family_size"] == 1
    ).astype(int)

    df["fare_per_person"] = (
        df["fare"] /
        df["family_size"]
    )

    # print("AFTER: ")
    # print(df.head())

    # print(df.info())

    # print(df.isnull().sum())
    # print(df.types)

    return df


def encode_data(df):
    df = df.copy()
    df = pd.get_dummies(
        df,
        columns=["sex", "embarked"],
        drop_first=True
    )
    # print(df.head())

    save_dataset(
    df,
    "processed/titanic_encoded.csv"
)

    return df


def prepare_features_target(df):
    X = df.drop("survived", axis=1)

    y = df["survived"]

    return X, y


def split_data(X, y):
    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def get_models():
    return {

        "Logistic Regression":
            LogisticRegression(max_iter=1000),

        "Decision Tree":
            DecisionTreeClassifier(random_state=42),

        "Random Forest":
            RandomForestClassifier(random_state=42)

    }


def train_models(X, y, X_train, X_test, y_train, y_test):
    models = get_models()

    # ==========================
    # Train & Evaluate
    # ==========================

    results = []
    best_model = None
    best_score = float("-inf")
    best_model_name = ""

    for name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        # Cross Validation
        cv_scores = cross_val_score(
            model,
            X,
            y,
            cv=5,
            scoring="accuracy"
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        result = {

            "Model": name,

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1 Score": f1,

            # Cross Validation
            "CV Mean": cv_scores.mean(),

            "CV Std": cv_scores.std()

        }

        results.append(result)

        if cv_scores.mean() > best_score:
            best_score = cv_scores.mean()
            best_model = model
            best_model_name = name

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
    by="CV Mean",
    ascending=False
)

    # print(results_df)
    return results_df, best_model, best_model_name, best_score


def save_model(model):
    save_dir = Path("models/trained")
    save_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        model,
        save_dir / "best_model.pkl"
    )

    print("Model saved.")


def display_results(results_df, best_model_name, best_score):

    print(results_df)

    print("\nBest Model:", best_model_name)

    print("Best CV Score:", best_score)
    

def main():
    # ==========================
    # Load Dataset
    # ==========================

    df = load_data()

    # print("BEFORE: ")
    # print(df.head())

    # print(df.info())

    # print(df.isnull().sum())


    # ==========================
    # Data Cleaning
    # ==========================

    df = clean_data(df)
    

    # ===================================
    # Feature Engineering
    # ===================================

    df = engineer_features(df)
    

    # ==========================
    # Encoding
    # ==========================

    df = encode_data(df)

    
    # ==========================
    # Features & Target
    # ==========================

    X, y = prepare_features_target(df)
    # print(X.shape)
    # print(y.shape)


    # ==========================
    # Train Test Split
    # ==========================

    X_train, X_test, y_train, y_test = split_data(X, y)

    # print(X_train.shape)
    # print(X_test.shape)


    # ==========================
    # Train & Evaluate
    # ==========================

    results_df, best_model, best_model_name, best_score = train_models(
        X,
        y,
        X_train,
        X_test,
        y_train,
        y_test
    )


    # ===================================
    # Save Best Model
    # ===================================

    save_model(best_model)


    # ===================================
    # Display Results
    # ===================================


    display_results(
        results_df,
        best_model_name,
        best_score
    )
    

if __name__ == "__main__":
    main()