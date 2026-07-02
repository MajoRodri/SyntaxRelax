def predict_attrition(processed_data: dict) -> dict:
    """
    DUMMY: Calcula un score de riesgo de burnout a partir de Q1-Q5.
    Cada pregunta puntúa de 1 (bajo riesgo) a 5 (alto riesgo).
    Score máximo raw = 25 → se normaliza a 100.
    """
    raw = sum([
        processed_data.get("Q1", 1),
        processed_data.get("Q2", 1),
        processed_data.get("Q3", 1),
        processed_data.get("Q4", 1),
        processed_data.get("Q5", 1),
    ])

    score = round((raw / 25) * 100)

    if score >= 70:
        label, badge = "Alto Riesgo de Burnout", "danger"
    elif score >= 40:
        label, badge = "Riesgo Moderado", "warning"
    else:
        label, badge = "Riesgo Bajo", "success"

    return {"label": label, "badge": badge, "score": score}
