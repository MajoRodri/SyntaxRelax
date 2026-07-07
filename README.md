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
  <img src="https://img.shields.io/badge/XGBoost-Model-E86C00?style=flat&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-Pipeline-F7931E?style=flat&logo=scikit-learn&logoColor=white"/>
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

> ES Ejecuta la aplicación localmente con los pasos de la sección de instalación.  
> EN Run the application locally following the steps in the installation section.

| 🖥️ Pantalla / Screen | ES | EN |
|---|---|---|
| 🏠 **Inicio / Home** | Página informativa sobre el burnout y cómo funciona la herramienta | Informational page about burnout and how the tool works |
| 📋 **Test** | Formulario de preguntas sobre tu situación laboral | Question form about your current work situation |
| 💬 **Chat** | Conversación guiada de 11 preguntas con un asistente virtual | Guided 11-question conversation with a virtual assistant |
| 📊 **Resultado / Result** | Score de 0–100 con gráfica de dona, nivel de riesgo y factores principales | 0–100 score with donut chart, risk level, and top contributing factors |
| 📄 **Informe PDF / PDF Report** | Descarga un informe personalizado bilingüe con tus respuestas, resultado y recomendaciones | Download a bilingual personalized report with answers, result, and recommendations |

---

## 🦥 Neo — El asistente / The assistant

<div align="center">
  <img src="static/icons/neo.png" alt="Neo" width="120" style="border-radius:50%;"/>
</div>

<br/>

**Neo** es el asistente conversacional de SyntaxRelax. Su nombre viene de *nuevo*: la idea central es innovar la forma en que las personas se relacionan con su bienestar laboral, dándoles una herramienta accesible y sin juicios para detectar señales de burnout antes de que sea tarde.

**Neo** is SyntaxRelax's conversational assistant. Its name comes from *new*: the core idea is to innovate the way people relate to their work wellbeing, giving them an accessible, judgment-free tool to detect burnout signals before it's too late.

---

**ES — ¿Por qué un perezoso?**
Elegimos un perezoso como mascota de Neo porque su imagen transmite exactamente lo que buscamos: calma, pausa y apoyo. En un entorno laboral acelerado, Neo recuerda que está bien ir despacio, descansar y pedir ayuda. No juzga, no presiona, solo acompaña.

**EN — Why a sloth?**
We chose a sloth as Neo's mascot because its image conveys exactly what we're after: calm, pause, and support. In a fast-paced work environment, Neo reminds you that it's okay to slow down, rest, and ask for help. No judgment, no pressure, just companionship.

---

**ES — Rol de Neo**
Neo guía al usuario a través de 11 preguntas sobre su jornada laboral en un espacio seguro y confidencial. A partir de esas respuestas, el modelo detecta patrones de vulnerabilidad y estima el nivel de riesgo de burnout, ofreciendo recomendaciones concretas y accionables.

**EN — Neo's role**
Neo guides the user through 11 questions about their workday in a safe, confidential space. From those answers, the model detects vulnerability patterns and estimates the burnout risk level, delivering concrete, actionable recommendations.

---

## 🛠️ Herramientas utilizadas / Tech Stack

| 🔧 Capa / Layer | ⚙️ Tecnología / Technology |
|---|---|
| 🐍 Backend | Python 3.11, Flask |
| 🤖 Machine Learning | XGBoost, scikit-learn, pandas, numpy |
| 🔍 Análisis exploratorio / EDA | Jupyter Notebooks, matplotlib, seaborn |
| 🎨 Frontend | HTML5, Bootstrap 5, Bootstrap Icons, jsPDF |
| 📦 Entorno / Environment | venv |

---

## 🚀 Instalación y uso / Installation & Usage

```bash
# ES Clona el repositorio / EN Clone the repository
git clone <url-del-repo>
cd SyntaxRelax

# ES Activa el entorno virtual / EN Activate the virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# ES Instala dependencias / EN Install dependencies
pip install -r requirements.txt

# ES Ejecuta la app / EN Run the app
python app.py
```

