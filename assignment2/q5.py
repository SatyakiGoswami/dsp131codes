import pandas as pd
df = pd.read_csv('weather.csv')
df = df.rename(columns={'Weather': 'Weather condition'})

print(df.head())
