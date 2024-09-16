import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def diabetes_prediction(inputs):
    diabetes_dataset = pd.read_csv(
        'https://raw.githubusercontent.com/PulasthiAbey/Datasets/main/Diabetes/diabetesFinalValues.csv')

    X = diabetes_dataset.drop(
        columns=['Affected Values', 'HbA1c', 'Height', 'Weight', 'Duration of disease'])
    Y = diabetes_dataset['Affected Values']

    scaler = StandardScaler()
    scaler.fit(X)

    standardize_data = scaler.transform(X)

    X = standardize_data
    Y = diabetes_dataset['Affected Values']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, stratify=Y,  random_state=2)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    X_train_prediction = classifier.predict(X_train)
    X_test_prediction = classifier.predict(X_test)

    input_data_as_numpy_array = np.asarray(inputs)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    std_data = scaler.transform(input_data_reshaped)

    prediction = classifier.predict(std_data)

    output = ''

    if (prediction[0] == 0):
      output = 'Congratulations! You are Not Diabetic'
      return output
    else:
        if(prediction[0] == 1):
            output = 'You Have Diabetic, Please Consult A Doctor'
            return output
        else:
            output = 'The Results Are Inconclusive'
            return output
