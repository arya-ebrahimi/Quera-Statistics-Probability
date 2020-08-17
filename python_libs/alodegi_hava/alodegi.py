import numpy as np
import pandas as pd

aqi_data = pd.read_csv("AQI2018.csv")
aqi_data.head()


#dates

df = aqi_data.groupby('Date').AQI.mean()
df = df.nlargest(10)
print(df)
df.to_csv('dates.csv',header = False)

#states

df = aqi_data.groupby('State Name').AQI.median()
df = df.sort_values(ascending = False)
df = df.head(10)
df.to_csv('states.csv',header = False)

#parameters

df = aqi_data[aqi_data['county Name'] == 'San Diego']
df = df.groupby('Defining Parameter').nunique().Date
df = df.sort_values(ascending = False)
df.to_csv('parameters.csv',header = False)