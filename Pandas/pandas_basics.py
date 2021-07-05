from re import T
import numpy as np
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import append
import pandas as pd
from pandas.core.reshape.concat import concat
import seaborn as sns

print(pd.Series([59, 2, 72, 30, 85]))
print(pd.Series([59, 2, 72, 30, 85], index = [1, 3, 5, 7, 9]))

serie = pd.Series([59, 2, 72, 30, 85])
print("concat([serie, serie]) =", concat([serie, serie]))
print("index = ",serie.index)
print(serie.keys)
print("list version = ", list(serie.items()))
print("values: ", serie.values)

## querying elements' index

print(2 in serie)
print(17 in serie)

## fancy element

print(serie[[4, 1]])

##

k = np.arange(16).reshape(4, 4)
df = pd.DataFrame(k, columns = ["var1", "var2", "var3", "var4"])
print("df = ", df)

print(df.head())

df.columns = ("variable1", "variable2", "variable3", "variable4")
print(df)

print(type(df))
print(df.values)
print(type(df.values))

dfNew = df.drop(['variable1'], axis = 1)
print("dfNew:", dfNew)

dfNew2 = df.drop(['variable2', 'variable3'], axis = 1) # axis = 1 is for columns
print("dfNew2:", dfNew2)

dfNew3 = df.drop([2], axis = 0) # axis = 0 is for rows
print("dfNew3:", dfNew3)

df.drop(["variable1"], axis = 1, inplace = True) # incplace provides changes on the dataframe permanently
print("df:", df)

l = ["variable1", "variable3", "variable6"]
for i in l:
    print(i in df)

df["variable5"] = df["variable2"]*df["variable3"]
print(df)

## loc and iloc

print("df.loc[0:3]:", df.loc[0:3])
print("df.iloc[0:3]:", df.iloc[0:3])

print(df.loc[0:4, "variable3"]) # this way could not used in iloc, its only valid for loc

print(df.iloc[:3]["variable4"]) # so for printing a specific column in iloc this way could be used

##

print(df[(df.variable3 % 2 == 0)])
print(df[(df.variable3 % 2 == 0)]["variable4"])

##

m = np.random.randint(1, 50, size = (4,4))
df1 = pd.DataFrame(m, columns = ["var1", "var2", "var3", "var4"])
print("df1", df1)

df2 = df1*2
print("df2", df2)

print("concat:", pd.concat([df1, df2], ignore_index = True))

df2.columns = ["var1", "var2", "var3", "variable4"]
print("df2", df2)

print(pd.concat([df1, df2], ignore_index = True, join = "inner"))

## merge

df1 = pd.DataFrame({'employees': ['pitircik', 'aynaz', 'deniz', 'papatya'], 
                                'group': ['engineer', 'HR', 'accounting', 'salesman']})

df2 = pd.DataFrame({'employees': ['pitircik', 'aynaz', 'deniz', 'papatya'], 
                                'starting year': ['2009', '2008', '2007', '2008']})

print(df1)
print(df2)
print(pd.merge(df1, df2))
print(pd.merge(df1, df2))

## seaborn

df = sns.load_dataset("planets")

print(df.head())
print(df.shape)
print(df.mean())
print("mean of masses:", df["mass"].mean())
print("describe:\n",df.describe())
print("describe:\n",df.describe().T) # its transpose
print(df.dropna().describe().T) # all the NaT and NaN values are dropped

## groupby

df = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'], 
                    'data': [14, 76, 23, 73, 18, 52]}, 
                    columns = ['groups', 'data'])

print(df)
print(df.groupby("groups").mean())
print(df.groupby("groups").sum())

## groupby using seaborn

df = sns.load_dataset("planets")

print(df.head()) # just used for seeing the data in a small scale
print(df.groupby("method")["distance"].mean())
print(df.groupby("method")["orbital_period"].sum())
print(df.groupby("method")["orbital_period"].describe())

##

newdf = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'], 
                    'data': [14, 76, 23, 73, 18, 52],
                    'data2': [43, 75, 28, 51, 93, 40]}, 
                    columns = ['groups', 'data', 'data2'])

print(newdf)

print(newdf.groupby("groups").mean())
print(newdf.groupby("groups").aggregate(["min", "max", np.median]))
# function which belongs to pandas are written in "", where funcitons from numpy are written in the way like np.whatsoever
print(newdf.groupby("groups").aggregate({"data": "min", "data2": "max"}))

## filter()

df = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'], 
                    'data': [14, 76, 23, 73, 18, 52],
                    'data2': [43, 75, 28, 51, 93, 40]}, 
                    columns = ['groups', 'data', 'data2'])

print(df)

def filter_func(x):
    return x["data"].std() > 40

print(df.groupby("groups").std())
print(df.groupby("groups").filter(filter_func))

## transform

df = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'], 
                    'data': [14, 76, 23, 73, 18, 52],
                    'data2': [43, 75, 28, 51, 93, 40]}, 
                    columns = ['groups', 'data', 'data2'])

print(df)

df1 = df.iloc[:, 1:3] # for excluding the values 'ABCABC'
print(df1.transform(lambda x: x.mean()-x))

## apply

df = pd.DataFrame({ 'data': [14, 76, 23, 73, 18, 52],
                    'data2': [43, 75, 28, 51, 93, 40]}, 
                    columns = ['data', 'data2'])

print(df)
print(df.apply(np.sum))
print(df.apply(np.mean))

## apply with group

df = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C'], 
                    'data': [14, 76, 23, 73, 18, 52],
                    'data2': [43, 75, 28, 51, 93, 40]}, 
                    columns = ['groups', 'data', 'data2'])

print(df.groupby("groups").apply(np.sum))

## pivot tables

titanic = sns.load_dataset("titanic")
print(titanic.head())

print(titanic.groupby("sex")[["survived"]].mean())
print(titanic.groupby(["sex", "class"])["survived"].aggregate("mean").unstack())
# unstack() provides a better appearance of the table
print(titanic.pivot_table("survived", index = "sex", columns = "class"))
# serves for the same as before print entry

age_range = pd.cut(titanic["age"], [0, 18, 65, 100])
print(age_range.head(10))

print(titanic.pivot_table("survived", ["sex", age_range], "class"))