"""
ES: Módulo de preprocesado de datos para la app de riesgo de burnout.
EN: Data preprocessing module for the burnout risk app.

Miembro 2 - Anas: Data Engineer
"""

import json
import joblib
import pandas as pd

_PIPELINE_PATH = "models/preprocessing_pipeline.joblib"
_METADATA_PATH = "models/preprocessing_metadata.json"

_fitted_pipeline = joblib.load(_PIPELINE_PATH)

with open(_METADATA_PATH) as f:
    _metadata = json.load(f)

_expected_columns = _metadata["categorical_features"] + _metadata["numerical_features"]


def clean_and_process(raw_dict, pipeline=_fitted_pipeline, expected_columns=_expected_columns):
    """
    ES: Transforma un diccionario de entrada (formulario HTML) en un array
    listo para el modelo de riesgo de burnout.
    EN: Transforms an input dictionary (HTML form) into an array ready
    for the burnout risk model.
    """

    missing_keys = [column for column in expected_columns if column not in raw_dict]
    if missing_keys:
        raise ValueError(f"Missing keys in raw_dict: {missing_keys}")

    input_df = pd.DataFrame([{column: raw_dict[column] for column in expected_columns}])

    return pipeline.transform(input_df)
