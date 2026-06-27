# ======================
# SERVER TESTING 
# from fastapi import FastAPI


# app = FastAPI(
#     title="Titanic Survival Prediction API",
#     description="Predict Titanic passenger survival using a trained Random Forest model.",
#     version="1.0.0"
# )


# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to the Titanic Survival Prediction API!"
#     }

# @app.get("/health")
# def health():
#     return {
#         "status": "healthy"
#     }

# ======================

from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Predict Titanic passenger survival using a trained Random Forest model.",
    version="1.0.0"
)
 

app.include_router(router)