import pandas as pd

weather = pd.read_csv('weather.csv')

print(weather[['TMIN', 'TAVG', 'TMAX']].describe())

weather[['TAVG', 'TMIN', 'TMAX']].plot(kind='box')

plt.show()

weather['TDIFF'] = weather.TMAX - weather.TMIN

print(weather.TDIFF.describe())

weather.TDIFF.plot(kind='hist', bins=20)

plt.show()

WT = weather.loc[:,'WT01': 'WT22']

weather['bad_conditions'] = WT.sum(axis='columns')

weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

weather.bad_conditions.plot(kind = 'hist')

plt.show()

print(weather.bad_conditions.value_counts().sort_index())

mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad',4:'bad', 5:'worse', 6:'worse',7:'worse',8:'worse',9:'worse'}
weather['rating'] = weather.bad_conditions.map(mapping)
print(weather.rating.value_counts()) 

cats = ['good', 'bad', 'worse']

weather['rating'] = weather.rating.astype('category', ordered=True, categories=cats)

print(weather.rating.head())