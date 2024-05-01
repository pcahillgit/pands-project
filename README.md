# Programming and Scripting Project

![Van Goghs Irises](https://upload.wikimedia.org/wikipedia/commons/9/98/VanGoghIrises2.jpg)

## About This Repository
This repository contains my submission for the Programming and Scripting Project and contains an anlysis of the classic [Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris).

My analysis aims to demonstrate some key programming, scripting and data analytics techniques such as researching and importing a dataset, examaning and summarising its variables and plotting them in a variety of ways.

My repository is structured as follows:

- This README which provides information on the Iris dataset and lists the references used to inform my work.
- The iris.data file which contains the raw Iris data, this is imported in my code.
- The project.ipynb Jupyter Notebook which provides a brief written summary of the outputs of my code.
- The analysis.py file which contains my code, used to analyse the dataset. All other files are products of that analysis:
- Summaries of the variables saved as a text file (summary.txt).
- Data Visualisations. These include histograms (histograms_of_iris_variables.png) and a pairplot of each pair of variables (pairplots.png).
- There is also some additional analysis into the correlation coefficients of each pair of variables saved as a text file (correlation_coefficient.txt).

## About the Iris Dataset
The Iris Dataset is taken from Ronald Fisher's 1936 paper *The Use of Multiple Measurements in Taxonomic Problems*. The study is an example of taxonomy, or the classification of living things. In the paper, Fisher outlines the physical attributes of 150 flowers, comprised of three related Iris species (fifty instances of each).

The three speces of Iris studied in Fisher's dataset are:

- *Iris Setosa*
- *Iris Virginica*
- *Iris Versicolor*

These species are broken down by the following attributes:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

All of the Irises were picked in the Gaspé Peninsula (near Quebec City, Canada) under the same conditions (on the same day, by the same person).

## What Makes This Particular Dataset so Special?
Aside from being published by an already established and successful statistician, this dataset is renowned across multiple scientific and computing fields in it's own right for a number of reasons.

The Iris dataset is readily accessible for beginners; it has an easily contextualised subject matter (flowers) and examines those flowers in relatively few variables, using the same unit of meaurement for each (centimetres). Further, the data is evenly spread amongst three species (fifty instances of each), with no missing data- this means it doesn't require tidying before analysis and each of the three species of flower can be compared to one another using the same count of instances, with enough data to carry out in-depth analysis but not too much to become inaccessible.

Although the dats is relatively straight forward, scientists and data analysists can use it to test and utilise a wide range of statistical analysis and machine learning techniques. Judging from a quick review of the literature surounding the dataset, this analysis can range from those dipping their toes into coding, statistics and data analysis to those blazing the trail. With such a wide range of applications and given it's popularity, the Iris dataset has become a benchmark dataset to test data analytics, statistics and machine learning techniques.

## Get Started
I used [Anaconda](https://www.anaconda.com/download) in [Visual Studio Code](https://code.visualstudio.com/download) to create and write this project and recommend you download and use the same to view the work.

Anaconda will pre-install Python along with the libraries used within this notebook. Visual Studio Code is a tool which allows the user to view and edit code.

Try out the analysis.py code which saves my outputs by typing 'python analysis.py' as a command line argument.

## References
| Author | Title | About |
| :---   | :---: | :---: |
| Fisher, Ronald | "The Use of Multiple Measurements in Taxonomic Problems", Annals of Eugenics, 7(2): 179–188 | Fishers original paper. The dataset is available [here](https://archive.ics.uci.edu/dataset/53/iris). |
| GitHub Docs | [*Basic writing and formatting syntax: Create sophisticated formatting for your prose and code on GitHub with simple syntax*](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) | Useful guide for basic markdown; stylising text, making lists, adding images, etc. |
| Laerd Statistics | [*Pearson's product moment correlation: Statistical tutorials and software guides*](https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php) | Outlines what Pearson's Correlation Coefficient is as is not. Highlightes 7 assumptions that the variables must meet to be appropriate for testing using the Pearson's correlation- I didn't get into this. Still, a very approachable guide. |
| Pandas Documentation | [*10 Minutes to Pandas Guide*](https://pandas.pydata.org/docs/user_guide/10min.html) | Importing pandas, using it to import the dataset, etc. |
| Seaborn | [*seaborn.kdeplot*](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) | Kernal density estimations with seaborn, explanations and guides. |
| Seaborn | [*seaborn.pairplot*](https://seaborn.pydata.org/generated/seaborn.pairplot.html) | Pairplots with seaborn, how to edit the various parameters of the plot |
| Solomon, Brad. Real Python | [*Python Plotting with Matplotlib (Guide)*](https://realpython.com/python-matplotlib-guide/) | Lots of useful information on plotting, additional resources are available at the end of the article. |
| NumPy User Guide | [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) | Installing NumPy and working with numerical data in Python |
| Pandas Documentation | [*10 Minutes to Pandas Guide*](https://pandas.pydata.org/docs/user_guide/10min.html) | How to create arrays with Panda's, like most of the articles referenced here- this one includes info for both beginners and those with a little more experience. Pick and choose what you need from it. |
| Stack Overflow | [*Stack Overflow*](https://stackoverflow.com/) | Used for finding similar issues and their solutions. As the Iris dataset is so widespread, there are plenty of threads discussing how to analyse it such as [*this*](https://stackoverflow.com/questions/67300148/best-fit-to-a-histogramplot-iris) one I read about plotting the histograms. |
| Van Gogh, Vincent | [*Ireses*](https://commons.wikimedia.org/wiki/File:VanGoghIrises2.jpg) | Cover image for README souced from Wikimedia Commons. Vincent Van Gogh's 1889 painting *Ireses*. |
| W3 Schools | [*Python For Loops*](https://www.w3schools.com/python/python_for_loops.asp) | I used loops to simplify the process of creating the histograms. |
| W3 Schools | [*Python String join() Method*](https://www.w3schools.com/python/ref_string_join.asp) | joining items in an iterable as strings with seperators. |
| W3 Schools | [*Matplotlib Tutorials*](https://www.w3schools.com/python/matplotlib_intro.asp) | Another useful one for plotting. I used this to see how I could enhance my plots visually by adding titles, legends, etc. |
| W3 Schools | [*Python Data Types*](https://www.w3schools.com/python/python_datatypes.asp) | Contains lots of helpful information on the various types of data within Python. |
| Wikipedia | [*Kernal Density Estimation*](https://en.wikipedia.org/wiki/Kernel_density_estimation) | Wikipedia article on kernal density estimations. |
| Zhane, Jaya. RealPython | Writing Comments in Python (Guide) | I used this guide to inform how I commented within my python code (with the aim of keeping comments uniform stylistically). |

## Author
*Paul Cahill*

## Contact
Please feel free to reach out to me at G00438905@atu.ie with any questions, comments or fan mail.