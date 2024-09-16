from flask import Flask, render_template, request

import heart

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route("/")
def home():
    return render_template('predict_diabetes.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        age = int(request.form.getlist("ageOfTheUser")[0])
        gender = 1 if request.form.get("genderMale") == 'on' else 0

        if(gender == 0):
            gender = 1 if request.form.get("genderFemale") == 'on' else 0

        cp = 1 if request.form.get("otherDis") == 'on' else 0
        trestbps = float(request.form.getlist("trestbps")[0])
        chol = float(request.form.getlist("chol")[0])

        if (chol > 200):
            restecg = 1
        else:
            restecg = 0

        thalach = 1 if request.form.get("thalach") == 'on' else 0
        fbs = 1 if request.form.get("fbs") == 'on' else 0
        exang = 1 if request.form.get("exang") == 'on' else 0
        oldpeak = 1 if request.form.get("oldpeak") == 'on' else 0
        ca = 1 if request.form.get("ca") == 'on' else 0
        slope = 1 if request.form.get("slope") == 'on' else 0
        thal = 1 if request.form.get("thal") == 'on' else 0

        if (thal == 0 and slope == 0):
            thal = 2
        else:
            thal = 3

        inputs = (age, gender, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal)
       
        prediction = heart.heart_prediction(inputs)
       

    return render_template('predict.html', predict=prediction)


if __name__ == '__main__':
    app.run(host="localhost", port=8214, debug=True)
