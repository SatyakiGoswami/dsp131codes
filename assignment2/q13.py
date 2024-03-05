import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
fog_records = df[df['Weather Condition']=='Fog']
print("fog records:",fog_records)