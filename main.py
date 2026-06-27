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

# Local Imports
from src.data import load_data
from src.preprocess import (
    clean_data,
    encode_data,
    prepare_features_target,
    split_data
)
from src.features import engineer_features
from src.models import train_models
from src.save import save_model
from src.evaluate import display_results


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