ES Abre tu navegador en `http://localhost:5000`.  
EN Open your browser at `http://localhost:5000`.

---

<details>
<summary><strong>🔬 Análisis exploratorio de datos / Exploratory Data Analysis (EDA)</strong></summary>

### 📂 Datasets utilizados / Datasets used

ES El proyecto combina dos fuentes de datos complementarias.  
EN The project combines two complementary data sources.

---

#### 🔥 Dataset de Burnout · [Kaggle](https://www.kaggle.com/datasets/aryanmdev/remote-work-burnout-and-social-isolation-2026)

- 📌 **2.000 registros · 14 columnas · Sin valores nulos**  
  **2,000 records · 14 columns · No missing values**
- ES Contiene variables de comportamiento laboral diario: horas trabajadas, horas de pantalla, reuniones, descansos, sueño, fatiga y aislamiento social.  
  EN Contains daily work behavior variables: hours worked, screen time, meetings, breaks, sleep, fatigue, and social isolation.

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

> ⚠️ ES `burnout_risk` se deriva de `burnout_score`, por lo que `burnout_score` **no debe usarse como predictor**.  
> ⚠️ EN `burnout_risk` is derived from `burnout_score`, so `burnout_score` **must not be used as a predictor**.

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
- ES Registros de RRHH con información demográfica, salarial, de satisfacción y de permanencia en la empresa.  
  EN HR records with demographic, salary, satisfaction, and tenure information.

> 💼 ES **`Attrition`**: `Yes` = el empleado ya no pertenece a la empresa · `No` = empleado activo. No distingue entre salida voluntaria e involuntaria.  
> 💼 EN **`Attrition`**: `Yes` = employee no longer belongs to the company · `No` = active employee. Does not distinguish between voluntary and involuntary departures.

**🔗 Pares con alta multicolinealidad / High multicollinearity pairs** (ES a gestionar en preprocessing / EN to handle during preprocessing):

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

- ⚖️ ES El riesgo alto de burnout representa solo el **6.9 %** del dataset → desbalanceo de clases que debe tratarse durante el modelado.  
  EN High burnout risk represents only **6.9%** of the dataset → class imbalance that must be addressed during modeling.
- 🏆 ES Los predictores más potentes son: `fatigue_score`, `isolation_index`, `sleep_hours`, `work_hours` y `screen_time_hours`.  
  EN The strongest predictors are: `fatigue_score`, `isolation_index`, `sleep_hours`, `work_hours`, and `screen_time_hours`.
- 📉 ES En el dataset de attrition, `OverTime`, `JobSatisfaction`, `WorkLifeBalance`, `JobRole`, `Department` y `MonthlyIncome` muestran las relaciones más relevantes con la salida de empleados.  
  EN In the attrition dataset, `OverTime`, `JobSatisfaction`, `WorkLifeBalance`, `JobRole`, `Department`, and `MonthlyIncome` show the most relevant relationships with employee departure.
- 🚨 ES Los roles con mayor tasa de attrition son: **Sales Representative**, **Laboratory Technician** y **Human Resources**.  
  EN Roles with the highest attrition rates are: **Sales Representative**, **Laboratory Technician**, and **Human Resources**.

### 🗑️ Variables a excluir en preprocessing / Variables to exclude in preprocessing

| Variable | ES | EN |
|---|---|---|
| EmployeeCount | Varianza cero | Zero variance |
| StandardHours | Varianza cero | Zero variance |
| EmployeeNumber | Identificador sin valor predictivo | Identifier with no predictive value |
| burnout_score | Fuente directa de `burnout_risk` (data leakage) | Direct source of `burnout_risk` (data leakage) |

</details>

<details>
<summary><strong>⚙️ Preprocesado de datos / Data Preprocessing</strong></summary>

### 🎯 Objetivo / Goal

ES Transformar el dataset de burnout en datos listos para el entrenamiento del modelo, garantizando que ninguna información del conjunto de test contamine el ajuste de las transformaciones.  
EN Transform the burnout dataset into data ready for model training, ensuring no test-set information contaminates the fitting of any transformation.

---

