import os
import joblib
import numpy as np
import pandas as pd

try:
    BASE_DIR = os.path.dirname(__file__)
except NameError:
    BASE_DIR = os.getcwd()

_ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

_MODEL    = None
_PIPELINE = None


def _load():
    global _MODEL, _PIPELINE
    if _MODEL is None:
        model_path    = os.path.join(_ROOT_DIR, "models", "best_burnout_model.joblib")
        pipeline_path = os.path.join(_ROOT_DIR, "models", "preprocessing_pipeline.joblib")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")
        if not os.path.exists(pipeline_path):
            raise FileNotFoundError(f"Pipeline not found: {pipeline_path}")
        _MODEL    = joblib.load(model_path)
        _PIPELINE = joblib.load(pipeline_path)
    return _MODEL, _PIPELINE


_BADGE_MAP = {
    "Low":    ("success", "Riesgo Bajo"),
    "Medium": ("warning", "Riesgo Moderado"),
    "High":   ("danger",  "Alto Riesgo de Burnout"),
}


def predict_burnout(features_dict: dict) -> dict:
    """
    Preprocesses raw feature dict, runs the XGBoost model and returns a
    template-compatible result: {label, badge, score (0-100)}.
    """
    model, pipeline = _load()

    df    = pd.DataFrame([features_dict])
    X     = pipeline.transform(df)
    proba = model.predict_proba(X)[0]

    classes         = ["Low", "Medium", "High"]
    predicted_class = classes[int(np.argmax(proba))]
    badge, label    = _BADGE_MAP[predicted_class]

    # Weighted risk score 0-100: Low→0, Medium→50, High→100
    score = round(float(proba[0] * 0 + proba[1] * 50 + proba[2] * 100))

    return {"label": label, "badge": badge, "score": score}
