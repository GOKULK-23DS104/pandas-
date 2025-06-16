import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'}, inplace=True)
df.columns = ['X', 'Y', 'Z']
print(df)