### 🗑️ Variables eliminadas / Removed variables

| Variable | ES | EN |
|---|---|---|
| `user_id` | Identificador sin valor predictivo | Identifier with no predictive value |
| `burnout_score` | Fuente directa de `burnout_risk` → data leakage | Direct source of `burnout_risk` → data leakage |

> ⚠️ ES `burnout_risk` es la variable objetivo. Usar `burnout_score` como predictor revelaría la respuesta al modelo antes de que prediga.  
> ⚠️ EN `burnout_risk` is the target variable. Using `burnout_score` as a predictor would reveal the answer to the model before it predicts.

---

### ✂️ División train / test

ES El dataset se dividió **antes** de ajustar cualquier transformación (80 % entrenamiento · 20 % test) con estratificación para preservar la proporción de las clases, especialmente la clase `High` (~7 % de los datos).  
EN The dataset was split **before** fitting any transformation (80% train · 20% test) with stratification to preserve the class proportions, especially the `High` class (~7% of the data).

| Conjunto / Set | Filas / Rows | Low | Medium | High |
|---|---|---|---|---|
| Train | 1 600 | 50.9 % | 42.1 % | 6.9 % |
| Test | 400 | 51.0 % | 42.2 % | 6.8 % |

---

### 🔧 Pipeline de preprocesado / Preprocessing pipeline

ES Se construyó un `Pipeline` de scikit-learn con un `ColumnTransformer` que aplica transformaciones distintas según el tipo de variable:  
EN A scikit-learn `Pipeline` with a `ColumnTransformer` was built to apply different transformations depending on the variable type:

| Variable | Transformación | ES | EN |
|---|---|---|---|
| `day_type` | `OneHotEncoder` | Convierte `Weekday`/`Weekend` en columna binaria | Converts `Weekday`/`Weekend` into a binary column |
| Variables numéricas (×10) | `StandardScaler` | Media 0, desviación estándar 1 | Mean 0, standard deviation 1 |

> 🔒 ES El pipeline se ajustó **únicamente con datos de entrenamiento** y luego se aplicó al test, evitando así *data leakage*.  
> 🔒 EN The pipeline was fitted **only on training data** and then applied to the test set, thus avoiding data leakage.

**Variables de salida tras el pipeline / Output features after the pipeline (11 total):**

```
day_type_Weekend · work_hours · screen_time_hours · meetings_count · breaks_taken
after_hours_work · app_switches · sleep_hours · task_completion · isolation_index · fatigue_score
```

---

### 🔗 Función `clean_and_process()`

ES La entrega principal de este notebook es la función `clean_and_process(raw_dict)`, guardada en `src/preprocessing.py`. Recibe el diccionario que enviará el formulario web y devuelve el array NumPy listo para el modelo, desacoplando la lógica de transformación del resto de la aplicación.  
EN The main deliverable of this notebook is the `clean_and_process(raw_dict)` function, saved in `src/preprocessing.py`. It receives the dictionary sent by the web form and returns the NumPy array ready for the model, decoupling the transformation logic from the rest of the application.

---

### 💡 Conclusiones / Key takeaways

- ✅ ES El pipeline se serializa en `models/preprocessing_pipeline.joblib` para reutilizarse en predicción sin reentrenar.  
  EN The pipeline is serialized to `models/preprocessing_pipeline.joblib` for reuse in prediction without retraining.
- 📦 ES Los datos procesados se guardan en `data/processed/burnout_processed.npz` para el notebook 03 (selección y entrenamiento del modelo).  
  EN Processed data is saved to `data/processed/burnout_processed.npz` for notebook 03 (model selection and training).
- ⚖️ ES El desbalanceo de la clase `High` (~7 %) se preserva en la división y deberá tratarse durante el modelado (notebook 03).  
  EN The `High` class imbalance (~7%) is preserved in the split and must be addressed during modeling (notebook 03).

</details>

<details>
<summary><strong>🤖 Selección y entrenamiento del modelo / Model Selection & Training</strong></summary>

### 🎯 Estrategia de validación / Validation strategy

