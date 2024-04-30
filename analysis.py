# pands project
# This is the script which contains all my code used to produce my analysis of Fisher's Iris dataset.
# Author: Paul Cahill

# I start off by importing the dataset and defining the columns,
# then I produce some summary statistics (first rows of the dataframe, types, unique classes, numerical data summaries),
# followed by plots: histograms (one for each variable), then a pairplot of the pairs of variables.
# I then finish with some additional analysis (correlation coefficient, ).
# The outputs of this code are saved in the repository.

### LIBRARIES ###

# Libraries:
# Data frames
import pandas as pd

# Plotting
import matplotlib.pyplot as plt

# Seaborn for pairplot
import seaborn as sns

### IMPORTING DATASET ###

# Importing the dataset
df = pd.read_csv("iris.data")
print(df)

# Naming the columns
columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','class']
df.columns = columns

### VARIABLE SUMMARIES ###

# Summarising the variables:
# Displaying the dataframe (first five values)
print("First five rows of the dataset:\n", df.head(5))

# Checking the types of data held in the dataset
print("\n\nTypes of data:\n", df.dtypes)

# Showing the unique class (species) values
print("\n\nListing unique class variables (species of iris):\n",df['class'].unique())

# Summary of numerical data (these show as type float64, they are floating point numbers (stored using 64 bits)- in this case it's the physical dimensions of the iris)
print("\n\nSummary of numerical data:\n", df.describe()) 

# Saving the output of the summaries as a text file
# Opening a file called summary.txt in write mode ("w") and attributing it to the variable text_file, then filling the file with the summary statistics above as strings.
# \n here is a line break
# the join function allows us to take the unique class variables as an array and convert them to a string seperated by commas.
with open("summary.txt", "w") as text_file: 
    text_file.write("Summary of the Iris Dataset Variables:\n\n\n")
    text_file.write("- First Five Rows of the Dataset):\n\n")
    text_file.write(df.head(5).to_string())
    text_file.write("\n\n- Types of Data:\n\n")
    text_file.write(df.dtypes.to_string())
    text_file.write("\n\n- Listing Unique Class Variables (Species of Iris):\n\n")
    text_file.write(", ".join(df['class'].unique()))
    text_file.write("\n\n- Summary of Numerical Variables:\n\n")
    text_file.write(df.describe().to_string())

'''  

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

### PAIRPLOT ###

# As opposed to creating 6 individual scatterplots I created a pairplot using seaborn.
# As opposed to plotting histograms within this pairplot, as these have already been produced, I chose to use kernal density estimates.

# Creating the pairplot using the dataframe, setting the diagonal boxes as kernal density estimates,
# highlighting species by setting hue as class, coloring the classes in easy to distinguish palette.
sns.pairplot(df, diag_kind = 'kde', hue = 'class', palette = 'colorblind')

# Saving the figure as a PNG
plt.savefig('pairplots.png')

'''
'''

### ADDITIONAL ANALYSIS ###

# Additional Analysis:

# Measuring the correlation
correlation = np.corrcoef('sepal width (cm)', 'petal length (cm)')

### END ###

'''