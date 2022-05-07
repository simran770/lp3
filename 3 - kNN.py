"""

In the following diagram let blue circles indicate positive examples and orange
squares indicate negative examples. We want to use k-NN algorithm for classifying
the points. If k=3, find the class of the point (6,6). Extend the same example for
Distance-Weighted k-NN and Locally weighted Averaging

"""


# import the packages
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

# Read dataset
dataset = pd.read_csv("./data/kdata.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 2].values

# import KNeighborshood Classifier and create object of it
# Creating model
classifier = KNeighborsClassifier(n_neighbors=3)
# Training model
classifier.fit(X, y)

# predict the class for the point(6,6)
X_test = np.array([6, 6])
# Predictions for test data
y_pred = classifier.predict([X_test])
print('General KNN:', y_pred)

# KNeighborsClassifier looks for the 5 nearest neighbors
# If set to uniform, all points in each neighbourhood have
# equal influence in predicting class i.e. predicted class is the class with highest number of points in the neighbourhood.
classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
classifier.fit(X, y)

# predict the class for the point(6,6)
X_test = np.array([6, 6])
y_pred = classifier.predict([X_test])
print('Distance Weighted KNN:', y_pred)
