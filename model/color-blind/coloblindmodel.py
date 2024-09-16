import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def colorblind_prediction(inputs):
    if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 1 and inputs[5] == 0):
        return 'Daughter in your family is a colorblind carrier'
    else:
        if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 1):
            return 'Daughter in your family is a colorblind carrier'
        else:
            if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 1 and inputs[5] == 1):
                return 'Sons and Daughters are colorblind'
            else:
                if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                    return 'No Risk of Colorblindness'
                else:
                    if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 1 and inputs[4] == 1 and inputs[5] == 0):
                        return 'Daughter in your family is a colorblind carrier'
                    else:
                        if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 1):
                            return 'Son has 50%  Chance of colorblindness (Daughter has a 50%  being a carrier)'
                        else:
                            if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                                return 'Son has 50%  Chance of colorblindness (Daughter has a 50%  being a carrier)'
                            else:
                                if (inputs[0] == 0 and inputs[1] == 1 and inputs[2] == 0 and inputs[3] == 1 and inputs[4] == 1 and inputs[5] == 0):
                                    return 'Son & Daughter has 50%  Chance of colorblindness (Daughter has a 50%  Chance being a carrier)'
                                else:
                                    if (inputs[0] == 0 and inputs[1] == 1 and inputs[2] == 0 and inputs[3] == 1 and inputs[4] == 1 and inputs[5] == 1):
                                        return 'Son & Daughter has 50%  Chance of colorblindness (Daughter has a 50%  Chance being a carrier)'
                                    else:
                                        if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 1 and inputs[4] == 0 and inputs[5] == 1):
                                            return 'Son & Daughter has 50%  Chance of colorblindness (Daughter has a 50%  Chance being a carrier)'
                                        else:
                                            if (inputs[0] == 1 and inputs[1] == 1 and inputs[2] == 1 and inputs[3] == 1 and inputs[4] == 1 and inputs[5] == 1):
                                                return 'Son & Daughter has colorblindness'
                                            else:
                                                return 'Results are Inconclusive'
