import os
import joblib
import pandas as pd
import numpy as np

try:
    BASE_DIR = os.path.dirname(__file__)
except NameError:
    BASE_DIR = os.getcwd()

DEFAULT_MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "./models/best_burnout_model.joblib")
)

def predict_burnout(features_dict, model_path=DEFAULT_MODEL_PATH):
    """
    Loads the trained raw model and extracts custom metadata from its internal attributes.
    Outputs the highest class probability as a float and the category as a string badge.

    Parameters:
    -----------
    features_dict : dict
        Raw key-value pairs representing features from the client request.
    model_path : str, optional
        The file path to the saved .joblib model binary.

    Returns:
    --------
    dict
        A structured dictionary containing {"score": float, "badge": str}
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No trained model found at: {model_path}")

    # Load the raw machine learning model from disk
    model = joblib.load(model_path)

    # Extract target class metadata from the internal XGBoost Booster
    try:
        classes_attr = model.get_booster().get_attr("target_classes")
        classes = classes_attr.split(",") if classes_attr else ['Low', 'Medium', 'High']
    except AttributeError:
        # Fallback list if the loaded model doesn't have an underlying booster
        classes = ['Low', 'Medium', 'High']

    # Convert the single input dictionary into a 2D pandas DataFrame for inference
    df_features = pd.DataFrame([features_dict])

    # Generate predictive probabilities for all targeted classes
    probabilities = model.predict_proba(df_features)[0]

    # Identify the index pointing to the maximum confidence score
    highest_prob_index = np.argmax(probabilities)

    # Parse the structural score value and class labels dynamically
    score = float(probabilities[highest_prob_index])
    predicted_class = str(classes[highest_prob_index])

    # Map the parsed metadata dynamically to a badge string
    badge = f"{predicted_class} Burnout Risk"

    return {
        "score": round(score, 4),
        "badge": badge
    }
