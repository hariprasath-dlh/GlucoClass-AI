from model import predict_diabetes

def main():
    print("=========================================")
    print("         GlucoClass AI Predictor         ")
    print("=========================================")
    print("Please enter the following medical details:")
    
    try:
        # 4. Take user input from terminal
        # Using float() handles both integer and decimal inputs gracefully
        pregnancies = float(input("Pregnancies: "))
        glucose = float(input("Glucose: "))
        blood_pressure = float(input("Blood Pressure: "))
        skin_thickness = float(input("Skin Thickness: "))
        insulin = float(input("Insulin: "))
        bmi = float(input("BMI: "))
        dpf = float(input("Diabetes Pedigree Function: "))
        age = float(input("Age: "))
        
        # Combine all features into a single list in the correct order
        user_input = [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]
        
        print("\nAnalyzing data...")
        
        # 5. Predict using the trained model
        result = predict_diabetes(user_input)
        
        # 6. Display result clearly
        print("\n-----------------------------------------")
        if result == 1:
            print("Prediction: Diabetes")
        elif result == 0:
            print("Prediction: No Diabetes")
        else:
            print(f"Prediction: Unknown result ({result})")
        print("-----------------------------------------")
        
    except ValueError:
        print("\nError: Please enter valid numerical values.")
    except FileNotFoundError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
