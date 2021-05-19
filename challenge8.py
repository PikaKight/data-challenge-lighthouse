import pandas as pd

df = pd.read_csv("milk.csv")

max_milk = df["Monthly milk production: pounds per cow"].max()
max_milk_index = df["Monthly milk production: pounds per cow"].idxmax()
print(df.loc(max_milk_index))

min_milk = df["Monthly milk production: pounds per cow"].min()
min_milk_index = df["Monthly milk production: pounds per cow"].idxmin()
print(df.iloc(min_milk_index))