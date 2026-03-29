from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score

# Regression
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Classification
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)