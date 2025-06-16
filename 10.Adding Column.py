import pandas as pd
sdf = pd.DataFrame()
sdf['Name'] = ['Raja','Rani','Muthu', 'Suman']
sdf['m1'] = [20, 19, 20, 14]
sdf['m2'] = [35, 45, 23, 40]
sdf['tot'] = sdf['m1']+sdf['m2']
print(sdf)
