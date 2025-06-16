import pandas as pd
df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
df2 = pd.DataFrame({'c':[7,8,9],'d':[10,11,12]},index=[1,2,3])
df3 = df.join(df2)
print(df3)
