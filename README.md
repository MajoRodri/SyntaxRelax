<div align="center">
  <img src="static/assets/items.png" width="80" align="left"/>
  <img src="static/assets/items_right.png" width="80" align="right"/>
  <img src="static/img/Logo.png" alt="SyntaxRelax logo" height="120"/>
  <h1>SyntaxRelax</h1>
</div>
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
<summary><strong>⚙️ Preprocesado de datos / Data Preprocessing</strong></summary>

### 🎯 Objetivo / Goal

🇪🇸 Transformar el dataset de burnout en datos listos para el entrenamiento del modelo, garantizando que ninguna información del conjunto de test contamine el ajuste de las transformaciones.  
🇬🇧 Transform the burnout dataset into data ready for model training, ensuring no test-set information contaminates the fitting of any transformation.

---

### 🗑️ Variables eliminadas / Removed variables

| Variable | 🇪🇸 ES | 🇬🇧 EN |
|---|---|---|
| `user_id` | Identificador sin valor predictivo | Identifier with no predictive value |
| `burnout_score` | Fuente directa de `burnout_risk` → data leakage | Direct source of `burnout_risk` → data leakage |

> ⚠️ 🇪🇸 `burnout_risk` es la variable objetivo. Usar `burnout_score` como predictor revelaría la respuesta al modelo antes de que prediga.  
> ⚠️ 🇬🇧 `burnout_risk` is the target variable. Using `burnout_score` as a predictor would reveal the answer to the model before it predicts.

---

### ✂️ División train / test

🇪🇸 El dataset se dividió **antes** de ajustar cualquier transformación (80 % entrenamiento · 20 % test) con estratificación para preservar la proporción de las clases, especialmente la clase `High` (~7 % de los datos).  
🇬🇧 The dataset was split **before** fitting any transformation (80% train · 20% test) with stratification to preserve the class proportions, especially the `High` class (~7% of the data).

| Conjunto / Set | Filas / Rows | Low | Medium | High |
|---|---|---|---|---|
| Train | 1 600 | 50.9 % | 42.1 % | 6.9 % |
| Test | 400 | 51.0 % | 42.2 % | 6.8 % |

---

### 🔧 Pipeline de preprocesado / Preprocessing pipeline

🇪🇸 Se construyó un `Pipeline` de scikit-learn con un `ColumnTransformer` que aplica transformaciones distintas según el tipo de variable:  
🇬🇧 A scikit-learn `Pipeline` with a `ColumnTransformer` was built to apply different transformations depending on the variable type:

| Variable | Transformación | 🇪🇸 ES | 🇬🇧 EN |
|---|---|---|---|
| `day_type` | `OneHotEncoder` | Convierte `Weekday`/`Weekend` en columna binaria | Converts `Weekday`/`Weekend` into a binary column |
| Variables numéricas (×10) | `StandardScaler` | Media 0, desviación estándar 1 | Mean 0, standard deviation 1 |

> 🔒 🇪🇸 El pipeline se ajustó **únicamente con datos de entrenamiento** y luego se aplicó al test, evitando así *data leakage*.  
> 🔒 🇬🇧 The pipeline was fitted **only on training data** and then applied to the test set, thus avoiding data leakage.

**Variables de salida tras el pipeline / Output features after the pipeline (11 total):**

```
day_type_Weekend · work_hours · screen_time_hours · meetings_count · breaks_taken
after_hours_work · app_switches · sleep_hours · task_completion · isolation_index · fatigue_score
```

---

### 🔗 Función `clean_and_process()`

🇪🇸 La entrega principal de este notebook es la función `clean_and_process(raw_dict)`, guardada en `src/preprocessing.py`. Recibe el diccionario que enviará el formulario web y devuelve el array NumPy listo para el modelo, desacoplando la lógica de transformación del resto de la aplicación.  
🇬🇧 The main deliverable of this notebook is the `clean_and_process(raw_dict)` function, saved in `src/preprocessing.py`. It receives the dictionary sent by the web form and returns the NumPy array ready for the model, decoupling the transformation logic from the rest of the application.

---

### 💡 Conclusiones / Key takeaways

- ✅ 🇪🇸 El pipeline se serializa en `models/preprocessing_pipeline.joblib` para reutilizarse en predicción sin reentrenar.  
  🇬🇧 The pipeline is serialized to `models/preprocessing_pipeline.joblib` for reuse in prediction without retraining.
- 📦 🇪🇸 Los datos procesados se guardan en `data/processed/burnout_processed.npz` para el notebook 03 (selección y entrenamiento del modelo).  
  🇬🇧 Processed data is saved to `data/processed/burnout_processed.npz` for notebook 03 (model selection and training).
- ⚖️ 🇪🇸 El desbalanceo de la clase `High` (~7 %) se preserva en la división y deberá tratarse durante el modelado (notebook 03).  
  🇬🇧 The `High` class imbalance (~7%) is preserved in the split and must be addressed during modeling (notebook 03).

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

<div align="center">
  <img src="static/assets/itemsI.png" width="80" align="left"/>
  <img src="static/assets/itemsI_right.png" width="80" align="right"/>
  <p>💙 SyntaxRelax &copy; 2026 </p>
</div>
