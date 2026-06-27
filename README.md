# 🚢 Titanic Survival Prediction

An end-to-end Machine Learning project that predicts whether a passenger aboard the Titanic would survive based on passenger information.

This project demonstrates the complete machine learning workflow, from data preprocessing and feature engineering to model evaluation, pipeline creation, and prediction using a trained model.

---

## 📌 Project Overview

The goal of this project is to build a classification model capable of predicting passenger survival on the Titanic dataset.

Unlike a simple Jupyter Notebook implementation, this project follows a modular software architecture using Python packages and Scikit-learn Pipelines, making it easier to maintain, extend, and deploy.

---

## 🚀 Features

* Data cleaning and preprocessing
* Feature engineering
* Scikit-learn Pipeline implementation
* Multiple model comparison
* Cross Validation
* Model evaluation
* Model serialization with Joblib
* Command-line prediction system
* Modular project structure

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Seaborn
* Matplotlib
* Joblib

---

## 📂 Project Structure

```text
Titanic-Survival-Prediction/
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
├── main.py
├── main_old.py
├── main_pipeline.py
├── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Machine Learning Workflow

```
Load Dataset
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Encoding
        ↓
Train/Test Split
        ↓
Cross Validation
        ↓
Model Training
        ↓
Evaluation
        ↓
Save Pipeline
        ↓
Predict New Passenger
```

---

## 📊 Models Compared

* Logistic Regression
* Decision Tree
* Random Forest

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Cross Validation

---

## 🧠 Feature Engineering

The following custom features were created:

* Family Size
* Is Alone
* Fare Per Person

These engineered features helped improve the model's predictive performance.

---

## 📈 Best Model

**Random Forest Classifier**

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

The final model is saved using Joblib and can be loaded later without retraining.

---

## 🔮 Making Predictions

Train the pipeline:

```bash
python main_pipeline.py
```

Predict a passenger's survival:

```bash
python predict.py
```

Example:

```text
Passenger Class (1-3): 1
Sex (male/female): female
Age: 23
Siblings/Spouses: 2
Parents/Children: 0
Fare: 389
Embarked (C/Q/S): C

Prediction: Survived
Confidence: 95%
```

---

## 📚 What I Learned

During this project I learned how to:

* Perform exploratory data analysis (EDA)
* Handle missing values
* Engineer meaningful features
* Build reusable machine learning pipelines
* Compare multiple machine learning models
* Perform Cross Validation
* Evaluate classification models
* Serialize trained models using Joblib
* Organize Python projects using a modular architecture
* Build an interactive prediction application

---

## 🔮 Future Improvements

* FastAPI REST API
* React frontend
* Docker support
* Cloud deployment
* Hyperparameter tuning
* Automated testing
* CI/CD with GitHub Actions

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
