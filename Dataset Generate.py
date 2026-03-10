
# -----------------------------------------------------------------------
#                         Dataset Creation
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# number of customers
n = 10000

customer_id = np.arange(1, n+1)
vehicle_id = ["V"+str(i) for i in range(1, n+1)]

# tenure distribution
tenure = np.random.choice([1,2,3,4], size=n, p=[0.2,0.3,0.4,0.1])

purchase_dates = pd.date_range("2024-01-01","2024-12-31")
purchase = np.random.choice(purchase_dates, n)

start_date = purchase + pd.Timedelta(days=365)
end_date = start_date + pd.to_timedelta(tenure*365, unit='D')

data = pd.DataFrame({
    "Customer_ID": customer_id,
    "Vehicle_ID": vehicle_id,
    "Vehicle_Value": 100000,
    "Policy_Tenure": tenure,
    "Premium": tenure*100,
    "Policy_Purchase_Date": purchase,
    "Policy_Start_Date": start_date,
    "Policy_End_Date": end_date
})


df = pd.DataFrame(data)

try:
    df.to_csv("policy_sales_data.csv", index=False)
    print("Dataset generated successfully!")
    
except PermissionError:
    print("File close karo! Excel already open hai.")

