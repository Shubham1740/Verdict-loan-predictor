# Verdict · Loan Approval Predictor

🔗 **Live demo:** [shubham2140.pythonanywhere.com](https://shubham2140.pythonanywhere.com/)

Verdict is a small Flask web app that predicts whether a loan application is likely to be approved. You fill in an applicant's details, and a pre-trained machine-learning model returns an approved / not approved result along with its confidence.

## Features

- Clean, responsive form split into three steps: applicant details, income, and loan details
- Instant prediction with a confidence percentage and a visual confidence bar
- Form values stay filled in after you submit
- Works on desktop and mobile

## Project Structure

```
.
├── app.py              # Flask app: handles the form and runs the model
├── model.pkl           # Pre-trained model (loaded with pickle)
├── requirements.txt    # Python dependencies
├── README.md
└── templates/
    └── index.html      # The Verdict interface
```

## Getting Started

### Prerequisites

- Python 3.8 or newer

### Installation

1. Clone or download the project and open a terminal in its folder.

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Run the app

```bash
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## How It Works

The form sends the applicant's details to the Flask route in `app.py`, which:

1. One-hot encodes `Dependents` (0, 1, 2, 3+) and `Property_Area` (Rural, Semiurban, Urban).
2. Builds a 16-feature vector in this order:

   | # | Feature |
   |---|---------|
   | 1 | Gender |
   | 2 | Married |
   | 3 | Education |
   | 4 | Self_Employed |
   | 5 | ApplicantIncome |
   | 6 | CoapplicantIncome |
   | 7 | LoanAmount |
   | 8 | Loan_Amount_Term |
   | 9 | Credit_History |
   | 10–12 | Property_Area (Rural, Semiurban, Urban) |
   | 13–16 | Dependents (0, 1, 2, 3+) |

3. Passes the vector to the model and returns the prediction plus its probability.

### Input encoding

The numeric form fields use the following values. They must match the encoding the model was trained with:

| Field | Values |
|-------|--------|
| Gender | Male = 1, Female = 0 |
| Married | Married = 1, Single = 0 |
| Education | Graduate = 1, Not Graduate = 0 |
| Self_Employed | Yes = 1, No = 0 |
| Credit_History | Good = 1.0, Poor = 0.0 |

If your model was trained with a different mapping, update the `value` attributes of the matching `<option>` tags in `templates/index.html`.

## Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn model loaded via pickle, NumPy
- **Frontend:** HTML, CSS, and a little vanilla JavaScript (Jinja2 templating)

## Disclaimer

Verdict is an educational project. Its predictions are statistical estimates from a machine-learning model and are not financial advice or a guarantee of loan approval.