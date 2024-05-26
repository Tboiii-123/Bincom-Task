import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt




df =pd.read_csv('username.csv',delimiter=';')

#print(df.head())
# Create a new feature from the length of the Username

df['Username_length'] = df['Username'].apply(len)

# Prepare the data for linear regression
X = df[['Username_length']]  # Independent variable
y = df['Identifier']         # Dependent variable

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Output the model's parameters
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

# Plotting the results 
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.xlabel('Username_Length')
plt.ylabel('Identifier')
plt.title('Linear Regression: Identifier vs Username Length')
plt.legend()
plt.show()