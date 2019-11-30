import pandas as pd
cars=pd.read_csv('cars.csv')

#Problem 2A
odd=cars.iloc[0:5,0::2]
print(odd)

#Problem 2B
MazdaRow=cars.loc[[0]]
print(MazdaRow)

#Problem 2C
cyl=cars.loc[[23],['cyl']]
print(cyl)

#Problem 2D
z=cars.loc[[1,28,18],['Model','cyl','gear']]
print(z)