# Simple Linear Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define dependent and independent variables
y_simple = tips_df[['tip']]  # Dependent variable (tip amount)
x_simple = tips_df[['total_bill']]  # Independent variable (total bill)

# Split data into training and testing sets
x_train_simple, x_test_simple, y_train_simple, y_test_simple = train_test_split(x_simple, y_simple, test_size=0.3, random_state=42)

# Create a Linear Regression model
lr_simple = LinearRegression()

# Fit the model on the training data
lr_simple.fit(x_train_simple, y_train_simple)

# Predict on the test data
y_pred_simple = lr_simple.predict(x_test_simple)

# Calculate Mean Squared Error
mse_simple = mean_squared_error(y_test_simple, y_pred_simple)
print("Mean Squared Error (Simple Linear Regression):", mse_simple)

# Plotting the regression line
sns.regplot(x='total_bill', y='tip', data=tips_df)
plt.title('Linear Regression Fit: Total Bill vs Tip Amount')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip Amount ($)')
plt.show()
