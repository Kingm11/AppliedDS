# Creating pipline using Pycaret3
## Overview

1. ### The pipeline uses Pycaret3 to create a machine learning model to predict the species of an iris flower based on its characteristics.

2. ### The pipeline loads the iris dataset from Pycaret3's built-in datasets and sets the target variable as 'species'.

3. ### The pipeline uses Pycaret3's setup() function to preprocess the data and set up the machine learning pipeline.

4. ### The pipeline creates a Random Forest model using Pycaret3's create_model() function.

5. ### The pipeline evaluates the model using Pycaret3's plot_model() function to visualize the confusion matrix.

6. ### The pipeline deploys the model using Pycaret3's deploy_model() function, making it available for predictions through an API endpoint.

## Scope 

1. ### The scope of this pipeline is to demonstrate how Pycaret3 can be used to build an end-to-end machine learning pipeline with minimal coding effort.
2. ### Pycaret3 automates the machine learning pipeline, making it easier and faster to build and deploy machine learning models.
3. ### Pycaret3 can be used for a wide range of machine learning tasks, including classification, regression, clustering, and anomaly detection.
4. ### This pipeline demonstrates how easy and fast it is to create a machine learning model using Pycaret3. By automating the end-to-end machine learning process, Pycaret3 enables data scientists and machine learning practitioners to focus on high-level tasks such as feature engineering, hyperparameter tuning, and model selection.


## Data

### For this Project, we will use the classic Iris dataset, which contains information about the physical characteristics of different types of iris flowers.

### We loaded the Iris dataset from Scikit-learn and convert it into a Pandas DataFrame.
https://archive.ics.uci.edu/ml/datasets/iris
## Visualization
### I created several visualizations using Seaborn and Matplotlib, including a histogram of the sepal length by class, a scatterplot of the sepal length and petal length colored by class

![image](https://user-images.githubusercontent.com/122539722/231402756-eabd6b59-e028-4e56-842a-c715736ba698.png)


![image](https://user-images.githubusercontent.com/122539722/231403198-173a3015-5efa-4207-bf0a-6ea159561f3d.png)

## Technologies Used
 
  .Matlotlib
  
  .Seaborn
## Steps
### 1.I define a function called data_analysis

This function takes a pandas dataframe as input and performs the following operations:

. Checks for missing values using Pandas isnull function data_analysis.py , and drops them using dropna function if there are any.

. Checks for duplicate rows using Pandas duplicated function, and drops them using drop_duplicates function if there are any.

. Calculates the mean, mode, median, and standard deviation using Pandas mean, mode, median, and std functions, respectively.

. Prints the calculated statistics.

. Returns the cleaned dataframe.

### 2.Then i used read_csv function from Pandas to load it into a DataFrame

### 3.Then I called the data_analysis function to perform some data cleaning and analysis

### 4.Then i created  some visualizations using Matplotlib and Seaborn
