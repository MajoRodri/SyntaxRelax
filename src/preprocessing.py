import pandas as pd
import os
import joblib

def clean_and_process(raw_dict):
    """
    Cleans and preprocesses raw HR data for the Attrition ML model.
    Limpia y preprocesa los datos brutos de RRHH para el modelo de ML de Attrition.
    """
    # 1. Convert input to DataFrame / Convertir la entrada a DataFrame
    df = pd.DataFrame([raw_dict])
    
    # 2. Drop useless and highly correlated columns / Eliminar columnas inútiles y altamente correlacionadas
    # We drop IDs, zero-variance columns, and variables that cause multicollinearity (like JobLevel).
    # Eliminamos IDs, columnas sin varianza y variables que causan multicolinealidad (como JobLevel).
    cols_to_drop = [
        'EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours', # Zero variance / Useless IDs
        'JobLevel',               # Highly correlated with MonthlyIncome (0.95)
        'TotalWorkingYears',      # Correlated with Age and MonthlyIncome
        'PerformanceRating',      # Correlated with PercentSalaryHike
        'YearsWithCurrManager',   # Correlated with YearsAtCompany
        'YearsInCurrentRole'      # Correlated with YearsAtCompany
    ]
    
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns], errors='ignore')
    
    # Path to models directory / Ruta al directorio de modelos
    models_dir = os.path.join(os.path.dirname(__file__), '../models')
    
    try:
        # 3. Encode Categorical Features / Codificar Variables Categóricas
        # HR inputs text (e.g., 'Yes'/'No', 'Sales'), the model needs numbers (0/1).
        # RRHH introduce texto ('Yes'/'No', 'Sales'), el modelo necesita números (0/1).
        categorical_cols = [
            'BusinessTravel', 'Department', 'EducationField', 
            'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
        ]
        
        for col in categorical_cols:
            if col in df.columns:
                encoder_path = os.path.join(models_dir, f'encoder_{col.lower()}.pkl')
                if os.path.exists(encoder_path):
                    le = joblib.load(encoder_path)
                    df[col] = le.transform(df[col])
                else:
                    print(f"Warning/Advertencia: Encoder for {col} not found.")

        # 4. Scale Numerical Features / Escalar Variables Numéricas
        # Prevents large numbers (MonthlyIncome) from dominating small numbers (Age).
        #  Evita que los números grandes (MonthlyIncome) dominen a los pequeños (Age).
        scaler_path = os.path.join(models_dir, 'scaler.pkl')
        if os.path.exists(scaler_path):
            scaler = joblib.load(scaler_path)
            
            num_cols = [
                'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 
                'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 
                'PercentSalaryHike', 'TrainingTimesLastYear', 
                'YearsAtCompany', 'YearsSinceLastPromotion'
            ]
            
            num_cols_present = [col for col in num_cols if col in df.columns]
            
            if num_cols_present:
                df[num_cols_present] = scaler.transform(df[num_cols_present])
        else:
            print("Warning/Advertencia: scaler.pkl not found.")

        return df

    except Exception as e:
        # Fallback to prevent app crashes / Respaldo para evitar caídas de la app
        print(f"Pipeline Error: {e}")
        return df

# --- Local Testing Block / Bloque de Pruebas Local ---
if __name__ == "__main__":
    #  Simulating HR input / Simulando la entrada de RRHH
    dummy_hr_data = {
        'Age': 34,
        'BusinessTravel': 'Travel_Rarely',
        'DailyRate': 628,
        'Department': 'Research & Development',
        'DistanceFromHome': 8,
        'Education': 3,
        'EducationField': 'Medical',
        'EnvironmentSatisfaction': 2,
        'Gender': 'Male',
        'HourlyRate': 82,
        'JobInvolvement': 4,
        'JobRole': 'Laboratory Technician',
        'JobSatisfaction': 3,
        'MaritalStatus': 'Married',
        'MonthlyIncome': 4000,
        'MonthlyRate': 12000,
        'NumCompaniesWorked': 2,
        'OverTime': 'Yes',
        'PercentSalaryHike': 14,
        'RelationshipSatisfaction': 1,
        'TrainingTimesLastYear': 3,
        'WorkLifeBalance': 2,
        'YearsAtCompany': 8,
        'YearsSinceLastPromotion': 1,
        'JobLevel': 2, 
        'TotalWorkingYears': 10
    }

    processed_df = clean_and_process(dummy_hr_data)
    print("\n--- 📊 Final DataFrame Ready for ML Model / DataFrame Final Listo ---")
    print(processed_df)