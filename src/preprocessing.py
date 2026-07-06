
import os
import json
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

pd.set_option("display.max_columns", None)

# ES: Semilla para reproducibilidad. | EN: Seed for reproducibility.
RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
RAW_DATA_PATH = "../data/01_output/burnout_df.csv"
MODELS_DIR = "../models"
PROCESSED_DIR = "../data/processed"
PIPELINE_PATH = os.path.join(MODELS_DIR, "preprocessing_pipeline.joblib")
METADATA_PATH = os.path.join(MODELS_DIR, "preprocessing_metadata.json")
PROCESSED_NPZ_PATH = os.path.join(PROCESSED_DIR, "burnout_processed.npz")

# ---------------------------------------------------------------------------
# Feature definitions (recap of EDA decisions)
# ---------------------------------------------------------------------------
TARGET_COLUMN = "burnout_risk"

# ES: Columnas excluidas del conjunto de predictores.
# EN: Columns excluded from the predictor set.
COLUMNS_TO_DROP = ["user_id", "burnout_score", TARGET_COLUMN]

# ES: Variable categórica. | EN: Categorical feature.
CATEGORICAL_FEATURES = ["day_type"]


def build_feature_lists(df):
    """
    ES: Devuelve (categorical_features, numerical_features) a partir del df.
    EN: Returns (categorical_features, numerical_features) from the df.
    """
    numerical_features = [
        column for column in df.columns
        if column not in COLUMNS_TO_DROP + CATEGORICAL_FEATURES
    ]
    return CATEGORICAL_FEATURES, numerical_features


def build_pipeline(categorical_features, numerical_features):
    """
    ES: Construye el pipeline de preprocesado (OneHot + StandardScaler).
    EN: Builds the preprocessing pipeline (OneHot + StandardScaler).
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore", drop="if_binary"),
             categorical_features),
            ("numerical", StandardScaler(), numerical_features),
        ]
    )
    return Pipeline(steps=[("preprocessor", preprocessor)])


def run_training():
    """
    ES: Ejecuta el flujo completo: cargar datos, split, ajustar pipeline,
        transformar y guardar pipeline, datos procesados y metadatos.
    EN: Runs the full flow: load data, split, fit pipeline, transform and save
        pipeline, processed data and metadata.
    """
    # --- Load raw dataset -------------------------------------------------
    burnout_df = pd.read_csv(RAW_DATA_PATH)
    print(f"Shape: {burnout_df.shape}")
    print(burnout_df.head())

    # --- Feature lists ----------------------------------------------------
    categorical_features, numerical_features = build_feature_lists(burnout_df)
    print("Categorical features:", categorical_features)
    print("Numerical features:", numerical_features)

    # --- Train / test split ----------------------------------------------
    X = burnout_df[categorical_features + numerical_features]
    y = burnout_df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    print(f"X_train: {X_train.shape}  |  X_test: {X_test.shape}")
    print("\nClass distribution (train):")
    print(y_train.value_counts(normalize=True).round(3))
    print("\nClass distribution (test):")
    print(y_test.value_counts(normalize=True).round(3))

    # --- Fit pipeline -----------------------------------------------------
    preprocessing_pipeline = build_pipeline(categorical_features, numerical_features)
    preprocessing_pipeline.fit(X_train)

    X_train_processed = preprocessing_pipeline.transform(X_train)
    X_test_processed = preprocessing_pipeline.transform(X_test)

    feature_names = (
        preprocessing_pipeline
        .named_steps["preprocessor"]
        .get_feature_names_out()
    )

    print(f"\nX_train_processed shape: {X_train_processed.shape}")
    print(f"X_test_processed shape: {X_test_processed.shape}")
    print("\nResulting features:")
    print(list(feature_names))

    # --- Save pipeline, processed data and metadata -----------------------
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    joblib.dump(preprocessing_pipeline, PIPELINE_PATH)

    np.savez(
        PROCESSED_NPZ_PATH,
        X_train=X_train_processed,
        X_test=X_test_processed,
        y_train=y_train.values,
        y_test=y_test.values,
    )

    metadata = {
        "categorical_features": categorical_features,
        "numerical_features": numerical_features,
        "feature_names_out": list(feature_names),
        "target_classes": ["Low", "Medium", "High"],
    }
    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=2)

    print("\nPipeline, processed data and metadata saved successfully.")


# ---------------------------------------------------------------------------
# Production-facing function
# ---------------------------------------------------------------------------
_fitted_pipeline = None
_expected_columns = None


def _load_artifacts():
    """
    ES: Carga (una sola vez) el pipeline y los metadatos guardados.
    EN: Loads (once) the saved pipeline and metadata.
    """
    global _fitted_pipeline, _expected_columns
    if _fitted_pipeline is None:
        _fitted_pipeline = joblib.load(PIPELINE_PATH)
        with open(METADATA_PATH) as f:
            metadata = json.load(f)
        _expected_columns = (
            metadata["categorical_features"] + metadata["numerical_features"]
        )
    return _fitted_pipeline, _expected_columns


def clean_and_process(raw_dict, pipeline=None, expected_columns=None):
    """
    ES: Transforma un diccionario de entrada (por ejemplo, procedente de un
        formulario HTML) en un array listo para el modelo de riesgo de burnout.
    EN: Transforms an input dictionary (e.g. coming from an HTML form)
        into an array ready for the burnout risk model.

    Parameters
    ----------
    raw_dict : dict
        ES: Claves esperadas: day_type, work_hours, screen_time_hours,
        meetings_count, breaks_taken, after_hours_work, app_switches,
        sleep_hours, task_completion, isolation_index, fatigue_score.
        EN: Expected keys: day_type, work_hours, screen_time_hours,
        meetings_count, breaks_taken, after_hours_work, app_switches,
        sleep_hours, task_completion, isolation_index, fatigue_score.

    Returns
    -------
    numpy.ndarray
        ES: Array 2D (1 fila) listo para predict_attrition().
        EN: 2D array (1 row) ready for predict_attrition().
    """
    if pipeline is None or expected_columns is None:
        pipeline, expected_columns = _load_artifacts()

    # ES: Comprobar que no falte ninguna clave esperada.
    # EN: Check that no expected key is missing.
    missing_keys = [c for c in expected_columns if c not in raw_dict]
    if missing_keys:
        raise ValueError(f"Missing keys in raw_dict: {missing_keys}")

    # ES: DataFrame de una fila con el orden de columnas correcto.
    # EN: Single-row DataFrame with the correct column order.
    input_df = pd.DataFrame([{c: raw_dict[c] for c in expected_columns}])

    return pipeline.transform(input_df)


def _test_clean_and_process():
    """ES: Prueba rápida de la función. | EN: Quick smoke test of the function."""
    sample_raw_dict = {
        "day_type": "Weekday",
        "work_hours": 11.5,
        "screen_time_hours": 10.2,
        "meetings_count": 5,
        "breaks_taken": 2,
        "after_hours_work": 1,
        "app_switches": 95,
        "sleep_hours": 5.2,
        "task_completion": 68.0,
        "isolation_index": 7,
        "fatigue_score": 8.6,
    }
    processed_sample = clean_and_process(sample_raw_dict)
    print("Processed array shape:", processed_sample.shape)
    print(processed_sample)


if __name__ == "__main__":
    run_training()
    print("\n--- Testing clean_and_process ---")
    _test_clean_and_process()