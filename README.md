# 🧠 Alzheimer's Prediction – Flask Deployment

This project demonstrates an end-to-end **Machine Learning deployment** using **Flask (backend)** and **HTML (frontend)**.  
It trains a Logistic Regression model on an Alzheimer's dataset, saves it using `pickle`, and serves predictions through a simple web app.

---

## 📁 Project Structure

```
alzheimers-flask-app/
├── app.py                    # Flask backend
├── model.py                  # Train & save model (pickle)
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation (this file)
├── models/
│   └── model.pkl            # Saved model + column order
├── templates/
│   ├── welcome.html         # Page 1: user info
│   ├── input.html           # Page 2: input features
│   └── output.html          # Page 3: prediction result
└── static/
    └── style.css            # Optional styles
```

> **Note:** Place your dataset file `alzheimers_disease_data.csv` in the project root before running `model.py`.

---

## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone <repo_url>
   cd alzheimers-flask-app
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## 📊 Train & Save the Model

**Run:**
```bash
python model.py
```

This will:
- Load `alzheimers_disease_data.csv`
- Train a Logistic Regression model
- Save the trained model (and feature order) to `models/model.pkl`

---

## 🚀 Run the Web App

**Start Flask:**
```bash
python app.py
```

The app will run on:
👉 **http://localhost:5000**

---

## 🖥️ Application Flow

1. **`/` → welcome.html**
   - Enter basic user info (name/email).

2. **`/input` → input.html**
   - Enter all clinical & lifestyle features.
   - **Dropdowns:** Gender, Smoking, Diabetes, Depression
   - **Numeric inputs:** All other features.

3. **`/predict` → output.html**
   - Shows the prediction result:
     - If prediction == 1: ✅ **The person is diagnosed with Alzheimer's**
     - Else: ❌ **The person doesn't have Alzheimer's**

---

## 📦 Requirements

- **Python 3.9+** recommended
- Flask
- pandas
- numpy
- scikit-learn

*(Already listed in requirements.txt)*

---

## 🔧 Key Features

### Model Training (`model.py`)
- **Data preprocessing:** Handles missing values, excludes non-predictive columns
- **Feature scaling:** Uses StandardScaler for better model performance
- **Model evaluation:** Provides accuracy, classification report, and confusion matrix
- **Persistence:** Saves both model and feature columns using pickle

### Flask Backend (`app.py`)
- **Session management:** Stores user information across pages
- **Error handling:** Comprehensive error handling for predictions
- **Model integration:** Seamlessly loads and uses the trained model
- **Feature processing:** Handles both numeric and categorical inputs

### Frontend Templates
- **Responsive design:** Modern, mobile-friendly interface
- **Progressive flow:** Step-by-step user experience
- **Input validation:** Client-side and server-side validation
- **Professional styling:** Clean, medical-themed design

---

## 📊 Model Details

### Features Used
- **Demographic:** Age, Gender, Education Level, Ethnicity
- **Lifestyle:** BMI, Alcohol Consumption, Smoking, Physical Activity
- **Medical History:** Family History, Cardiovascular Disease, Diabetes, Depression
- **Clinical Measurements:** Blood pressure, Cholesterol levels, MMSE scores
- **Functional Assessments:** ADL, Memory Complaints, Behavioral Problems

### Model Performance
- **Algorithm:** Logistic Regression with StandardScaler
- **Evaluation:** Stratified train-test split (80/20)
- **Metrics:** Accuracy, Precision, Recall, F1-Score
- **Output:** Binary classification (0: No Alzheimer's, 1: Alzheimer's)

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome page with user information form |
| `/input` | GET/POST | Clinical features input form |
| `/predict` | POST | Make prediction and show results |
| `/reset` | GET | Clear session and restart |

---

## 📝 Usage Notes

1. **Dataset Requirements:**
   - The dataset columns `DoctorInCharge` and `PatientID` are excluded from training
   - Target column should be named `Diagnosis`

2. **Predictions:**
   - **Binary output:** 0/1
     - `1` → Alzheimer's diagnosed
     - `0` → No Alzheimer's
   - **Confidence scores:** Probability estimates for both classes

3. **Customization:**
   - Update dropdown labels in `input.html` if your dataset uses specific encodings
   - Modify feature lists in `app.py` to match your dataset structure
   - Adjust model parameters in `model.py` for better performance

---

## 🚨 Important Disclaimers

- **Educational Purpose Only:** This tool is designed for educational and demonstration purposes
- **Not Medical Advice:** Results should not be used for actual medical diagnosis
- **Consult Professionals:** Always consult qualified healthcare professionals for medical concerns
- **Data Privacy:** Ensure compliance with healthcare data regulations in production use

---

## 🔄 Development Workflow

1. **Prepare your dataset** and place it in the project root
2. **Train the model** using `python model.py`
3. **Start the Flask app** with `python app.py`
4. **Access the application** at `http://localhost:5000`
5. **Test the prediction flow** with sample data

---

## 🛠️ Troubleshooting

### Common Issues:

**Model not found error:**
```bash
# Solution: Train the model first
python model.py
```

**Missing dataset:**
```bash
# Ensure alzheimers_disease_data.csv is in project root
ls alzheimers_disease_data.csv
```

**Port already in use:**
```bash
# Change port in app.py or kill existing process
lsof -ti:5000 | xargs kill -9
```

---

## 📈 Future Enhancements

- **Multiple algorithms:** Compare Random Forest, SVM, Neural Networks
- **Feature importance:** Visualize which factors contribute most to predictions
- **Data visualization:** Add charts and graphs for better insights
- **Export functionality:** Generate PDF reports of predictions
- **Database integration:** Store predictions and user data
- **REST API:** Create API endpoints for external integrations

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Scikit-learn** for machine learning algorithms
- **Flask** for web framework
- **Bootstrap** for responsive design components
- **Medical community** for Alzheimer's research insights
