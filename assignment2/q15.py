import pandas as pd 
file_name ="weather.csv"
df = pd.read_csv('weather.csv')
condition_A =(df['Weather Condition']=='Clear')&(df['Rel hum_%'] > 50)
condition_B =(df['Visibility_km'] > 40)
instances =df[condition_A | condition_B]
print(instances)