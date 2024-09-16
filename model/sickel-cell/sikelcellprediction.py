import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


def sklcell_prediction(inputs):
    if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 1 and inputs[5] == 0):
        return '100%  Children are Carriers'
    else:
        if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 1):
            return '100%  Children are Carriers'
        else:
            if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 1 and inputs[5] == 1):
                return '100%  Children are Affected'
            else:
                if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 1 and inputs[4] == 0 and inputs[5] == 0):
                    return '50%  Chance of Unaffected Children and 50%  Chance have Carrier Children'
                else:
                    if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                        return '50%  Chance of Unaffected Children and 50%  Chance have Carrier Children'
                    else:
                        if (inputs[0] == 0 and inputs[1] == 1 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                            return '50%  Chance of Unaffected Children and 50%  Chance have Carrier Children'
                        else:
                            if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                                return '50%  Chance of Unaffected Children and 50%  Chance have Carrier Children'
                            else:
                                if (inputs[0] == 0 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 1 and inputs[4] == 0 and inputs[5] == 1):
                                    return '100%  Chance of Carrier Children'
                                else:
                                    if (inputs[0] == 1 and inputs[1] == 1 and inputs[2] == 0 and inputs[3] == 0 and inputs[4] == 1 and inputs[5] == 0):
                                        return '100%  Chance of Carrier Children'
                                    else:
                                        if (inputs[0] == 1 and inputs[1] == 0 and inputs[2] == 1 and inputs[3] == 0 and inputs[4] == 0 and inputs[5] == 0):
                                            return '25%  Chance of Unaffected Children & 50%  Chance of Carrier Children & 25%  Chance have Affected Children'
                                        else:
                                            if (inputs[0] == 1 and inputs[1] == 1 and inputs[2] == 1 and inputs[3] == 1 and inputs[4] == 1 and inputs[5] == 1):
                                                return '100%  Affected Children'
                                            else:
                                                return 'Results are Inconclusive'
