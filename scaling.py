#scaling:it ensures that all the features contribute equally to the distance computations in algorithms like KNN and K-means.
#by bringing them to a common scale,improving the performance and convergence speed of these algorithms.
#for distance-based allgorithms.z=(x-mean)/std
from sklearn.preprocessing import StandardScaler
import numpy as np

X=np.array([[1,2],[3,4],[5,6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print((X_scaled))