ES Se empleó **Validación Cruzada Estratificada de 5 pliegues** (`StratifiedKFold`) durante la búsqueda de hiperparámetros con `RandomizedSearchCV`, optimizando la métrica **F1 Macro** para compensar el desbalanceo de la clase `High` (~7 % del dataset).  
EN **5-fold Stratified Cross-Validation** (`StratifiedKFold`) was used during hyperparameter tuning via `RandomizedSearchCV`, optimizing **Macro F1** to compensate for the `High` class imbalance (~7% of the dataset).

---

### 📊 Comparativa de modelos / Model comparison

| Modelo / Model | CV Val F1 (Macro) | Test F1 (Macro) | Test Accuracy | Overfitting Gap |
|---|---|---|---|---|
| 🏆 **XGBoost** | 0.9377 | **0.9857** | **98.75 %** | 0.0623 |
| SVM (kernel lineal) | 0.9683 | 0.9837 | 98.50 % | **0.0140** |
| Softmax Regression | 0.9652 | 0.9819 | 98.25 % | 0.0161 |
| Random Forest | 0.9230 | 0.9350 | 96.50 % | 0.0770 |

---

### 🏆 Modelo seleccionado: XGBoost

ES Se seleccionó **XGBoost** con los siguientes hiperparámetros óptimos encontrados por `RandomizedSearchCV`:

| Hiperparámetro | Valor |
|---|---|
| `n_estimators` | 100 |
| `max_depth` | 3 |
| `learning_rate` | 0.2 |
| `eval_metric` | `mlogloss` |

ES Aunque el modelo memoriza el conjunto de entrenamiento ($\text{CV Train F1} = 1.0$), la restricción `max_depth: 3` contiene el sobreajuste y sus patrones son altamente transferibles a datos nuevos (Test F1 = 0.9857).  
EN Although the model memorizes the training set ($\text{CV Train F1} = 1.0$), the `max_depth: 3` constraint contains overfitting and its learned patterns transfer strongly to new data (Test F1 = 0.9857).

> 💡 ES **Alternativa:** SVM con kernel lineal o Softmax Regression tienen una pérdida de rendimiento marginal (< 0.4 %) con mayor interpretabilidad, útiles si se requiere explicabilidad ante comités de RRHH.  
> 💡 EN **Alternative:** SVM with linear kernel or Softmax Regression show marginal performance loss (< 0.4%) with greater interpretability — suitable when explainability to HR committees is required.

---

### ⚙️ Cómo funciona la predicción en producción / How prediction works in production

ES Cuando el usuario completa el test, `app.py` ejecuta los siguientes pasos:  
EN When the user completes the test, `app.py` runs the following steps:

1. **Preprocessing** — El input pasa por el pipeline scikit-learn serializado (StandardScaler + OneHotEncoder). / The input goes through the serialized sklearn pipeline (StandardScaler + OneHotEncoder).
2. **Inference** — XGBoost devuelve probabilidades para las 3 clases: `P(Low)`, `P(Medium)`, `P(High)`. / XGBoost returns probabilities for 3 classes: `P(Low)`, `P(Medium)`, `P(High)`.
3. **Badge** — La clase con mayor probabilidad (`argmax`) determina el nivel de riesgo. / The class with the highest probability (`argmax`) determines the risk level.
4. **Score 0–100** — Indicador visual ponderado: `score = round(P(Low)×0 + P(Medium)×50 + P(High)×100)`.
5. **Top 3 factores / Top 3 factors** — Se calcula `importancia × valor_escalado × dirección_de_riesgo` por feature para identificar los factores que más empujan hacia un riesgo alto para ese usuario concreto. / Computed as `importance × scaled_value × risk_direction` per feature to identify the factors most pushing toward high risk for that specific user.

</details>

<details>
<summary><strong>✅ Evaluación y calidad / Evaluation & QA</strong></summary>

### 🎯 Objetivo / Goal

