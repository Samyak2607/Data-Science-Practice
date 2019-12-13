
import pandas as pd

ri = pd.read_csv('police.csv')
print(ri.head())

print(ri.isnull().sum())
# print(ri.info())

print(ri.shape)


ri.drop(['county_name', 'state'], axis='columns', inplace=True)
print(ri.shape)

print(ri.isnull().sum())
ri.dropna(subset=['driver_gender'], inplace=True)

print(ri.isnull().sum())

print(ri.shape)

print(ri.is_arrested.head())

ri['is_arrested'] = ri.is_arrested.astype('bool')

print(ri.is_arrested.dtype)

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

ri['stop_datetime'] = pd.to_datetime(combined)

print(ri.dtypes)

ri.set_index('stop_datetime', inplace=True)

print(ri.index)

print(ri.columns)

print(ri.violation.value_counts())

print(ri.violation.value_counts(normalize=True))

female = ri[ri.driver_gender == 'F']
male = ri[ri.driver_gender == 'M']
print(female.violation.value_counts(normalize = True))

print(male.violation.value_counts(normalize=True))

female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

print(female_and_speeding.stop_outcome.value_counts(normalize = True))

print(male_and_speeding.stop_outcome.value_counts(normalize = True))

print(ri[ri.driver_gender == 'F'].search_conducted.mean())

print(ri.groupby('driver_gender').search_conducted.mean())

print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())

print(ri.search_type.value_counts())

ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# print(ri.frisk.dtype)
print(ri.frisk.sum())

searched = ri[ri.search_conducted == True]

print(searched.frisk.mean())

print(searched.groupby('driver_gender').frisk.mean())

#Does time of day affect arrest rate

print(ri.is_arrested.mean())

print(ri.groupby(ri.index.hour).is_arrested.mean())
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()
import matplotlib.pyplot as plt
plt.plot(hourly_arrest_rate)
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')
plt.show()

#Are drug-related stops on the rise?
print(ri.drugs_related_stop.resample('A').mean())

annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

plt.plot(annual_drug_rate)
plt.show()
annual_search_rate = ri.search_conducted.resample('A').mean()
annual = pd.concat([annual_drug_rate, annual_search_rate], axis=1)
annual.plot(subplots=True)
plt.show()

print(pd.crosstab(ri.district, ri.violation))
all_zones = pd.crosstab(ri.district, ri.violation)
print(all_zones.loc['Zone K1': 'Zone K3'])
k_zones = all_zones.loc['Zone K1': 'Zone K3']

k_zones.plot(kind='bar')

plt.show()

k_zones.plot(kind='bar', stacked=True)

plt.show()


#How long might you be stopped for a violation?
print(ri.stop_duration.unique())

mapping = {'0-15 Min':8, '16-30 Min':23, '30+ Min':45}

ri['stop_minutes'] = ri.stop_duration.map(mapping)

print(ri.stop_minutes.unique())

print(ri.groupby('violation_raw').stop_minutes.mean())

stop_length = ri.groupby('violation_raw').stop_minutes.mean()

stop_length.sort_values().plot(kind='barh')

plt.show()
