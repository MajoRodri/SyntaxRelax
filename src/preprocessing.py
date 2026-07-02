def clean_and_process(form_data: dict) -> dict:
    """
    DUMMY: Recibe los datos del formulario (Q1-Q5) y los convierte a enteros.
    Reemplazar con lógica real de preprocessing cuando el pipeline ML esté listo.
    """
    return {
        "Q1": int(form_data.get("Q1", 1)),  # Agotamiento emocional
        "Q2": int(form_data.get("Q2", 1)),  # Dificultad para desconectarse
        "Q3": int(form_data.get("Q3", 1)),  # Falta de motivación
        "Q4": int(form_data.get("Q4", 1)),  # Horas extra semanales
        "Q5": int(form_data.get("Q5", 1)),  # Apoyo del equipo/liderazgo
    }
