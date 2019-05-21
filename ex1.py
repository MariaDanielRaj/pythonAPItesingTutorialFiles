dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]


print('.')
print('.')
print('.')
brics.to_csv('my_csv.csv') #save as csv

print('.............') 
cars = pd.read_csv('my_csv.csv', index_col = 0)
print(cars)
print('.............') 
# Print out country column as Pandas Series
#print(cars['country'])

# Print out country column as Pandas DataFrame
#print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'area']])

print('.')
print('.')
# Print out first 4 observations
print(cars[0:1])
print('.')
print('.')
# Print out fifth, sixth, and seventh observation
print(cars[2:4])


print('.')
print('.')
# Print out observation for Japan
print(cars.iloc[2])
print('.')
print('.')
# Print out observations for Australia and Egypt
print(cars.loc[['RU', 'IN']])

print('.')

print(cars.iloc[[2,4]])
