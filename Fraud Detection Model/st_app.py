import streamlit as st  
import pandas as pd  
import joblib  
import os  

# Define a simple rule-based model class  
class RuleBasedFraudDetector:  
    def __init__(self):  
        # You can add model parameters or rules here if needed  
        pass  

    def predict(self, data):  
        # Example rule: if the transaction type is "TRANSFER" and the new balance of origin is zero, it's fraud.  
        # Otherwise, if the amount is above a threshold (say 10000), mark as fraud.  
        # This is a simple logic for demonstration only.  
        predictions = []  
        for i, row in data.iterrows():  
            if row['type'] == 'TRANSFER' and row['newbalanceOrig'] == 0:  
                predictions.append(1)  
            elif row['amount'] > 10000:  
                predictions.append(1)  
            else:  
                predictions.append(0)  
        return predictions  

# File path for saving the model  
MODEL_FILE = "fraud_rule_model.joblib"  

# Function to load or create model  
def load_or_create_model():  
    if os.path.exists(MODEL_FILE):  
        model = joblib.load(MODEL_FILE)  
    else:  
        model = RuleBasedFraudDetector()  
        joblib.dump(model, MODEL_FILE)  
    return model  

# Load the model  
model = load_or_create_model()  

# Streamlit UI  
st.title("Fraud Detection Application")  

st.write("This application predicts if a transaction is fraudulent based on a simple rule-based model.")  

# Input fields for transaction details  
transaction_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT"])  
amount = st.number_input("Amount", min_value=0.0, value=0.0, step=1.0)  
oldbalanceOrg = st.number_input("Origin Old Balance", min_value=0.0, value=0.0, step=1.0)  
newbalanceOrig = st.number_input("Origin New Balance", min_value=0.0, value=0.0, step=1.0)  
oldbalanceDest = st.number_input("Destination Old Balance", min_value=0.0, value=0.0, step=1.0)  
newbalanceDest = st.number_input("Destination New Balance", min_value=0.0, value=0.0, step=1.0)  

if st.button("Predict Fraud"):  
    # Create a DataFrame from the inputs  
    input_data = pd.DataFrame({  
        "type": [transaction_type],  
        "amount": [amount],  
        "oldbalanceOrg": [oldbalanceOrg],  
        "newbalanceOrig": [newbalanceOrig],  
        "oldbalanceDest": [oldbalanceDest],  
        "newbalanceDest": [newbalanceDest]  
    })  
    
    # Get prediction (1 indicates fraud, 0 indicates normal)  
    prediction = model.predict(input_data)[0]  
    
    # Display the result  
    if prediction == 1:  
        st.error("Prediction: Fraudulent Transaction")  
    else:  
        st.success("Prediction: Normal Transaction")  

# Additional section: display dataset sample for user reference  
if st.checkbox("Show sample of Fraud Analysis Dataset"):  
    try:  
        df = pd.read_csv("Fraud_Analysis_Dataset.csv", encoding="ascii")  
        st.write("Dataset sample:")  
        st.write(df.head())  
    except Exception as e:  
        st.write("Error loading data file: " + str(e))  
