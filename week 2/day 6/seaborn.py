import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
np.random.seed(0)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Creating a scatter plot with regression line using Seaborn
sns.regplot(x=x, y=y, color='blue', scatter_kws={'s': 20})  # scatter_kws adjusts marker size
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Linear Regression Line')
plt.grid(True)
plt.show()


# Creating a pairplot to explore relationships between variables
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
plt.suptitle('Pairplot of Iris Dataset')
plt.show()

# Creating a boxplot to visualize distribution of 'total_bill' by 'day'
tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=tips, palette='Set2')
plt.title('Boxplot of Total Bill by Day')
plt.show()
