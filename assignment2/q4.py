import pandas as pd

df = pd.read_csv('weather.csv')
null_values = df.isnull().sum()

print("Null values in the data:")
print(null_values)
