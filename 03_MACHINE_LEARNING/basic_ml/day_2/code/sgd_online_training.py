from sklearn.linear_model import SGDRegressor
import numpy as np

# Online training model / نموذج التعلم المستمر
model = SGDRegressor(max_iter=1, learning_rate='constant', eta0=0.1)

# New data arrives sequentially / وصول البيانات الجديدة بشكل متسلسل
for x, y in zip([[1], [2], [3], [4]], [2, 4, 6, 8]):
    model.partial_fit([x], [y])

# Predict / التنبؤ
print(model.predict([[5]]))  # Output close to 10 / الناتج قريب من 10