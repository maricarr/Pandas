import pandas as pd
cars=pd.read_csv('cars.csv')
y=cars.iloc[0:5]
z=cars.iloc[27:32]
car=pd.concat([y,z])
print(car)