import pandas as pd

# Load dataset with 'Name' as index
data = pd.read_csv(r'D:\documents\study notes\DATA ANALYISIS\python packages\pandas\DataFrame\2file.csv', index_col="Name")

# Display the dataset
print("Dataset (first 5 rows):")
print(data.head())

# -------------------------
# 1. DataFrame[] - Basic indexing
# -------------------------
print("\n1. DataFrame[] - Basic Column Selection:")
print(data["Team"])  # Single column
print(data[["Team", "Age"]])  # Multiple columns

# -------------------------
# 2. DataFrame.loc[] - Label-based indexing
# -------------------------
print("\n2. DataFrame.loc[] - Label-based Row and Column Selection:")
print(data.loc["Avery Bradley"])  # Single row
print(data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Position"]])  # Multiple rows and columns

# -------------------------
# 3. DataFrame.iloc[] - Position-based indexing
# -------------------------
print("\n3. DataFrame.iloc[] - Position-based Row and Column Selection:")
print(data.iloc[0])  # First row
print(data.iloc[[0, 1], [0, 2]])  # Multiple rows and columns by position (Team and Position of 1st and 2nd row)

# -------------------------
# 4. DataFrame.ix[] - Deprecated (for reference only)
# -------------------------
# .ix was deprecated in Pandas 0.20.0 and removed in later versions.
# This is just for educational purposes (you should NOT use .ix in new code).
# If you're using a very old version of pandas (before 0.20), this would work:
# print("\n4. DataFrame.ix[] - Combined label and position-based selection:")
# print(data.ix[["Avery Bradley"], ["Team", "Position"]])

print("\nNote: .ix[] has been removed from recent versions of pandas. Use .loc[] or .iloc[] instead.")
