# GlucoClass AI

A beginner-friendly machine learning project that predicts the likelihood of diabetes based on medical data using the Pima Indians Diabetes dataset.

## Features
- Loads and processes the dataset robustly.
- Uses **Logistic Regression** (Scikit-learn) for classification.
- Takes dynamic user input from the terminal.
- Provides a clear prediction: **Diabetes** or **No Diabetes**.

## Tech Stack
- **Python**: Core programming language.
- **Pandas**: For loading and handling the structured dataset.
- **Scikit-learn**: For building and training the Logistic Regression model.

## Folder Structure
```
GlucoClass-AI/
│── main.py
│── model.py
│── data/
│    └── diabetes.csv  <-- You need to place your Kaggle dataset here
│── requirements.txt
│── README.md
```

## How to Run

1. **Install Dependencies**  
   Open your terminal in VS Code and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add Dataset**  
   Download the **Pima Indians Diabetes dataset** (`diabetes.csv`) from Kaggle and place it directly inside the `data/` folder. Ensure it contains the standard 8 feature columns and the `Outcome` target column.

3. **Run the Project**  
   Execute the `main.py` file to start the application:
   ```bash
   python main.py
   ```

## Sample Input/Output

**Input Session:**
```
=========================================
         GlucoClass AI Predictor         
=========================================
Please enter the following medical details:
Pregnancies: 2
Glucose: 150
Blood Pressure: 70
Skin Thickness: 30
Insulin: 120
BMI: 34.5
Diabetes Pedigree Function: 0.8
Age: 45

Analyzing data...
Loading dataset from data/diabetes.csv...
Training the Logistic Regression model...
Model trained successfully!

-----------------------------------------
Prediction: Diabetes
-----------------------------------------
```
