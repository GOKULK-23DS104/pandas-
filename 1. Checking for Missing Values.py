"""Pandas provides two useful functions:

isnull() – Returns True for NaN values.

notnull() – Returns True for non-NaN values.

python
Copy
Edit"""
import pandas as pd
import numpy as np

data = {
    'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score': [np.nan, 40, 80, 98]
}
df = pd.DataFrame(data)
print(df.isnull())