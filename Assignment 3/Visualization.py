# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the Iris dataset from seaborn
df = sns.load_dataset('iris')

# 1. EDA - Exploratory Data Analysis

print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nFirst 5 Rows:\n", df.head())
print("\nInfo:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:\n", df.isnull().sum())

print("\nClass Distribution:\n", df['species'].value_counts())


# 2. Data Preprocessing
# Encode the categorical target (species)
le = LabelEncoder()
df['species_encoded'] = le.fit_transform(df['species'])

print("\nAfter Encoding 'species':")
print(df[['species', 'species_encoded']].head())


# 3. Data Visualization
# Set global style
sns.set(style="whitegrid")

# 3.1 Line Plot - Sepal Length for each sample
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal_length'], marker='o', linestyle='-')
plt.title('Line Plot of Sepal Length')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()

# 3.2 Histogram - Petal Width Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['petal_width'], bins=15, color='purple', edgecolor='black')
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 3.3 Pie Chart - Species Distribution
species_counts = df['species'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Species Distribution in Iris Dataset')
plt.axis('equal')
plt.show()

# 3.4 Box and Whiskers Plot - Sepal Width per Species
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='sepal_width', data=df, palette='Set2')
plt.title('Box Plot of Sepal Width by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.show()