ES El notebook `04_model_evaluation_and_metrics.ipynb` cubre el rol de QA del equipo: verifica de forma independiente que el pipeline de preprocesado y el modelo entrenado funcionan correctamente antes de integrarse en la aplicación web.  
EN Notebook `04_model_evaluation_and_metrics.ipynb` covers the team's QA role: it independently verifies that the preprocessing pipeline and the trained model work correctly before being integrated into the web application.

---

### 🧪 Test Notebook 02 — Sanity Check del pipeline / Pipeline Sanity Check

ES Se carga el artefacto `preprocessing_pipeline.joblib` generado por el notebook 02 y se prueba la función `clean_and_process(raw_dict)` con un ejemplo simulado (perfil de riesgo esperado: medio/alto). Valida que el pipeline es reutilizable de forma independiente por el resto del equipo.  
EN The `preprocessing_pipeline.joblib` artifact from notebook 02 is loaded and the `clean_and_process(raw_dict)` function is tested with a simulated example (expected risk profile: medium/high). Validates that the pipeline is independently reusable by the rest of the team.

---

### 📊 Test Notebook 03 — Evaluación del modelo / Model Evaluation

| Sección / Section | ES | EN |
|---|---|---|
| **Métricas de clasificación** | Accuracy, Precision, Recall y F1-score (macro) en train y test | Accuracy, Precision, Recall and F1-score (macro) on train and test |
| **Overfitting checklist** | Comparación del F1-macro de train y test frente a un umbral de referencia | Comparison of train and test macro F1 against a reference threshold |
| **Matriz de confusión** | Versión absoluta y normalizada por fila (recall por clase) | Absolute and row-normalized versions (recall per class) |
| **Curvas ROC y Precision-Recall** | Una curva por clase (One-vs-Rest), AUC cercano a 1.0 en las 3 clases | One curve per class (One-vs-Rest), AUC close to 1.0 for all 3 classes |
| **Feature importance** | Ranking de variables según XGBoost, coherente con los hallazgos del EDA | Variable ranking per XGBoost, consistent with EDA findings |

---

### 🏁 Resultados clave / Key Results

- 🎯 **Recall del 100 %** en la clase `High` en test → la herramienta no deja pasar ningún caso de riesgo alto.  
  **100% recall** on the `High` class in test → the tool misses no high-risk case.
- 📈 **Test F1 Macro = 0.9857** · **Test Accuracy = 98.75 %**
- ✅ Gap de overfitting controlado — el modelo generaliza correctamente pese a memorizar el training set.  
  Overfitting gap under control — the model generalizes correctly despite memorizing the training set.

</details>

<details>
<summary><strong>📁 Estructura del proyecto / Project Structure</strong></summary>

```
SyntaxRelax/
├── app.py                              # 🐍 Aplicación Flask — rutas y lógica de predicción / Flask app — routes & prediction logic
├── src/
│   └── preprocessing.py                # ⚙️ Pipeline de features / Feature engineering pipeline
├── models/
│   ├── best_burnout_model.joblib       # 🏆 Modelo XGBoost serializado / Serialized XGBoost model
│   ├── preprocessing_pipeline.joblib   # 🔧 Pipeline sklearn serializado / Serialized sklearn pipeline
│   └── preprocessing_metadata.json    # 📋 Metadatos del pipeline / Pipeline metadata
├── templates/
│   ├── base.html                       # 🧩 Plantilla base con navbar y footer / Base template with navbar & footer
│   ├── home.html                       # 🏠 Página de inicio / Home page
│   ├── index.html                      # 📋 Test de burnout + resultados / Burnout test + results
│   ├── chat.html                       # 💬 Interfaz de chat + resultados / Chat interface + results
│   └── partials/                       # 🧱 Secciones reutilizables de home / Reusable home sections
│       ├── home_hero.html
│       ├── home_how.html
│       ├── home_burnout.html
│       ├── home_what.html
│       ├── home_data.html
│       ├── home_model.html
│       ├── home_who.html
│       └── home_cta.html
├── static/
│   ├── img/Logo.png
│   ├── assets/                         # 🎨 Imágenes decorativas / Decorative assets
│   └── js/
│       └── pdf-utils.js                # 📄 Helpers de generación de PDF / PDF generation helpers
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
