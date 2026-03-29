from sklearn.cluster import KMeans
import numpy as np

# Customer data: age and spending / بيانات العملاء: العمر والإنفاق
X = np.array([[25, 200], [30, 220], [50, 600], [55, 580]])

# Cluster into 2 groups / تجميع في مجموعتين
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print(kmeans.labels_)  # show cluster each customer belongs to / إظهار المجموعة لكل عميل