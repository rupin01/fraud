Here’s a brief description of the uploaded files:

FDM.ipynb – This appears to be a Jupyter Notebook, likely containing code, data analysis, and visualizations related to fraud detection or financial data modeling.

Fraud_Analysis_Dataset.csv – A dataset related to fraud analysis, probably containing transaction details such as amount, type, origin, and destination balances, which may be used for training or evaluating fraud detection models.

fraud_rule_model.joblib – A saved model file in joblib format. It likely contains a trained fraud detection model that can be loaded for making predictions.

st_app.py – A Streamlit-based web application for fraud detection. It:

Loads or creates a rule-based fraud detection model.
Allows users to input transaction details (type, amount, balances).
Uses simple rules (e.g., "TRANSFER" with zero balance or amount above 10,000) to predict fraud.
Displays results and optionally shows a sample of the fraud dataset.
