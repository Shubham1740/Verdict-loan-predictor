from flask import Flask, render_template, request
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))


# Initialize Flask app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        dep = request.form["Dependents"]
        prop = request.form["Property_Area"]

        # One-hot encode Dependents
        dep_0 = 1 if dep == "0" else 0
        dep_1 = 1 if dep == "1" else 0
        dep_2 = 1 if dep == "2" else 0
        dep_3 = 1 if dep == "3+" else 0

        # One-hot encode Property_Area
        prop_rural = 1 if prop == "Property_Area_Rural" else 0
        prop_semiurban = 1 if prop == "Property_Area_Semiurban" else 0
        prop_urban = 1 if prop == "Property_Area_Urban" else 0

        features = [
            int(request.form["Gender"]),
            int(request.form["Married"]),
            int(request.form["Education"]),
            int(request.form["Self_Employed"]),
            float(request.form["ApplicantIncome"]),
            float(request.form["CoapplicantIncome"]),
            float(request.form["LoanAmount"]),
            float(request.form["Loan_Amount_Term"]),
            float(request.form["Credit_History"]),
            prop_rural,
            prop_semiurban,
            prop_urban,
            dep_0,
            dep_1,
            dep_2,
            dep_3,
        ]

        arr = np.array(features).reshape(1, -1)
        prediction = model.predict(arr)[0]
        probability = model.predict_proba(arr)[0][1]

        if prediction == 1:
            result = f"✅ Loan Approved (Probability: {probability:.2%})"
        else:
            result = f"❌ Loan Not Approved (Probability: {1 - probability:.2%})"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
