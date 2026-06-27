<div align="center">
# 🚢 Titanic Survival Prediction
 
**An end-to-end Machine Learning project predicting passenger survival on the Titanic**
 
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
 
</div>

 
## 📌 Overview
 
This project demonstrates the **complete machine learning lifecycle** — from raw data to a production-ready REST API — using the classic Titanic dataset.
 
Given a passenger's information (class, age, sex, fare, etc.), the model predicts whether they would have survived.
 
---
 
## ✨ Features
 
| Area | Details |
|---|---|
| 📊 **Analysis** | Exploratory Data Analysis (EDA) |
| 🔧 **Preprocessing** | Data cleaning, feature engineering, Scikit-learn Pipelines |
| 🤖 **Modelling** | Multiple classifiers, cross-validation, hyperparameter tuning |
| 💾 **Serialization** | Trained pipeline saved with Joblib |
| 🖥️ **CLI** | Interactive command-line prediction tool |
| 🌐 **API** | FastAPI REST API with Swagger docs |
| 🗂️ **Architecture** | Fully modular Python project structure |
 
---
 
## 🛠 Tech Stack
 
**Machine Learning** — Python · Pandas · NumPy · Scikit-learn · Joblib
 
**Visualization** — Matplotlib · Seaborn
 
**Backend** — FastAPI · Uvicorn · Pydantic
 
---
 
## 📂 Project Structure
 
```text
Titanic-Survival-Prediction/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── routes.py        # API endpoints
│   ├── schemas.py       # Request / response models
│   └── model.py         # Load trained pipeline
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── trained/
│
├── src/
│   ├── data.py
│   ├── preprocess.py
│   ├── features.py
│   ├── pipeline.py
│   ├── save.py
│   └── evaluate.py
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```
 
---
 
## ⚙️ ML Workflow
 
```
Load Dataset → Data Cleaning → Feature Engineering → Preprocessing
     → Train/Test Split → Cross Validation → Model Training
          → Evaluation → Save Pipeline → Predictions
```
 
---
 
## 📊 Models Compared
 
Three classifiers were trained and evaluated head-to-head:
 
- Logistic Regression
- Decision Tree
- **Random Forest** ← 🏆 Best performer
Each model was assessed on **Accuracy, Precision, Recall, F1 Score, Confusion Matrix,** and **Cross Validation**.
 
---
 
## 🧠 Feature Engineering
 
Three custom features were derived to improve predictive power:
 
| Feature | Description |
|---|---|
| `family_size` | `SibSp + Parch + 1` |
| `is_alone` | Whether the passenger travelled alone |
| `fare_per_person` | `Fare / family_size` |
 
---
 
## 🏆 Best Model — Random Forest Classifier
 
The winning model is serialized as a full **Scikit-learn Pipeline** (preprocessing + classifier) using Joblib, ensuring consistent transformations at inference time.
 
---
 
## 🚀 Getting Started
 
**Install dependencies**
 
```bash
pip install -r requirements.txt
```
 
**Train the model**
 
```bash
python train.py
```
 
**Run CLI predictions**
 
```bash
python predict.py
```
 
```
Passenger Class (1-3): 1
Sex (male/female): female
Age: 23
Siblings/Spouses: 2
Parents/Children: 0
Fare: 389
Embarked (C/Q/S): C
 
Prediction:   Survived ✅
Confidence:   95%
```
 
---
 
## 🌐 FastAPI
 
**Start the server**
 
```bash
uvicorn app.main:app --reload
```
 
| URL | Description |
|---|---|
| `http://127.0.0.1:8000` | Base API |
| `http://127.0.0.1:8000/docs` | Interactive Swagger UI |
 
**Example request**
 
```json
{
  "pclass": 1,
  "sex": "female",
  "age": 23,
  "sibsp": 2,
  "parch": 0,
  "fare": 389,
  "embarked": "C"
}
```
 
**Example response**
 
```json
{
  "prediction": 1,
  "survived_probability": 0.96,
  "died_probability": 0.04
}
```
 
---
 
## 🔮 Future Improvements
 
- [ ] React frontend
- [ ] Docker containerisation
- [ ] Cloud deployment
- [ ] CI/CD pipeline
- [ ] Model monitoring
- [ ] Batch prediction API
- [ ] Authentication
- [ ] Automated testing
---
 
## 🤝 Contributing
 
Contributions, ideas, and suggestions are welcome! Feel free to fork the repo and open a Pull Request.
 
---
 
## 📄 License
 
This project is licensed under the **MIT License**.
 
