import pandas as pd
from sklearn.model_selection import train_test_split

from src.utils import save_dataset

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