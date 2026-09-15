# Telco Customer Churn Analysis & Prediction

This project analyzes Telco customer data to understand and predict customer churn using data visualization techniques.

### Features
- **Stacked Count Plot:** Visualizes churn count across categories (Contract, InternetService, PaymentMethod, SeniorCitizen)
- **100% Stacked Count Plot:** Shows churn percentage for better comparison
- **Heatmap:** Correlation heatmap for numeric features (tenure, MonthlyCharges, TotalCharges, Churn) and Churn Rate heatmap

### Dataset
- `telco_churn.csv` - Contains 7043 customers with 21 features including tenure, contract, payment method, and churn status.

### Key Insights
- Month-to-month contract customers have highest churn (>40%)
- Fiber optic and Electronic check users churn more
- Longer tenure and 2-year contracts have very low churn

### How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run notebook / python file: `python churn_analysis.py`

### Tools Used
Python, Pandas, Matplotlib, Seaborn

### Author
Data Analysis Project - Telco Churn
