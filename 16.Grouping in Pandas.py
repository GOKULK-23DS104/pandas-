import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Maths': [90, 85, 90, 70, 85, 70, 90, 85],
    'Science': [88, 90, 88, 80, 90, 80, 88, 90],
    'Cut': ['Excellent', 'Good', 'Excellent', 'Poor', 'Good', 'Poor', 'Excellent', 'Good'],
    'Color': ['Red', 'Blue', 'Red', 'Yellow', 'Blue', 'Yellow', 'Red', 'Blue']
})

# Display the original DataFrame
print("Original DataFrame:\n", df)

# -----------------------------------
# Group by 'Maths' and show first entry in each group
# -----------------------------------
grouped_math = df.groupby(by=['Maths'])
print("\nFirst entry in each 'Maths' group:\n", grouped_math.first())

# -----------------------------------
# Group by 'Maths' and 'Science'
# -----------------------------------
grouped_math_sci = df.groupby(['Maths', 'Science'])
print("\nFirst entry in each 'Maths-Science' group:\n", grouped_math_sci.first())

# -----------------------------------
# Group by 'Cut' and 'Color' and find the minimum in each group
# -----------------------------------
grouped_cut_color = df.groupby(['Cut', 'Color']).agg('min')
print("\nMinimum value in each 'Cut-Color' group:\n", grouped_cut_color)
