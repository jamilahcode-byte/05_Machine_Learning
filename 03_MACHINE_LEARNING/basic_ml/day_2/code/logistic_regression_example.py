from sklearn.linear_model import LogisticRegression

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]  # labels / التسميات

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[1.5]]))  # Output = 0