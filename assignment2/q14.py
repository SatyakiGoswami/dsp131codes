import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
clear_or_high_visibility = df[(df['Weather Condition'] == 'clear') |(df['Visibility_km']>40)]
print(clear_or_high_visibility)