import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
min_values= df.groupby('Weather Conditions').min()
m_values= df.groupby('Weather Conditions').max()
print("Minimum values:")
print(min_values)
print("\nMaximum values:")
print(max_values)
