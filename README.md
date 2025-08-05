# 🧠 Employee Attrition Prediction

A machine learning project that predicts whether an employee is likely to leave the company. This system is trained on HR analytics data, carefully preprocessed, balanced using SMOTE, and deployed through a web interface for real-time predictions.

---

## 🔍 Project Overview

Employee attrition is a key challenge faced by organizations. By analyzing employee characteristics, job satisfaction, and work environment data, this project aims to identify employees who are at risk of leaving.

The system uses **classification algorithms**, primarily **XGBoost** and **Random Forest**, trained and tuned to handle class imbalance. It is deployed as a simple web application where HR professionals can upload employee data and receive predictions instantly.

---

## 🌊 Dataset

* **Source**: [IBM HR Analytics Employee Attrition & Performance Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
* **Samples**: 1470 employees
* **Target Column**: `Attrition` (Yes/No)
* **Issue**: High class imbalance (No: 1233, Yes: 237)
* **Solution**: Applied **SMOTE** (Synthetic Minority Oversampling Technique)

---

## 🏗️ Project Features

* Clean, reproducible ML pipeline
* Encoded & scaled input features
* Balanced dataset using SMOTE
* Hyperparameter tuning using GridSearchCV
* Final model: **XGBoost**, tuned and exported using `pickle`
* Simple web app (Flask) hosted on Render

---

## 🧪 Model Evaluation (Final XGBoost)

* **Accuracy**: 92.43%
* **Precision (Leave class)**: 93%
* **Recall (Leave class)**: 91%
* **F1-score**: 0.92

Confusion Matrix:

```
[[345  24]  ← Stayed
 [ 32 339]] ← Left
```

---

## 🚀 Deployment

The application is deployed on **Render**.

🔗 **Live Web App**: [LINK](https://exitsense.onrender.com)

---

## 🗂️ Project Structure

```
employee-attrition-predictor/
├── app/
│   └── app.py                  # Flask API to handle uploads and predictions
│
├── models/
│   ├── main_model/              # Contains Final tuned model
│   ├── scaler_models/           # Contains Saved StandardScaler
│   └── encoder_models/          # Contains Saved LabelEncoder
│
├── data/
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv        # Example input data
│   └── Test_Data_1_10.csv                   # Optional testing input
│
├── src/
│   ├── data_preprocessing.py   # Encoding, scaling, input transformation
│   ├── model_loader.py         # Load model from file
│   └── predictor.py            # Make prediction from processed input
│
├── notebooks/
│   └── Test_Board.ipynb    # Exploratory data analysis, Model training, SMOTE, tuning
│
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

---

## 🢑 Collaborators

This project was built as a near-industry practice for our hackathon-ready ML team:

* 👩‍💻 **[Bidisha Pal](https://github.com/bi-disha)** – Data Pipeline, Preprocessing, Model Saving
* 👨‍💻 **[Ankur Halder](https://github.com/Ankur-Halder)** – Exploratory Data Analysis, Testing, Input Validations
* 👨‍🔬 **[Rohit Gomes](https://github.com/RJxGAMERxYT)** – Model Design, Tuning, Deployment, Project Lead

---

## 🛠️ How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/employee-attrition-predictor.git
   cd employee-attrition-predictor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   python app/app.py
   ```

4. Open browser and go to `http://localhost:5000`

---

## 📌 Future Improvements

* SHAP-based interpretability for predictions
* Excel input/output support
* Email alerts for high-risk predictions
* CI/CD pipeline with GitHub Actions

---

## 📜 License

This project is developed purely for educational and demo purposes.

---

## 🙏 Acknowledgement

Thanks to the Kaggle dataset providers and the open-source ML community for tools and resources that made this project possible.

---

## 📊 Power BI Dashboard

This repository also includes a fully interactive Power BI dashboard analyzing the same dataset used in the ML model.

📁 **File**: [Employee_Attrition_Dashboard.pbix](./Employee_Attrition_Dashboard.pbix)

## Dashboard Preview 
  
![Dashboard Preview](DASHBOARD%20PREVIEW.png)


### Highlights:
- 📌 KPI Cards for Total Employees, Attrition Count, Retention Rate, and Average Tenure
- 🧩 Attrition breakdown by Department, Overtime Status, Education Field, and Job Satisfaction
- 📊 Clustered charts for Age vs Attrition and Overtime Impact
- 📅 Filter slicers for Gender and Marital Status

This dashboard offers a visual storytelling layer on top of the ML prediction engine and is helpful for HR managers and stakeholders.


