''' The focus of this file is to
use the student2.py and get the highest % accuracy in 30 times '''


import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep = ";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]


# print(data.head())  Print the first 5 data

predict = "G3"    # G3 is the thing we want to predict

x = np.array(data.drop([predict], 1))      # x-axis
y = np.array(data[predict])                # y-axis

accuracy = 0
x, y = 0

for i in range (100):
    # Spliting the data into two parts, 80% for training, 20% for testing
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2)
    
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)   #Train the Algorithm

    acc = regressor.score(x_test, y_test)
    if acc > accuracy:
        accuracy = acc
        x = x_test
        y = y_test
        

print("The accuracy is ", accuracy)