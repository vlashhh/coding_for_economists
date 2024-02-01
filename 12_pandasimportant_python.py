import pandas as pd
import numpy as np

data = {"Tokyo": 30_000_000, "Delhi": 50_000_000, "Shanghai": 20_000_000}

df = pd.DataFrame(data = data, columns = [0])

df_raw = pd.read_csv("https://osf.io/yzntm/download")

print(df)


print(df_raw.shape[0])

df = df_raw.assign(nnights = 1)

del df_raw 

df['accommodationtype'].head()

df['accommodationtype'].str.split('@')

df['accommodationtype'].str.split('@').str[1]

df['accommodationtype'].value_counts()

df.accommodationtype.replace('', 'Unknown', inplace = True)

df['ratings'] = df['guestreviewsrating'].str.split("/").strip()

df['ratings'] = df['guestreviewsrating'].str.split("/").str[0].str.strip()

df['ratings'] = df['ratings'].astype('float')


df.center1distance.mean()

df.center1distance.str.split(' ').str[0].astype('float').mean()


df['distance_numeric'] = df['center1distance'].str.split(' ').str[0].astype('float')

df.filter(regex = 'rating').head()

df.rename(columns = {'rating_reviewcount': 'rating_count', 'rating2_ta': 'ratingta', }, inplace = True)

df.rename(columns = {'ratings2_ta_reviewcount': 'ratingta_count', 'adresscountryname': 'country', 'starrating': 'stars', 's_city': 'city'}, inplace = True)


df.loc[df['accommodationtype'] == 'Hotel']

df.ratings.isnull().sum()

df['ratings'].isnull().groupby(df.country).sum()
