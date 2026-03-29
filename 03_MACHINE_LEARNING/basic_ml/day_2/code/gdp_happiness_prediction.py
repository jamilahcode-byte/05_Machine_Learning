#import modules
import pandas as pd  # for data / للبيانات
import numpy as np   # for numbers / للأرقام
from sklearn.linear_model import LinearRegression  # for simple model / للنموذج البسيط

#create Sample data
# Data: GDP vs Happiness / البيانات: الناتج المحلي الإجمالي مقابل السعادة
GDP = np.array([12240, 27195, 37675, 50962, 55805]).reshape(-1, 1)
Happiness = np.array([4.9, 5.8, 6.5, 7.3, 7.2])
#Convert Text to Numbers
features = [[email.count("free")] for email in emails]

#Train a Simple Model
model = LinearRegression()
model.fit(GDP, Happiness)

#Make Predictions
# Predict Happiness for GDP = 22587 / التنبؤ بالسعادة لناتج محلي 22587
prediction = model.predict([[22587]])
print(prediction)  # output ~5.96