import pandas as pd 
df = pd.read_csv('weather.csv')
wind_speed_data =df['Wind Speed_km/h']
unique_wind_speeds=wind_speed_data.unique()
print(unique_wind_speeds)