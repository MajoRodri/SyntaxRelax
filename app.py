import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from src.preprocessing import clean_and_process

app = Flask(__name__)

# ── Carga de artefactos / Artifact loading ──────────────────────────────────
_pipeline = None
_model    = None

def _get_artifacts():
    global _pipeline, _model
    if _pipeline is None:
        base      = os.path.dirname(os.path.abspath(__file__))
        _pipeline = joblib.load(os.path.join(base, "models", "preprocessing_pipeline.joblib"))
        _model    = joblib.load(os.path.join(base, "models", "best_burnout_model.joblib"))
    return _pipeline, _model


# ── Metadatos de características / Feature metadata for top-factors ─────────
_FEATURE_META = {
    "categorical__day_type_Weekend": {"es": "Tipo de jornada",       "en": "Day type",          "dir": -1},
    "numerical__work_hours":         {"es": "Horas de trabajo",      "en": "Working hours",     "dir":  1},
    "numerical__screen_time_hours":  {"es": "Horas de pantalla",     "en": "Screen time",       "dir":  1},
    "numerical__meetings_count":     {"es": "Reuniones",             "en": "Meetings",          "dir":  1},
    "numerical__breaks_taken":       {"es": "Descansos tomados",     "en": "Breaks taken",      "dir": -1},
    "numerical__after_hours_work":   {"es": "Trabajo fuera horario", "en": "After-hours work",  "dir":  1},
    "numerical__app_switches":       {"es": "Cambios app/tarea",     "en": "App switches",      "dir":  1},
    "numerical__sleep_hours":        {"es": "Horas de sueño",        "en": "Sleep hours",       "dir": -1},
    "numerical__task_completion":    {"es": "Tareas completadas",    "en": "Task completion",   "dir": -1},
    "numerical__isolation_index":    {"es": "Aislamiento social",    "en": "Social isolation",  "dir":  1},
    "numerical__fatigue_score":      {"es": "Nivel de fatiga",       "en": "Fatigue level",     "dir":  1},
}

_BADGE_MAP = {
    "Low":    ("success", "Riesgo Bajo"),
    "Medium": ("warning", "Riesgo Moderado"),
    "High":   ("danger",  "Alto Riesgo de Burnout"),
}


def _format_value(fname: str, raw: dict) -> str:
    if fname == "categorical__day_type_Weekend":
        return "Fin de semana" if raw.get("day_type") == "Weekend" else "Día de semana"
    key = fname.replace("numerical__", "")
    val = raw.get(key)
    if val is None:
        return "–"
    if key == "after_hours_work":
        return "Sí" if int(val) == 1 else "No"
    units = {"work_hours": " h", "screen_time_hours": " h", "sleep_hours": " h",
             "task_completion": " %", "isolation_index": "/9", "fatigue_score": "/10"}
    return f"{val}{units.get(key, '')}"


def _predict(raw_features: dict) -> dict:
    pipeline, model = _get_artifacts()

    df    = pd.DataFrame([raw_features])
    X     = pipeline.transform(df)
    proba = model.predict_proba(X)[0]          # [P(Low), P(Medium), P(High)]

    classes         = ["Low", "Medium", "High"]
    predicted_class = classes[int(np.argmax(proba))]
    badge, label    = _BADGE_MAP[predicted_class]

    # Puntuación de riesgo ponderada / Weighted risk score  0-100
    score = round(float(proba[0] * 0 + proba[1] * 50 + proba[2] * 100))

    # Top 3 factores contribuyentes / Top 3 contributing factors
    # contribución = importancia × valor_escalado × dirección / contribution = importance × scaled_value × direction
    # positivo → empuja a mayor riesgo / positive → pushes toward higher risk
    feature_names = pipeline.named_steps["preprocessor"].get_feature_names_out()
    importances   = model.feature_importances_

    factors = []
    for i, fname in enumerate(feature_names):
        meta    = _FEATURE_META.get(fname, {})
        contrib = float(importances[i]) * float(X[0][i]) * meta.get("dir", 1)
        factors.append({
            "contrib":  contrib,
            "label_es": meta.get("es", fname),
            "label_en": meta.get("en", fname),
            "value":    _format_value(fname, raw_features),
            "risk":     "danger" if contrib > 0 else "protective",
        })

    top3 = sorted(factors, key=lambda x: abs(x["contrib"]), reverse=True)[:3]
    for f in top3:
        del f["contrib"]

    return {
        "label":   label,
        "badge":   badge,
        "score":   score,
        "proba":   {
            "low":    round(float(proba[0]) * 100),
            "medium": round(float(proba[1]) * 100),
            "high":   round(float(proba[2]) * 100),
        },
        "factors": top3,
    }


# ── Rutas / Routes ──────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form.to_dict()
    processed = clean_and_process(form_data)
    result    = _predict(processed)
    return render_template("index.html", result=result, form_data=form_data)


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/predict_chat", methods=["POST"])
def predict_chat():
    data      = request.get_json()
    processed = clean_and_process(data)
    result    = _predict(processed)
    return jsonify(result=result, form_data=data)


if __name__ == "__main__":
    app.run(debug=False)
