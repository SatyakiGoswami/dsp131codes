import pandas as pd

df = pd.read_csv('weather.csv')
wind_speed_count = df[df['Wind Speed_km/h'] == 4].shape[0]

print("Number of times when the wind speed was exactly 4 km/h:", wind_speed_count)

