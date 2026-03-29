# Emails and labels / الرسائل والتصنيفات
emails = ["win money", "hello", "free prize", "meeting"]
labels = [1, 0, 1, 0]

# Count "free" / عد كلمة "free"
features = [[email.count("free")] for email in emails]

# Train model / تدريب النموذج
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(features, labels)

# Predict / التنبؤ
new_email = "free vacation"
prediction = model.predict([[new_email.count("free")]])
print(prediction)