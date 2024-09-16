import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def heart_prediction(input_data):
    heart_dataset = pd.read_csv(
        'https://raw.githubusercontent.com/PulasthiAbey/Datasets/main/heartdiseace/heart.csv')

    X = heart_dataset.drop(columns='target', axis=1)
    Y = heart_dataset['target']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    if (prediction[0] == 0):
      return 'Congratulations! You Don\'t Have Heart Disease'
    else:
        return 'You Have Heart Disease'
