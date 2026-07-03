<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td align="left" valign="top" width="80"><img src="static/assets/items.png" width="80"/></td>
    <td align="center" valign="middle">
      <img src="static/img/Logo.png" alt="SyntaxRelax logo" height="120"/>
      <h1>SyntaxRelax</h1>
    </td>
    <td align="right" valign="top" width="80"><img src="static/assets/items_right.png" width="80"/></td>
  </tr>
</table>
<p align="center">
  Herramienta preventiva de apoyo a la decisión para estimar el riesgo de burnout laboral.<br/>
  <em>Preventive decision-support tool for estimating workplace burnout risk.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=flat&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat&logo=jupyter&logoColor=white"/>
</p>

---

## 🧠 ¿Qué es SyntaxRelax? / What is SyntaxRelax?

El burnout, o síndrome de desgaste profesional, afecta cada vez a más personas en el entorno laboral. Detectarlo a tiempo puede marcar la diferencia entre tomar acción preventiva o llegar al agotamiento total.

**SyntaxRelax** es una aplicación web que permite a cualquier persona responder un test breve sobre sus condiciones de trabajo y obtener, en segundos, una estimación de su nivel de riesgo de burnout: bajo, moderado o alto. El resultado se basa en un modelo de machine learning entrenado con datos reales de comportamiento laboral y registros de RRHH. No sustituye una evaluación profesional, pero sí ofrece una señal temprana y accionable.

---

Burnout, or professional exhaustion syndrome, is increasingly affecting people in the workplace. Detecting it early can make the difference between taking preventive action and reaching total exhaustion.

**SyntaxRelax** is a web application that allows anyone to answer a short test about their work conditions and receive, within seconds, an estimate of their burnout risk level: low, moderate, or high. The result is powered by a machine learning model trained on real behavioral and HR data. It does not replace a professional evaluation, but it does provide an early and actionable signal.

---

## 🎬 Demo

> 🇪🇸 Ejecuta la aplicación localmente con los pasos de la sección de instalación.  
> 🇬🇧 Run the application locally following the steps in the installation section.

| 🖥️ Pantalla / Screen | 🇪🇸 ES | 🇬🇧 EN |
|---|---|---|
| 🏠 **Inicio / Home** | Página informativa sobre el burnout y cómo funciona la herramienta | Informational page about burnout and how the tool works |
| 📋 **Test** | Formulario de 5 preguntas sobre tu situación laboral | 5-question form about your current work situation |
| 📊 **Resultado / Result** | Score de 0–100 con nivel de riesgo y barra visual | 0–100 score with risk level and visual progress bar |
| 📄 **Informe PDF / PDF Report** | Descarga un informe personalizado con tus respuestas y resultado | Download a personalized report with your answers and result |

---

## 🛠️ Herramientas utilizadas / Tech Stack

| 🔧 Capa / Layer | ⚙️ Tecnología / Technology |
|---|---|
| 🐍 Backend | Python 3.11, Flask |
| 🤖 Machine Learning | scikit-learn, pandas, numpy |
| 🔍 Análisis exploratorio / EDA | Jupyter Notebooks, matplotlib, seaborn |
| 🎨 Frontend | HTML5, Bootstrap 5, Bootstrap Icons, jsPDF |
| 📦 Entorno / Environment | venv |

---

## 🚀 Instalación y uso / Installation & Usage

```bash
# 🇪🇸 Clona el repositorio / 🇬🇧 Clone the repository
git clone <url-del-repo>
cd SyntaxRelax

# 🇪🇸 Activa el entorno virtual / 🇬🇧 Activate the virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 🇪🇸 Instala dependencias / 🇬🇧 Install dependencies
pip install -r requirements.txt

# 🇪🇸 Ejecuta la app / 🇬🇧 Run the app
python app.py
```

🇪🇸 Abre tu navegador en `http://localhost:5000`.  
🇬🇧 Open your browser at `http://localhost:5000`.

---

<details>
<summary><strong>🔬 Análisis exploratorio de datos / Exploratory Data Analysis (EDA)</strong></summary>

### 📂 Datasets utilizados / Datasets used

🇪🇸 El proyecto combina dos fuentes de datos complementarias.  
🇬🇧 The project combines two complementary data sources.

---

