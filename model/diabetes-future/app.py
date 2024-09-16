from flask import Flask, render_template, request
import numpy as np

import diabetes

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
def home():
    return render_template('predict_diabetes.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        fatherType01 = 1 if request.form.get("otherDis") == 'on' else 0
        motherType01 = 1 if request.form.get("adeqNut") == 'on' else 0
        motherChild = 1 if request.form.get("childBefore") == 'on' else 0
        fatherDiabBefore11 = 1 if request.form.get(
            "diabBefore11") == 'on' else 0
        motherDiabBefore11 = 1 if request.form.get(
            "mDiabBefore11") == 'on' else 0
        fatherType2 = 1 if request.form.get("fatherType2") == 'on' else 0
        motherType2 = 1 if request.form.get("motherType2") == 'on' else 0
        glucoseIssues = 1 if request.form.get("glucoseIssues") == 'on' else 0
        motherGlucoseIssues = 1 if request.form.get(
            "motherGlucoseIssues") == 'on' else 0
        

        inputs = [fatherType01, motherType01, motherChild, fatherDiabBefore11, motherDiabBefore11,
                  fatherType2, motherType2, glucoseIssues, motherGlucoseIssues]

        prediction = diabetes.diabetes_prediction(inputs)

    return render_template('predict.html', predict=prediction)


if __name__ == '__main__':
    app.run(host="localhost", port=4586, debug=True)
