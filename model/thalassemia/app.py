from flask import Flask, render_template, request
import numpy as np

import thalassemia

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
def home():
    return render_template('predict_diabetes.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        otherDis = 1 if request.form.get("otherDis") == 'on' else 0
        adeqNut = 1 if request.form.get("adeqNut") == 'on' else 0
        autoAnti = 1 if request.form.get("autoAnti") == 'on' else 0
        gluMeta = 1 if request.form.get("gluMeta") == 'on' else 0
        tookInsulin = 1 if request.form.get("tookInsulin") == 'on' else 0
        type1 = 1 if request.form.get("type1") == 'on' else 0

        inputs = [autoAnti, gluMeta, tookInsulin, type1, otherDis, adeqNut]

        
        prediction = thalassemia.thalassemia_prediction(inputs)


    return render_template('predict.html', predict=prediction)


if __name__ == '__main__':
    app.run(host="localhost", port=7770, debug=True)
