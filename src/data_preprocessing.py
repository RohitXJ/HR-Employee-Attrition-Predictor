import pandas as pd
import os
import pickle
import joblib

def process_data(df:pd.DataFrame) -> pd.DataFrame:
    """

    """
    if not df:
        return []
    encode_model_load_dir = 'model\encoder_models'
    loaded_encoders = {}

    col_to_scale = ["Age","DailyRate","DistanceFromHome","HourlyRate","MonthlyRate","TotalWorkingYears","YearsAtCompany"]
    col_to_encode = ['BusinessTravel', 'Department', 'EducationField', 'Gender','JobRole', 'MaritalStatus', 'OverTime']
    # Encoding categorical columns
    try:
        for col_name in col_to_encode:
            filename = f'{col_name}_encoder.pkl'
            filepath = os.path.join(encode_model_load_dir, filename)
            
            if os.path.exists(filepath): # Check if the specific file exists
                with open(filepath, 'rb') as file:
                    loaded_encoder = pickle.load(file)
                    loaded_encoders[col_name] = loaded_encoder
            else:
                print(f"Warning: Encoder file for column '{col_name}' not found at '{filepath}'.")

    except FileNotFoundError:
        pass
    except Exception:
        pass
    
    for col_name, encoder_model in loaded_encoders.items():
        if col_name in df.columns:
            try:
                df[col_name] = encoder_model.transform(df[col_name])
            except ValueError:
                pass
        else:
            pass


    # Scaling numerical columns

    try:
        scaler = joblib.load("models\scaler_model\standard_scaler.pkl")
    except FileNotFoundError:
        print("Scaler model not found. Please ensure the scaler model is available.")
        pass

    for col_name in col_to_scale:
        if col_name in df.columns:
            try:
                df[col_name] = scaler.transform(df[[col_name]])
            except ValueError:
                pass
        else:
            pass

    return df

print("Data preprocessing Test ",process_data(pd.DataFrame()))