#### 🔥 Dataset de Burnout · [Kaggle](https://www.kaggle.com/datasets/aryanmdev/remote-work-burnout-and-social-isolation-2026)

- 📌 **2.000 registros · 14 columnas · Sin valores nulos**  
  **2,000 records · 14 columns · No missing values**
- 🇪🇸 Contiene variables de comportamiento laboral diario: horas trabajadas, horas de pantalla, reuniones, descansos, sueño, fatiga y aislamiento social.  
  🇬🇧 Contains daily work behavior variables: hours worked, screen time, meetings, breaks, sleep, fatigue, and social isolation.

| Columna / Column | Tipo / Type | Descripción / Description |
|---|---|---|
| user_id | int64 | Identificador de usuario / User identifier |
| day_type | str | Tipo de jornada / Type of workday |
| work_hours | float64 | Horas trabajadas / Hours worked |
| screen_time_hours | float64 | Horas de pantalla / Screen time hours |
| meetings_count | int64 | Número de reuniones / Number of meetings |
| breaks_taken | int64 | Descansos tomados / Breaks taken |
| after_hours_work | int64 | Trabajo fuera de horario / After-hours work |
| app_switches | int64 | Cambios de aplicación / App context switches |
| sleep_hours | float64 | Horas de sueño / Sleep hours |
| task_completion | float64 | Tasa de completitud de tareas / Task completion rate |
| isolation_index | int64 | Índice de aislamiento social / Social isolation index |
| fatigue_score | float64 | Nivel de fatiga / Fatigue level |
| burnout_score | float64 | Variable objetivo continua / Continuous target variable |
| burnout_risk | str | Variable objetivo categórica / Categorical target (Low / Medium / High) |

> ⚠️ 🇪🇸 `burnout_risk` se deriva de `burnout_score`, por lo que `burnout_score` **no debe usarse como predictor**.  
> ⚠️ 🇬🇧 `burnout_risk` is derived from `burnout_score`, so `burnout_score` **must not be used as a predictor**.

**📈 Correlación con `burnout_score` / Correlation with `burnout_score`:**

| Variable | Correlación / Correlation | Interpretación / Interpretation |
|---|---|---|
| fatigue_score | +0.90 | 🔴 Factor de riesgo muy alto / Very high risk factor |
| isolation_index | +0.77 | 🔴 Factor de riesgo alto / High risk factor |
| work_hours | +0.67 | 🟠 Factor de riesgo alto / High risk factor |
| screen_time_hours | +0.66 | 🟠 Factor de riesgo alto / High risk factor |
| app_switches | +0.54 | 🟡 Factor de riesgo moderado / Moderate risk factor |
| meetings_count | +0.33 | 🟡 Factor de riesgo leve / Mild risk factor |
| after_hours_work | +0.30 | 🟡 Factor de riesgo leve / Mild risk factor |
| breaks_taken | -0.35 | 🟢 Factor protector / Protective factor |
| task_completion | -0.46 | 🟢 Factor protector / Protective factor |
| sleep_hours | -0.80 | 🟢 Factor protector fuerte / Strong protective factor |

---

#### 🏢 Dataset de Attrition (IBM HR) · [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

- 📌 **1.470 registros · 35 columnas · Sin valores nulos**  
  **1,470 records · 35 columns · No missing values**
- 🇪🇸 Registros de RRHH con información demográfica, salarial, de satisfacción y de permanencia en la empresa.  
  🇬🇧 HR records with demographic, salary, satisfaction, and tenure information.

> 💼 🇪🇸 **`Attrition`**: `Yes` = el empleado ya no pertenece a la empresa · `No` = empleado activo. No distingue entre salida voluntaria e involuntaria.  
> 💼 🇬🇧 **`Attrition`**: `Yes` = employee no longer belongs to the company · `No` = active employee. Does not distinguish between voluntary and involuntary departures.

**🔗 Pares con alta multicolinealidad / High multicollinearity pairs** (🇪🇸 a gestionar en preprocessing / 🇬🇧 to handle during preprocessing):

