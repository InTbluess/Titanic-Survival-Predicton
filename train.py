from src.data import load_data
from src.preprocess import clean_data
from src.pipeline import build_pipeline
from src.save import save_model

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

def main():

    df = load_data()

    df = clean_data(df)
    
    X = df.drop("survived", axis=1)
    y = df["survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    pipeline = build_pipeline()
    
    # # Cross Validation
    # scores = cross_val_score(
    #     pipeline,
    #     X_train,
    #     y_train,
    #     cv=5,
    #     scoring="accuracy"
    # )

    # print("CV Mean:", scores.mean())

    # Final Training
    pipeline.fit(
        X_train,
        y_train
    )
    
    predictions = pipeline.predict(X_test)

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

    cm = confusion_matrix(
        y_test,
        predictions
    )

    
    print("\n===== Evaluation =====")

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\n===== Confusion Matrix =====")
    print(cm)

    print("\n===== Classification Report =====")
    print(classification_report(
        y_test,
        predictions
    ))  

    save_model(pipeline)

if __name__ == "__main__":
    main()