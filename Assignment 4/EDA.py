# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset and change path according to your System
df = pd.read_csv("E:/Internships & Certificates/Celebal/Celebal/Assignment 4/heart.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df.describe())

# Preview first few records
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Data Distribution: Histograms for all numerical features
df.hist(bins=20, figsize=(14, 10), color='skyblue', edgecolor='black')
plt.suptitle("Distribution of Numerical Features", fontsize=16)
plt.tight_layout()
plt.show()

# Outlier Detection: Boxplots for continuous variables
plt.figure(figsize=(15, 6))
numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
for i, col in enumerate(numeric_features):
    plt.subplot(2, 5, i+1)
    sns.boxplot(y=df[col], color='lightgreen')
    plt.title(col)
plt.tight_layout()
plt.show()

# Correlation Matrix and Heatmap (Fix: restrict to numeric columns only)
plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=['int64', 'float64'])  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Encode Categorical Features
df_encoded = df.copy()
categorical_cols = df_encoded.select_dtypes(include=['object']).columns.tolist()
encoder = LabelEncoder()

for col in categorical_cols:
    df_encoded[col] = encoder.fit_transform(df_encoded[col])

# Feature Scaling for numeric variables
scaler = StandardScaler()
scaled_features = df_encoded.copy()
scaled_columns = scaled_features.drop('HeartDisease', axis=1).columns

scaled_features[scaled_columns] = scaler.fit_transform(scaled_features[scaled_columns])

# Preview the processed data
print("\nEncoded and Scaled Dataset Sample:")
print(scaled_features.head())

# Pairplot to explore relationships
sns.pairplot(df_encoded[['Age', 'Cholesterol', 'MaxHR', 'Oldpeak', 'HeartDisease']],
             hue='HeartDisease', palette='Set2')
plt.suptitle("Pairwise Relationships", y=1.02)
plt.show()
