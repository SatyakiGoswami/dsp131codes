import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
snow_instances = df[df['Weather'].str.contains('Snow')]
print(snow_instances)

