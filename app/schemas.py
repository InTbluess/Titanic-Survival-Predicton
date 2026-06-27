from typing import Literal

from pydantic import (
    BaseModel,
    Field
)


class Passenger(BaseModel):

    pclass: int = Field(..., ge=1, le=3)

    sex: Literal[
        "male",
        "female"
    ]

    age: float = Field(..., ge=0)

    sibsp: int = Field(..., ge=0)

    parch: int = Field(..., ge=0)

    fare: float = Field(..., ge=0)

    embarked: Literal[
        "C",
        "Q",
        "S"
    ]


class PredictionResponse(BaseModel):

    prediction: int

    survived_probability: float

    died_probability: float