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
# Displaying the dataframe (first three values)
print("First three rows of the dataset:\n", df.head(3))

# Checking the types of data held in the dataset
print("\n\nTypes of data:\n", df.dtypes)

# Showing the unique class (species) values
print("\n\nListing unique class variables (species of iris):\n",df['class'].unique())

# Summary of numerical data (these show as type float64, they are floating point numbers (stored using 64 bits)- in this case it's the physical dimensions of the iris)
print("\n\nSummary of numerical data:\n", df.describe())

'''
# Saving the output of the summaries as a text file
# Opening a file called summary.txt in write mode ("w") and attributing it to the variable text_file, then filling the file with the summary statistics above as strings.
with open("summary.txt", "w") as text_file:
    text_file.write("Types of data:\n")
    text_file.write(df.dtypes.to_string())
    text_file.write("\n\nSummary of data:\n")
    text_file.write(df.describe().to_string())
'''
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