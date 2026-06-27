import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
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