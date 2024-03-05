import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
weathers = df['Weather']
for i in weathers:
    print(df.mean())