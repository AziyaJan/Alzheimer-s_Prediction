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


# Simple helper to coerce request.form values to correct types
# Declare expected dtype for each feature (based on your schema)
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


app.run(host='0.0.0.0', port=5000, debug=True)