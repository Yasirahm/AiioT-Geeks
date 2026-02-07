
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
import numpy as np


X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([20, 30, 40, 50, 60])

linear_model = LinearRegression()
linear_model.fit(X, y)

print("Linear Regression Prediction for 6 years:")
print(linear_model.predict([[6]]))

ridge_model = Ridge(alpha=1.0)   # alpha controls penalty
ridge_model.fit(X, y)

print("\nRidge Regression Prediction for 6 years:")
print(ridge_model.predict([[6]]))


lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X, y)

print("\nLasso Regression Prediction for 6 years:")
print(lasso_model.predict([[6]]))

tree_model = DecisionTreeRegressor()
tree_model.fit(X, y)

print("\nDecision Tree Regression Prediction for 6 years:")
print(tree_model.predict([[6]]))
