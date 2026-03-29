#import modules
import pandas as pd  # for data / للبيانات
import numpy as np   # for numbers / للأرقام
from sklearn.linear_model import LinearRegression  # for simple model / للنموذج البسيط

#create Sample data
emails = ["free money", "hello friend", "win prize", "meeting today"]
labels = [1, 0, 1, 0]

#Convert Text to Numbers
features = [[email.count("free")] for email in emails]

#Train a Simple Model
model = LinearRegression()
model.fit(features, labels)

#Make Predictions
New_email = "free vacation"
new_feature = [[New_email.count("free")]]

#convert to number
prediction = model.predict(new_feature)
print(prediction)