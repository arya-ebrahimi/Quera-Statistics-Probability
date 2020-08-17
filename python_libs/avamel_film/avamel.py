import pandas as pd

df = pd.read_csv('dates.csv')
df.describe()
df.head()

df.drop(columns = ['Unnamed: 0'], inplace = True)
print(df.dtypes)

df["formatted_date"]= pd.to_datetime(df["date"])
print(df.dtypes)

df = df.set_index('formatted_date')

df.loc["2015-5":"2015-5"]


m_2005 = df.loc["2005-12"]
m_2005[m_2005['country'].str.match(r"\S")]


filter = df.loc["2000-11":"2018-11"]
filtered_df = filter[filter['title'].str.match(r'(^B.*)')]
filtered_df = filtered_df.sort_index()