import pickle
from pathlib import Path


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# === Load data ===
DATA_PATH = Path('alzheimers_disease_data.csv')
if not DATA_PATH.exists():
 raise FileNotFoundError("Make sure 'alzheimers_disease_data.csv' is present in the project root.")


alzheimers_data = pd.read_csv(DATA_PATH)


# === Split features/target ===
# Your snippet had axis=0 in drop; columns should be dropped along axis=1.
X = alzheimers_data.drop(columns=['Diagnosis', 'DoctorInCharge', 'PatientID'], axis=1)
Y = alzheimers_data['Diagnosis']


# Persist the exact feature order for serving time
feature_order = list(X.columns)


# === Train/test split ===
X_train, X_test, Y_train, Y_test = train_test_split(
X, Y, test_size=0.1, stratify=Y, random_state=1
)


# === Model ===
logreg = LogisticRegression(max_iter=1000, n_jobs=None)
logreg.fit(X_train, Y_train)


# Optional quick sanity check
print('Train accuracy:', logreg.score(X_train, Y_train))
print('Test accuracy:', logreg.score(X_test, Y_test))


# === Save with pickle ===
models_dir = Path('models')
models_dir.mkdir(parents=True, exist_ok=True)
MODEL_PATH = models_dir / 'model.pkl'


artifact = {
'model': logreg,
'feature_order': feature_order,
}


with open(MODEL_PATH, 'wb') as f:
 pickle.dump(artifact, f)


print(f"Saved model to {MODEL_PATH.resolve()}")