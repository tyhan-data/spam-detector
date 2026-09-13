from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models" / "Spam_detector.joblib"
CV_DIR = BASE_DIR / "models" / "Count_Vectorizer.joblib"


_model = None
_vectorizer = None


def load_model():
    global _model, _vectorizer

    if _model is None:
        _model = joblib.load(MODEL_DIR)

    if _vectorizer is None:
        _vectorizer = joblib.load(CV_DIR)


def model_prediction(payload: dict):

    # Get text
    text = payload["Text"]

    # Convert text into vector
    data = _vectorizer.transform([text])

    # Prediction
    prediction = _model.predict(data)[0]

    # probability
    probabilities = _model.predict_proba(data)[0]
    
    max_idx = probabilities.argmax()

    probability = probabilities[max_idx]
        
        
    return {
        "Target": prediction,
        "Probability": float(probability)
    }