# pands project
# Author: Paul Cahill

# libraries
import pandas as pd

# importing the dataset
df = pd.read_csv("iris.data")
print(df)

# naming the columns
columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','class']
df.columns = columns

# Checking the types of data held in the dataset
print("Types of data:", df.dtypes)

# summary of data
print (df.describe())