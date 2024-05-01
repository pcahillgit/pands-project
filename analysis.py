# pands project
# This is the script which contains all my code used to produce my analysis of Fisher's Iris dataset.
# Author: Paul Cahill

# I start off by importing the dataset and defining the columns,
# then I produce some summary statistics (first rows of the dataframe, types, unique classes, numerical data summaries). When run this will save a .txt file with results
# followed by plots: histograms (one for each variable), then a pairplot of the pairs of variables. When run this will save two PNG files with figures.
# I then finish with some additional analysis (examining the correlation coefficient of the pairs of variables). When run this will save a .txt file with results.
# The outputs of this code are saved in the repository.


### LIBRARIES ###

# Libraries:
# Data frames
import pandas as pd

# Plotting
import matplotlib.pyplot as plt

# Seaborn for pairplot
import seaborn as sns

# NumPy which I use for correlation coefficients
import numpy as np

# Numerical arrays
import pandas as pd


### IMPORTING DATASET ###


# Importing the dataset
df = pd.read_csv("iris.data")
print(df)

# Naming the variables
columns = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','class']
df.columns = columns

# Defining labels for these variables
labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']


### VARIABLE SUMMARIES ###


# Summarising the variables:
# Displaying the dataframe (first five values)
df.head(5)

# Checking the types of data held in the dataset
df.dtypes

# Showing the unique class (species) values
df['class'].unique()

# Summary of numerical data (these show as type float64, they are floating point numbers (stored using 64 bits)- in this case it's the physical dimensions of the iris)
df.describe()

# Saving the output of the summaries as a text file
# Opening a file called summary.txt in write mode ("w") and attributing it to the variable text_file, then filling the file with the summary statistics above as strings.
# \n here is a line break
# the join function allows us to take the unique class variables as an array and convert them to a string seperated by commas.
with open("summary.txt", "w") as text_file: 
    text_file.write("Summary of the Iris Dataset Variables:\n\n\n")
    text_file.write("- First Five Rows of the Dataset:\n\n")
    text_file.write(df.head(5).to_string())
    text_file.write("\n\n- Types of Data:\n\n")
    text_file.write(df.dtypes.to_string())
    text_file.write("\n\n- Listing Unique Class Variables (Species of Iris):\n\n")
    text_file.write(", ".join(df['class'].unique()))
    text_file.write("\n\n- Summary of Numerical Variables:\n\n")
    text_file.write(df.describe().to_string())


### HISTOGRAMS ### 


# Histograms
# Defining unifrom colour scheme for each species
colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'orange', 'Iris-virginica': 'green'}

# Creating figure with subplots in 2 by 2 style, setting the size of the figure (length, height).
# Setting the axes to a 1 dimensional array (this makes it easier to work with)
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs = axs.flatten()

# Making a loop and looping through each variable
# var = variable, label = it's respective label
# Zip pairs these variables and labels together as tuples one by one
# Enumerate indexes these tuples, starting with 0 (we have 4 plots so these will go from 0 to 3)
for i, (var, label) in enumerate(zip(columns, labels)):
    # Plotting, distinguishing by colour, setting number of bins, labelling and adding transparency (alpha)
    for species, color in colors.items():
        data = df[df['class'] == species][var]
        axs[i].hist(data, bins=9, color=color, alpha=0.8, label=species)

    # Setting axes labels and titles
    # Combining labels with 'cm'
    axs[i].set_xlabel(label + ' (cm)')
    # Setting the Y label for each plot
    axs[i].set_ylabel('Frequency')
    # Combining Histogram of and the label
    axs[i].set_title('Histogram of ' + label)

    # Adding legend to the first subplot (0 here is the first subplot (this was defined when we enumerated the tuples))
    if i == 0:
        axs[i].legend()

# Adjusting the padding between and around subplots, this ensures no overlap between the plot titles/axes labels, etc.
plt.tight_layout()

# Saving the 4 histograms figure as a PNG
plt.savefig('histograms_of_iris_variables.png')

### PAIRPLOT ###
# As opposed to creating 6 individual scatterplots I created a pairplot using seaborn.
# As opposed to plotting histograms within this pairplot, as these have already been produced, I chose to use kernal density estimates.

# Creating the pairplot using the dataframe, setting the diagonal boxes as kernal density estimates (kde),
# highlighting species by setting hue as class, coloring the classes in an easy to distinguish palette.
sns.pairplot(df, diag_kind = 'kde', hue = 'class', palette = 'colorblind')

# Adjusting the padding between and around subplots, again this prevents any crossover between titles/axes labels, etc.
plt.tight_layout()

# Saving the figure as a PNG
plt.savefig('pairplots.png')


### ADDITIONAL ANALYSIS ###


# Additional Analysis:
# Measuring the correlation coefficients of each pair of variables

# Excluding the class column
columns_no_class = df.columns[:-1] 

# Creating an empty DataFrame (this is done with pandas) to store correlation coefficients
correlation_df = pd.DataFrame(index=columns_no_class, columns=columns_no_class)

# Performing a loop which takes each pair of variables and computes their correlation coefficients in a table
for col1 in columns_no_class:
    for col2 in columns_no_class:
        correlation = np.corrcoef(df[col1], df[col2])
        correlation_coefficient = correlation[0, 1]
        #setting the correlation coefficient for the row and column
        correlation_df.loc[col1, col2] = correlation_coefficient

# As with the other analysis above, this code will save the output as a .txt file in the repository
# w is write mode, \n is returning a line and to_strong converts the correlation dataframe into a string which can then be written into the text file
with open("correlation_coefficients.txt", "w") as text_file: 
    text_file.write("Correlation Coefficients:\n\n\n")
    text_file.write(correlation_df.to_string())


### END ###