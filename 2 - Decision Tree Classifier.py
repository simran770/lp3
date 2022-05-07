"""

A dataset collected in a cosmetics shop showing details of customers and whether or
not they responded to a special offer to buy a new lip-stick is shown in table below.
Use this dataset to build a decision tree, with Buys as the target variable, to help in
buying lip-sticks in the future. Find the root node of decision tree. According to the
decision tree you have made from previous training data set, what is the decision for
the test data: [Age < 21, Income = Low, Gender = Female, Marital Status =
Married]?

"""

#import packages
import pydotplus
from sklearn.tree import export_graphviz
from IPython.display import Image
from six import StringIO
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# reading Dataset
dataset = pd.read_csv("./data/cosmetics.csv")
X = dataset.iloc[:, :-1]
# print(X)
y = dataset.iloc[:, 5].values
# print(y)

# Perform Label encoding
labelencoder_X = LabelEncoder()
X = X.apply(LabelEncoder().fit_transform)
print("Label Encoded Data: ")
# print(X)

# Decision Tree Classifier
regressor = DecisionTreeClassifier()
regressor.fit(X.iloc[:, 1:5], y)

# Predict value for the given expression
X_in = np.array([1, 1, 0, 0])
y_pred = regressor.predict([X_in])
print("\nPrediction:", y_pred)
dot_data = StringIO()
export_graphviz(regressor, out_file=dot_data, filled=True,
                rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
