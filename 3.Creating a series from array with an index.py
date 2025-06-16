import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e'])
ser = pd.Series(data, index=[1,2,3,4,5])
print(ser)