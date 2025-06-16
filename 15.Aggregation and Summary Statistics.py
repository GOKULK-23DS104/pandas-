import pandas as pd

df = pd.DataFrame([[9, 4, 8, 9],
                   [8, 10, 7, 6],
                   [7, 6, 8, 5]],
                  columns=['Maths', 'English',
                           'Science', 'History'])

print(df)


import pandas as pd

# Create the DataFrame
df = pd.DataFrame(
    [[9, 4, 8, 9],
     [8, 10, 7, 6],
     [7, 6, 8, 5]],
    columns=['Maths', 'English', 'Science', 'History']
)

# Display the original DataFrame
print("Original DataFrame:\n", df)

# -------------------------------
# Basic Aggregation Operations
# -------------------------------
print("\nSum of each column:\n", df.sum())
print("\nMinimum of each column:\n", df.min())
print("\nMaximum of each column:\n", df.max())
print("\nMean of each column:\n", df.mean())
print("\nStandard Deviation:\n", df.std())
print("\nVariance:\n", df.var())

# -------------------------------
# Aggregation using agg()
# -------------------------------
print("\nAggregation using agg() - multiple functions:")
agg_result = df.agg(['sum', 'min', 'max', 'mean'])
print(agg_result)

# -------------------------------
# Describe – Summary Statistics
# -------------------------------
print("\nDescriptive Statistics:\n", df.describe())

# -------------------------------
# Additional Summary Functions
# -------------------------------
print("\nCount of values in each column:\n", df.count())
print("\nFirst row values (using first()):\n", df.first_valid_index())
print("\nLast row values (using last()):\n", df.last_valid_index())
print("\nStandard error of mean (SEM):\n", df.sem())
