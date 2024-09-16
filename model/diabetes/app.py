from flask import Flask, render_template, request

import diabetes

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
def home():
    return render_template('predict_diabetes.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        age = int(request.form.getlist("ageOfTheUser")[0])
        height = int(request.form.getlist("heightUser")[0])
        bmi = float(request.form.getlist("bmiUser")[0])
        glucose = float(request.form.getlist("glucoseUser")[0])
        bp = int(request.form.get("bloodpUser")[0])

        otherDis = 1 if request.form.get("otherDis") == 'on' else 0
        adeqNut = 1 if request.form.get("adeqNut") == 'on' else 0
        autoAnti = 1 if request.form.get("autoAnti") == 'on' else 0
        gluMeta = 1 if request.form.get("gluMeta") == 'on' else 0
        tookInsulin = 1 if request.form.get("tookInsulin") == 'on' else 0
        type1 = 1 if request.form.get("type1") == 'on' else 0
        type2 = 1 if request.form.get("type2") == 'on' else 0
        hypo = 1 if request.form.get("hypo") == 'on' else 0
        panci = 1 if request.form.get("panci") == 'on' else 0

        inputs = (bmi, otherDis, adeqNut, autoAnti, gluMeta,
                  tookInsulin, type1, type2, hypo, panci)
        prediction = diabetes.diabetes_prediction(inputs)

    return render_template('predict.html', predict=prediction)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
