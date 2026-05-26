from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
brain = joblib.load('saas_saver_brain.joblib')

@app.post("/predict")
def predict_churn(customer_data: dict):
    
    # 1. The Waiter takes the JSON order
    df = pd.DataFrame([customer_data])
    
    # 2. THE BOUNCER: We explicitly define the exact column order the AI memorized during training.
    # (Pandas get_dummies sorts things alphabetically by default)
    expected_columns = [
        "tenure", 
        "MonthlyCharges", 
        "Contract_Month-to-month", "Contract_One year", "Contract_Two year", 
        "InternetService_DSL", "InternetService_Fiber optic", "InternetService_No",
        "TechSupport_No", "TechSupport_No internet service", "TechSupport_Yes"
    ]
    
    # 3. We force our DataFrame to rearrange itself to match this exact list
    df = df[expected_columns]
    
    # 4. The Chef makes the prediction
    prediction = brain.predict(df)[0]
    
    if prediction == 1:
        result = "High Risk: Customer will likely churn!"
    else:
        result = "Safe: Customer will likely stay."
        
    return {"prediction": result}