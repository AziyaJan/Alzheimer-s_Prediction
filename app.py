# app.py
from pathlib import Path
import pickle

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model artifact (model + feature order)
MODEL_PATH = Path('models/model.pkl')
if not MODEL_PATH.exists():
    raise FileNotFoundError("Run model.py first to create models/model.pkl")

with open(MODEL_PATH, 'rb') as f:
    artifact = pickle.load(f)

model = artifact['model']
feature_order = artifact['feature_order']

# Expected dtypes for each feature (based on dataset schema)
FEATURE_DTYPES = {
    'Age': int,
    'Gender': int,
    'Ethnicity': int,
    'EducationLevel': int,
    'BMI': float,
    'Smoking': int,
    'AlcoholConsumption': float,
    'PhysicalActivity': float,
    'DietQuality': float,
    'SleepQuality': float,
    'FamilyHistoryAlzheimers': int,
    'CardiovascularDisease': int,
    'Diabetes': int,
    'Depression': int,
    'HeadInjury': int,
    'Hypertension': int,
    'SystolicBP': int,
    'DiastolicBP': int,
    'CholesterolTotal': float,
    'CholesterolLDL': float,
    'CholesterolHDL': float,
    'CholesterolTriglycerides': float,
    'MMSE': float,
    'FunctionalAssessment': float,
    'MemoryComplaints': int,
    'BehavioralProblems': int,
    'ADL': float,
    'Confusion': int,
    'Disorientation': int,
    'PersonalityChanges': int,
    'DifficultyCompletingTasks': int,
    'Forgetfulness': int,
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    user_name = request.form.get('user_name', '') if request.method == 'POST' else ''
    user_email = request.form.get('user_email', '') if request.method == 'POST' else ''
    return render_template('input.html', user_name=user_name, user_email=user_email)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect values
    row = {}
    errors = []

    for col in feature_order:
        raw = request.form.get(col, None)
        if raw is None or raw.strip() == '':
            errors.append(f"Missing value for {col}")
            continue
        caster = FEATURE_DTYPES.get(col, float)
        try:
            row[col] = caster(raw)
        except Exception:
            errors.append(f"Invalid value for {col}: {raw}")

    if errors:
        return render_template(
            'output.html',
            prediction_text='Input error',
            details='; '.join(errors),
            is_error=True
        )

    # Build input DataFrame
    X_in = pd.DataFrame([[row[c] for c in feature_order]], columns=feature_order)

    # Predict
    pred = model.predict(X_in)[0]

    if int(pred) == 1:
        message = "The person is diagnosed with Alzheimer's."
    else:
        message = "The person doesn't have Alzheimer's."

    return render_template(
        'output.html',
        prediction_text=message,
        details=None,
        is_error=False
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
