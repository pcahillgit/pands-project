# pands project
# This is the script which contains all my code used to produce my analysis of Fisher's Iris dataset.
# I start off by importing the dataset and definng the columns, then I produce some summary statistics, followed by plots and finish with some additional analysis.
# The outputs of this code are saved in the repository.
# Author: Paul Cahill

# Libraries
import pandas as pd

# Importing the dataset
df = pd.read_csv("iris.data")
print(df)

# Naming the columns
columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','class']
df.columns = columns

# Summarising the variables:
# Checking the types of data held in the dataset
print("Types of data:\n", df.dtypes)

# Summary of data
print (df.describe())

# Saving the output of the summaries as a text file
# Opening a file called summary.txt in write mode ("w") and attributing it to the variable text_file, then filling the file with the summary statistics above as strings.
with open("summary.txt", "w") as text_file:
    text_file.write("Types of data:\n")
    text_file.write(df.dtypes.to_string())
    text_file.write("\n\nSummary of data:\n")
    text_file.write(df.describe().to_string())

'''
# Histograms:
#
#
#
#

# Scatter Plots:
#

# Additional Analysis:
#

'''