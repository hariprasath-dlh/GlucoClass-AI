# 🩺 GlucoClass AI – Diabetes Prediction System

GlucoClass AI is a machine learning-based application that predicts whether a person has diabetes using medical diagnostic data. It leverages the Pima Indians Diabetes dataset and applies Logistic Regression to provide fast and accurate predictions based on user input.

---

## 📌 Features

* 🧠 Predicts diabetes based on medical parameters
* ⚡ Uses Logistic Regression (supervised learning)
* 📊 Trained on real-world healthcare dataset
* ⌨️ Accepts user input through terminal
* 📂 Simple and beginner-friendly implementation
* 🎯 Fast and accurate predictions

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Machine Learning

---
```
## 📁 Project Structure

GlucoClass-AI/
│── main.py
│── model.py
│── requirements.txt
│── data/
│    └── diabetes.csv
│── README.md
```
---

## ⚙️ How It Works

1. The dataset is loaded from the data folder
2. Features and target variable are separated
3. A Logistic Regression model is trained
4. User provides medical input values
5. The model predicts diabetes status
6. Result is displayed clearly

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

git clone https://github.com/YOUR_USERNAME/GlucoClass-AI.git

### Step 2: Navigate to the project folder

cd GlucoClass-AI

### Step 3: Install dependencies

pip install -r requirements.txt

### Step 4: Run the program

python main.py

---

## 🧪 Sample Input

Pregnancies: 2
Glucose: 150
Blood Pressure: 85
Skin Thickness: 30
Insulin: 130
BMI: 32.0
Diabetes Pedigree Function: 0.5
Age: 45

---

## ✨ Sample Output

Prediction: Diabetes

---

## 📊 Dataset Information

This project uses the **Pima Indians Diabetes Dataset**, which contains medical diagnostic measurements such as glucose level, BMI, insulin, and age to predict diabetes occurrence.

---

## 🧠 Key Concept

The project uses **Logistic Regression**, a supervised machine learning algorithm used for classification problems. It learns patterns from historical medical data to predict whether a patient is diabetic or not.

---

## 🎯 Future Improvements

* Web-based interface
* Real-time patient data integration
* Advanced models (Random Forest, XGBoost)
* Risk level prediction (Low/Medium/High)
* Data visualization dashboard

---

## 👨‍💻 Author

Hariprasath
B.Tech Artificial Intelligence and Data Science

---

## 📌 Note

This project is developed for academic purposes to demonstrate machine learning-based classification using healthcare data.
