"""You can use a boolean mask to filter rows with missing values.

python
Copy
Edit"""
import pandas as pd

data = pd.read_csv("employees.csv")
missing_gender_data = data[pd.isnull(data["Gender"])]
print(missing_gender_data)