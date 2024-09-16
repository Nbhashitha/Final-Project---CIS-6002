# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis"""

# Import dataset to the development environment
diabetes_dataset = pd.read_csv('https://raw.githubusercontent.com/PulasthiAbey/Datasets/main/Diabetes/diabetesFinalValues.csv')

# Checking the dataframes in the dataset
diabetes_dataset.head()

# Number of rows and columns in the dataset
diabetes_dataset.shape

# Getting the Statistical measures of the dataset
diabetes_dataset.describe()

diabetes_dataset['Affected Values'].value_counts()

diabetes_dataset.groupby('Affected Values').mean()

# Seperate the dataset 
X = diabetes_dataset.drop(columns = ['Affected Values','HbA1c', 'Height', 'Weight', 'Duration of disease'])
# print(X)
Y = diabetes_dataset['Affected Values']
# print(Y)

"""

---


# **Data Standarization**"""

scaler = StandardScaler()

scaler.fit(X)

standardize_data = scaler.transform(X)
print(standardize_data)

X = standardize_data
Y = diabetes_dataset['Affected Values']

print(X)
print(Y)

"""---

---


# **Train Test Split**
"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y,  random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""

---


# **Training the Model**"""

classifier = svm.SVC(kernel='linear')

# training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

"""### Model Valuation"""



"""### Accuracy Score"""

# Accuracy score for the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy Score of the Training Data : ', training_data_accuracy)

# Accuracy score for the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy Score of the Test Data : ', test_data_accuracy)

"""# **Making the Prediction**

---


"""

input_data = (24.888889, 0, 0, 1, 1, 1, 1, 0, 1, 1)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
# print(std_data)

prediction = classifier.predict(std_data)
# print('Prediction Value', prediction)

if (prediction[0]==0):
  print('The person is non Diabetic')
else:
  print('This person is diabetic')

input_data = (32, 1, 1, 0, 0, 0, 0, 0, 1, 1)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
# print(std_data)

prediction = classifier.predict(std_data)
# print('Prediction Value', prediction)


if (prediction[0]==0):
  print('The person is non Diabetic')
else:
  print('This person is diabetic')