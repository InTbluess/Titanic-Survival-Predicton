from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    OneHotEncoder,
    FunctionTransformer
)
from src.features import create_features

NUMERICAL_FEATURES = [
    "age",
    "fare"
]

CATEGORICAL_FEATURES = [
    "sex", 
    "embarked"
]

MODEL = RandomForestClassifier(
    random_state=42
)

feature_engineer = FunctionTransformer(
    create_features,
    validate=False
)


preprocessor = ColumnTransformer(
    transformers=[
        (
            "num", #numerical
            SimpleImputer(strategy="median"),
            NUMERICAL_FEATURES
        ),
        (
            "cat", #categorical
            OneHotEncoder(drop="first"),
            CATEGORICAL_FEATURES
            
        )
    ],
    remainder="passthrough"
)



def build_pipeline():
    pipeline = Pipeline([
        ("features", feature_engineer),
        ("preprocessor", preprocessor),
        ("model", MODEL)
    ])

    return pipeline