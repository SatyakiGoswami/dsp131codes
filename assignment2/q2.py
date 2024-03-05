import pandas as pd

df = pd.read_csv('weather.csv')

clear_weather_count = df[df['Weather'] == 'Mainly Clear'].shape[0]

print("Number of times when the weather is exactly clear:", clear_weather_count)
