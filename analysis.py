# pands project
# This is the script which contains all my code used to produce my analysis of Fisher's Iris dataset.
# I start off by importing the dataset and defining the columns, then I produce some summary statistics
# followed by plots (histograms (one for each variable), then scatterplots (one for each pair of variables)) and finish with some additional analysis.
# The outputs of this code are saved in the repository.
# Author: Paul Cahill

### LIBRARIES ###

# Libraries:
# Data frames
import pandas as pd

# Plotting
import matplotlib.pyplot as plt

# Plotting Scatterplot
import seaborn as sns

### IMPORTING DATASET ###

# Importing the dataset
df = pd.read_csv("iris.data")
print(df)

# Naming the columns
columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','class']
df.columns = columns

### VARIABLE SUMMARIES ###

'''

# Summarising the variables:
# Displaying the dataframe (first three values)
print("First three rows of the dataset:\n", df.head(3))

# Checking the types of data held in the dataset
print("\n\nTypes of data:\n", df.dtypes)

# Showing the unique class (species) values
print("\n\nListing unique class variables (species of iris):\n",df['class'].unique())

# Summary of numerical data (these show as type float64, they are floating point numbers (stored using 64 bits)- in this case it's the physical dimensions of the iris)
print("\n\nSummary of numerical data:\n", df.describe()) 

# Saving the output of the summaries as a text file
# Opening a file called summary.txt in write mode ("w") and attributing it to the variable text_file, then filling the file with the summary statistics above as strings.
with open("summary.txt", "w") as text_file:
    text_file.write("First three rows of the dataset:\n")
    text_file.write(df.head(3).to_string())
    text_file.write("\n\nTypes of data:\n")
    text_file.write(df.dtypes.to_string())
    text_file.write(df['class'].unique().to_string())
    text_file.write("\n\nListing unique class variables (species of iris):\n")
    text_file.write("\n\nSummary of numerical data:\n")
    text_file.write(df.describe().to_string())

### HISTOGRAMS ###

# Histograms:

# Sepal Length
# Filtering the dataset by class
setosa_sepallength = df[df['class'] == 'Iris-setosa']['sepal length (cm)']
versicolor_sepallength = df[df['class'] == 'Iris-versicolor']['sepal length (cm)']
virginica_sepallength = df[df['class'] == 'Iris-virginica']['sepal length (cm)']

# Plotting the three species individually on one plot, distinguishing by colour, labelling and adding a light transparency (alpha)
plt.hist(setosa_sepallength, bins=9, color='blue', alpha=0.8, label='Setosa')
plt.hist(versicolor_sepallength, bins=9, color='orange', alpha=0.8, label='Versicolor')
plt.hist(virginica_sepallength, bins=9, color='green', alpha=0.8, label='Virginica')

# Axis labels
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

# Title
plt.title('Histogram of Iris Sepal Length (by Species)')

# Legend
plt.legend()

# Saving plot as a PNG
plt.savefig('histogram of Iris Sepal Length (by Species)'.png)

# Sepal Width
# Filtering the dataset by class
setosa_sepalwidth = df[df['class'] == 'Iris-setosa']['sepal width (cm)']
versicolor_sepalwidth = df[df['class'] == 'Iris-versicolor']['sepal width (cm)']
virginica_sepalwidth = df[df['class'] == 'Iris-virginica']['sepal width (cm)']

# Plotting the three species individually on one plot, distinguishing by colour, labelling and adding a light transparency (alpha)
plt.hist(setosa_sepalwidth, bins=9, color='blue', alpha=0.8, label='Setosa')
plt.hist(versicolor_sepalwidth, bins=9, color='orange', alpha=0.8, label='Versicolor')
plt.hist(virginica_sepalwidth, bins=9, color='green', alpha=0.8, label='Virginica')

# Axis labels
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

# Title
plt.title('Histogram of Iris Sepal Width (by Species)')

# Legend
plt.legend()

# Saving plot as a PNG
plt.savefig('histogram of Iris Sepal Width (by Species)'.png)

# Petal Length
# Filtering the dataset by class
setosa_petallength = df[df['class'] == 'Iris-setosa']['petal length (cm)']
versicolor_petallength = df[df['class'] == 'Iris-versicolor']['petal length (cm)']
virginica_petallength = df[df['class'] == 'Iris-virginica']['petal length (cm)']

# Plotting the three species individually on one plot, distinguishing by colour, labelling and adding a light transparency (alpha)
plt.hist(setosa_petallength, bins=9, color='blue', alpha=0.8, label='Setosa')
plt.hist(versicolor_petallength, bins=9, color='orange', alpha=0.8, label='Versicolor')
plt.hist(virginica_petallength, bins=9, color='green', alpha=0.8, label='Virginica')

# Axis labels
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

# Title
plt.title('Histogram of Iris Petal Length (by Species)')

# Legend
plt.legend()

# Saving plot as a PNG
plt.savefig('histogram of Iris Petal Length (by Species).png')

# Petal Width
# Filtering the dataset by class
setosa_petalwidth = df[df['class'] == 'Iris-setosa']['petal width (cm)']
versicolor_petalwidth = df[df['class'] == 'Iris-versicolor']['petal width (cm)']
virginica_petalwidth = df[df['class'] == 'Iris-virginica']['petal width (cm)']

# Plotting the three species individually on one plot, distinguishing by colour, labelling and adding a light transparency (alpha)
plt.hist(setosa_petalwidth, bins=9, color='blue', alpha=0.8, label='Setosa')
plt.hist(versicolor_petalwidth, bins=9, color='orange', alpha=0.8, label='Versicolor')
plt.hist(virginica_petalwidth, bins=9, color='green', alpha=0.8, label='Virginica')

# Axis labels
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# Title
plt.title('Histogram of Iris Petal Width (by Species)')

# Legend
plt.legend()

# Saving plot as a PNG
plt.savefig('histogram of Iris Petal Width (by Species).png')

### SCATTERPLOTS ###

# As opposed to creating 6 individual scatterplots I created a pairplot using seaborn.
# As opposed to plotting histograms in this pairplot, as these have already been produced, I chose to use kernal density estimates.

# Creating the pairplot using the dataframe, setting the diagonal boxes as kernal density estimates,
# highlighting species by setting hue as class, coloring the classes in easy to distinguish palette.
sns.pairplot(df, diag_kind = 'kde', hue = 'class', palette = 'colorblind')

# Saving the figure as a PNG
plt.savefig('pairplots.png')

'''

### ADDITIONAL ANALYSIS ###

# Additional Analysis:
#

### END ###