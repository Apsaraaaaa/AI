from sklearn.preprocessing import LabelEncoder
data=['red','blue','red','blue',]
le=LabelEncoder()
encoded=le.fit_transform(data)
print(encoded)