| Variable 1 | Variable 2 | Correlación / Correlation |
|---|---|---|
| JobLevel | MonthlyIncome | 0.950 |
| TotalWorkingYears | JobLevel | 0.782 |
| PercentSalaryHike | PerformanceRating | 0.774 |
| MonthlyIncome | TotalWorkingYears | 0.773 |
| YearsWithCurrManager | YearsAtCompany | 0.769 |
| YearsAtCompany | YearsInCurrentRole | 0.759 |
| YearsInCurrentRole | YearsWithCurrManager | 0.714 |
| TotalWorkingYears | Age | 0.680 |
| YearsAtCompany | TotalWorkingYears | 0.628 |
| YearsAtCompany | YearsSinceLastPromotion | 0.618 |

---

### 💡 Hallazgos principales / Key Findings

- ⚖️ 🇪🇸 El riesgo alto de burnout representa solo el **6.9 %** del dataset → desbalanceo de clases que debe tratarse durante el modelado.  
  🇬🇧 High burnout risk represents only **6.9%** of the dataset → class imbalance that must be addressed during modeling.
- 🏆 🇪🇸 Los predictores más potentes son: `fatigue_score`, `isolation_index`, `sleep_hours`, `work_hours` y `screen_time_hours`.  
  🇬🇧 The strongest predictors are: `fatigue_score`, `isolation_index`, `sleep_hours`, `work_hours`, and `screen_time_hours`.
- 📉 🇪🇸 En el dataset de attrition, `OverTime`, `JobSatisfaction`, `WorkLifeBalance`, `JobRole`, `Department` y `MonthlyIncome` muestran las relaciones más relevantes con la salida de empleados.  
  🇬🇧 In the attrition dataset, `OverTime`, `JobSatisfaction`, `WorkLifeBalance`, `JobRole`, `Department`, and `MonthlyIncome` show the most relevant relationships with employee departure.
- 🚨 🇪🇸 Los roles con mayor tasa de attrition son: **Sales Representative**, **Laboratory Technician** y **Human Resources**.  
  🇬🇧 Roles with the highest attrition rates are: **Sales Representative**, **Laboratory Technician**, and **Human Resources**.

### 🗑️ Variables a excluir en preprocessing / Variables to exclude in preprocessing

| Variable | 🇪🇸 ES | 🇬🇧 EN |
|---|---|---|
| EmployeeCount | Varianza cero | Zero variance |
| StandardHours | Varianza cero | Zero variance |
| EmployeeNumber | Identificador sin valor predictivo | Identifier with no predictive value |
| burnout_score | Fuente directa de `burnout_risk` (data leakage) | Direct source of `burnout_risk` (data leakage) |

</details>

<details>
<summary><strong>📁 Estructura del proyecto / Project Structure</strong></summary>

```
SyntaxRelax/
├── app.py                          # 🐍 Aplicación Flask / Flask application
├── src/
│   ├── preprocessing.py            # ⚙️ Pipeline de features / Feature engineering pipeline
│   └── model_utils.py              # 🤖 Carga del modelo y predicción / Model loading & prediction
├── templates/
│   ├── home.html                   # 🏠 Página de inicio / Home page
│   └── index.html                  # 📋 Test de burnout + resultados / Burnout test + results
├── static/
│   └── img/
│       └── Logo.png
├── notebooks/
│   ├── 01_business_oriented_exploratory_data_analysis.ipynb
│   ├── 02_data_preprocessing_and_engineering.ipynb
│   ├── 03_model_selection_and_training.ipynb
│   └── 04_model_evaluation_and_metrics.ipynb
└── requirements.txt
```

</details>

## 👥 Equipo / Team

| Miembro | Rol | Contacto |
| :--- | :--- | :--- |
| **Mariajose Alvarez** | 🔄 Scrum Master | [@MajoRodri](https://github.com/MajoRodri) |
| **Verónica Melero** | 🎯 Product Owner | [@vmelero13](https://github.com/vmelero13) |
| **Anas Fady** | 💻 Developer | [@Anasfady](https://github.com/Anasfady) |
| **Javier** | 💻 Developer | [@JCRbit](https://github.com/JCRbit) |
| **Yohanna S.Perez** | 💻 Developer | [@yohperez](https://github.com/yohperez) |

<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td align="left" valign="bottom" width="80"><img src="static/assets/itemsI.png" width="80"/></td>
    <td align="center" valign="middle">
      <p>💙 SyntaxRelax &copy; 2026 — HR Analytics Platform</p>
    </td>
    <td align="right" valign="bottom" width="80"><img src="static/assets/itemsI_right.png" width="80"/></td>
  </tr>
</table>
