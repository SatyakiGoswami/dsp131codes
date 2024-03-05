import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
mean_visibility = df['Visibility_km'].mean()
print("mean visibility:",mean_visibility)
