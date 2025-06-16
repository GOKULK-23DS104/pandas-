import pandas as pd

# First read without setting index_col
data = pd.read_csv(r'D:\documents\study notes\DATA ANALYISIS\python packages\pandas\DataFrame\1file.csv')
print("Column names:", data.columns.tolist())  # This will show available columns
print("\nFirst few rows:")
print(data.head())