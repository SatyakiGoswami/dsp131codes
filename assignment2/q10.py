import pandas as pd

file_name ="weather.csv"
df = pd.read_csv('weather.csv')

wind_vis_instances = df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]

print("Number of instances with wind speed > 24 km/h and visibility 25 km:", len(wind_vis_instances))
