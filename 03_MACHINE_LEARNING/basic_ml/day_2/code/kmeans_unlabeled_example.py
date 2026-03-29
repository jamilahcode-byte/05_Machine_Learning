from sklearn.cluster import KMeans

X = [[1], [2], [10], [11]]  # unlabeled / بدون تسميات

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)  # Output = [0 0 1 1]