# -*- coding: utf-8 -*-
"""customer Churn Analysis.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1toXoQd42Y7rBPRyntCoirft-n-Bwomfv

# customer Churn Analysis

# import Datasets
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/Customer Churn.csv')
df.head()

df.tail()

df.shape #checking shape of data

df.columns # columns in datasets

df.info() #checking Datatypes information

df.describe() # basic statistics

df.isnull().sum() #checking null values

df.duplicated().sum() #checking deplicad values in datasets

df.head()

df.hist(figsize=(10, 8))
plt.show()

print(df['gender'].value_counts())
sns.countplot(x='gender', data=df)

sns.boxplot(data=df, x='MonthlyCharges') # checking outliers

"""# groupby"""

df.groupby('gender')['MonthlyCharges'].describe()

df.groupby('gender')['MonthlyCharges'].describe().plot(kind='bar')

df.groupby('gender')[['MonthlyCharges','TotalCharges']].describe()

df.groupby('gender')[['MonthlyCharges','TotalCharges']].describe().plot(kind='bar')

df.head()

df.pivot_table(index='gender', values='MonthlyCharges',columns='SeniorCitizen', aggfunc='mean')

sns.heatmap(df.pivot_table(index='gender', values='MonthlyCharges',columns='SeniorCitizen', aggfunc='mean'))

"""# EDA"""

# Separate numerical and categorical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns

print("Numerical columns:", numerical_columns)
print("Categorical columns:", categorical_columns)

print(df['gender'].dtype)

# Convert 'gender' column to categorical type
df['gender'] = df['gender'].astype('category')
print(df['gender'].dtype)

print(df['gender'].value_counts())

sns.countplot(x='gender', data=df)
plt.show()

df['gender'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()

# summary of Statistics

print(df['MonthlyCharges'].describe())

#Distribution Visualization:

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['MonthlyCharges'], kde=True)
plt.show()

#Box Plot
sns.boxplot(x=df['MonthlyCharges'])
plt.show()

#Detecting Skewness:

print(df['MonthlyCharges'].skew())



print(df['MonthlyCharges'].isnull().sum())

"""# Bia Variate Analysis"""

import seaborn as sns
import matplotlib.pyplot as plt
#Scatter Plot: Visualize the relationship
sns.scatterplot(x='MonthlyCharges', y='TotalCharges', data=df)
plt.show()



print(df['MonthlyCharges'].dtype)

df['MonthlyCharges'] = df['MonthlyCharges'].astype('int')
print(df['MonthlyCharges'].dtype)

print(df['TotalCharges'].dtype)

print(df['TotalCharges'].dtype)

# Inspect the column to identify problematic values
print(df['TotalCharges'].head())  # View the first few rows
print(df['TotalCharges'].unique())  # Check unique values

# Convert to numeric, handle errors, and fill missing values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')  # Convert to numeric, NaN for errors
df['TotalCharges'] = df['TotalCharges'].fillna(0).astype('int')  # Replace NaN with 0 and cast to int

# Verify the conversion
print(df['TotalCharges'].dtype)

#Correlation Coefficient: Measure the strength and direction of the relationship.

correlation = df[['MonthlyCharges', 'TotalCharges']].corr()
print(correlation)

#Line plot
sns.lineplot(x='MonthlyCharges', y='TotalCharges', data=df)
plt.show()

#Key Insights: Distribution of numerical values within categories, differences in means, and variance.
sns.boxplot(x='gender', y='MonthlyCharges', data=df)
plt.show()

#violinplot
sns.violinplot(x='gender', y='MonthlyCharges', data=df)
plt.show()

#Bar Plot
sns.barplot(x='gender', y='MonthlyCharges', data=df, ci=None)
plt.show()

#Group Statistics
print(df.groupby('gender')['MonthlyCharges'].mean())
print(df.groupby('gender')['MonthlyCharges'].median())

#Key Insights: Frequency and proportion of combinations, dependency between variables.
contingency_table = pd.crosstab(df['gender'], df['PaymentMethod'])
print(contingency_table)

#Stacked Bar Plot: Visualize category combinations
contingency_table.plot(kind='bar', stacked=True)
plt.show()

#heatmap
sns.heatmap(contingency_table, annot=True, cmap='coolwarm', fmt='d')
plt.show()

#Chi-Square Test: Check for independence between two categorical variables
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2}, p-value: {p}")

