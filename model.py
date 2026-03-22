import pandas as pd
from sklearn.linear_model import LogisticRegression
import os

# Global variable to hold the trained model
_model = None

def train_model():
    """
    Loads the dataset and trains the Logistic Regression model.
    """
    global _model
    
    file_path = "data/diabetes.csv"
    
    # Check if dataset exists before proceeding
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at '{file_path}'. Please place 'diabetes.csv' in the 'data/' folder.")
        
    print("Loading dataset from data/diabetes.csv...")
    # 1. Load dataset
    df = pd.read_csv(file_path)
    
    # 2. Split into features (X) and target (y)
    # The Pima Indians Diabetes database typically has the target column named 'Outcome'
    if 'Outcome' not in df.columns:
        raise ValueError("Dataset must contain an 'Outcome' column for the target.")
        
    X = df.drop('Outcome', axis=1) # All columns except Outcome
    y = df['Outcome']              # Only the Outcome column
    
    print("Training the Logistic Regression model...")
    # 3. Train a classification model (Logistic Regression)
    _model = LogisticRegression(max_iter=1000)
    
    # Using .values removes feature names to prevent a warning when predicting with a simple list later
    _model.fit(X.values, y.values)
    print("Model trained successfully!\n")

def predict_diabetes(input_data):
    """
    Takes a 1D list/array of user input features and returns the prediction.
    """
    global _model
    
    # Train the model if it hasn't been trained yet
    if _model is None:
        train_model()
        
    # input_data is a single list of 8 features.
    # Scikit-learn expects a 2D array for predictions, so we wrap it in another list: [input_data]
    prediction = _model.predict([input_data])
    
    # Return the first (and only) prediction
    return prediction[0]
