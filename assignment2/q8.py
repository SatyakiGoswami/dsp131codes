import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
humidity_variance = df['Rel Hum_%'].var()
print("Relative Humidity:",humidity_variance)