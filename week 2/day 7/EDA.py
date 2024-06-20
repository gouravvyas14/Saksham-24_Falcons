import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset (built-in dataset in Seaborn)
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(iris.head())

# Basic information about the dataset
print("\nBasic information about the dataset:")
print(iris.info())

# Summary statistics of numerical columns
print("\nSummary statistics of numerical columns:")
print(iris.describe())

print("\nMissing values:")
print(iris.isnull().sum())

# Histograms for each numerical feature
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
sns.histplot(iris['sepal_length'], kde=True, color='skyblue')
plt.subplot(2, 2, 2)
sns.histplot(iris['sepal_width'], kde=True, color='salmon')
plt.subplot(2, 2, 3)
sns.histplot(iris['petal_length'], kde=True, color='green')
plt.subplot(2, 2, 4)
sns.histplot(iris['petal_width'], kde=True, color='orange')
plt.suptitle('Distribution of Numerical Features')
plt.tight_layout()
plt.show()
