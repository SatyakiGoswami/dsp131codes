import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
pressure_std = df['Press_kPa'].std()
print("Standar deviation:",pressure_std)