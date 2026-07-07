"""
ES: Módulo de preprocesado de datos para la app de riesgo de burnout.
EN: Data preprocessing module for the burnout risk app.

Miembro 2 - Anas: Data Engineer
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH      = os.path.join(_ROOT, "data", "01_output", "burnout_df.csv")
MODELS_DIR         = os.path.join(_ROOT, "models")
PROCESSED_DIR      = os.path.join(_ROOT, "data", "processed")
PIPELINE_PATH      = os.path.join(MODELS_DIR, "preprocessing_pipeline.joblib")
METADATA_PATH      = os.path.join(MODELS_DIR, "preprocessing_metadata.json")
PROCESSED_NPZ_PATH = os.path.join(PROCESSED_DIR, "burnout_processed.npz")

# ---------------------------------------------------------------------------
# Feature definitions
# ---------------------------------------------------------------------------
RANDOM_STATE = 42
TARGET_COLUMN = "burnout_risk"

COLUMNS_TO_DROP      = ["user_id", "burnout_score", TARGET_COLUMN]
CATEGORICAL_FEATURES = ["day_type"]


def build_feature_lists(df):
    """
    ES: Extrae las listas de features categóricas y numéricas del DataFrame.
    EN: Extracts categorical and numerical feature lists from the DataFrame.
    """
    numerical_features = [
        col for col in df.columns
        if col not in COLUMNS_TO_DROP + CATEGORICAL_FEATURES
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
    burnout_df = pd.read_csv(RAW_DATA_PATH)
    print(f"Shape: {burnout_df.shape}")
    print(burnout_df.head())

    categorical_features, numerical_features = build_feature_lists(burnout_df)
    print("Categorical features:", categorical_features)
    print("Numerical features:", numerical_features)

    X = burnout_df[categorical_features + numerical_features]
    y = burnout_df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y,
    )

    print(f"X_train: {X_train.shape}  |  X_test: {X_test.shape}")
    print("\nClass distribution (train):")
    print(y_train.value_counts(normalize=True).round(3))
    print("\nClass distribution (test):")
    print(y_test.value_counts(normalize=True).round(3))

    preprocessing_pipeline = build_pipeline(categorical_features, numerical_features)
    preprocessing_pipeline.fit(X_train)

    X_train_processed = preprocessing_pipeline.transform(X_train)
    X_test_processed  = preprocessing_pipeline.transform(X_test)

    feature_names = (
        preprocessing_pipeline
        .named_steps["preprocessor"]
        .get_feature_names_out()
    )

    print(f"\nX_train_processed shape: {X_train_processed.shape}")
    print(f"X_test_processed shape:  {X_test_processed.shape}")
    print("\nResulting features:", list(feature_names))

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
        "numerical_features":   numerical_features,
        "feature_names_out":    list(feature_names),
        "target_classes":       sorted(y.unique().tolist()),
    }
    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=2)

    print("\nPipeline, processed data and metadata saved successfully.")



def clean_and_process(form_data: dict) -> dict:
    """
    ES: Convierte las respuestas del chat a los tipos correctos del dataset.
    EN: Converts chat answers to the correct dataset feature types.
    """
    return {
        "day_type":          str(form_data.get("day_type", "Weekday")),
        "work_hours":        float(form_data.get("work_hours", 8.0)),
        "screen_time_hours": float(form_data.get("screen_time_hours", 7.0)),
        "meetings_count":    int(float(form_data.get("meetings_count", 3))),
        "breaks_taken":      int(float(form_data.get("breaks_taken", 5))),
        "after_hours_work":  int(float(form_data.get("after_hours_work", 0))),
        "app_switches":      int(float(form_data.get("app_switches", 50))),
        "sleep_hours":       float(form_data.get("sleep_hours", 7.0)),
        "task_completion":   float(form_data.get("task_completion", 80.0)),
        "isolation_index":   int(float(form_data.get("isolation_index", 5))),
        "fatigue_score":     float(form_data.get("fatigue_score", 6.0)),
    }


if __name__ == "__main__":
    run_training()
