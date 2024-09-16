import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def diabetes_prediction(inputs):
    count = 0

    if (inputs[0] == 1 and inputs[3] == 1):
        count = count + 1
        if (inputs[7] == 1):
            count = count + 1
            return "Child has 52%  Chance of Getting Diabetes"
        return "Child has 0.58%  Chance of Getting Diabetes"
    else:
        count = count + 1
        if (inputs[1] == 1 and inputs[2] == 1):
            count = count + 1
            return "Child has 1%  Chance of Getting Diabetes"
        else:
            count = count + 1
            if (inputs[1] == 1 and inputs[2] == 0):
                count = count + 1
                return "Child has 0.25%  Chance of Getting Diabetes"

    if (inputs[5] == 1):
        if (inputs[6] == 0):
            return "Child has 70%  Chance of Getting Diabetes"
        return "Child has 30%  Chance of Getting Diabetes"
    else:
        if (inputs[6] == 0):
            return "Child has 30%  Chance of Getting Diabetes"

    if (count > 0):
        if (inputs[4] == 1):
            return "Child has Some Risk of Having Diabetes"

        if (inputs[8] == 1):
            return "Child has Some Risk of Having Diabetes"
