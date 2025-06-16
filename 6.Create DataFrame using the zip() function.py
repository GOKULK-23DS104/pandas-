import pandas as pd
Name = ['Raja', 'Rani', 'Muthu', 'Suman']
Age = [20, 21, 19, 18]
list_of_tuples = list(zip(Name, Age))
df = pd.DataFrame(list_of_tuples,
                  columns=['Name', 'Age'])
print(df)