import pandas as pd
import os
import pickle
import joblib
import sklearn.preprocessing # Added this import to help with unpickling StandardScaler

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the input DataFrame by encoding categorical columns and scaling numerical columns.
    It loads pre-trained encoder and scaler models.
    """
    encode_model_load_dir = 'models/encoder_models'
    loaded_encoders = {}

    col_to_scale = ["Age", "DailyRate", "DistanceFromHome", "HourlyRate", "MonthlyRate", "TotalWorkingYears", "YearsAtCompany"]
    col_to_encode = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']

    # Encoding categorical columns
    for col_name in col_to_encode:
        filename = f'{col_name}_encoder.pkl'
        filepath = os.path.join(encode_model_load_dir, filename)

        try:
            if os.path.exists(filepath):
                with open(filepath, 'rb') as file:
                    loaded_encoder = pickle.load(file)
                    loaded_encoders[col_name] = loaded_encoder
            else:
                print(f"Warning: Encoder file for column '{col_name}' not found at '{filepath}'. Skipping encoding for this column.")
        except Exception as e:
            print(f"Error loading encoder for '{col_name}' from '{filepath}': {e}")

    for col_name, encoder_model in loaded_encoders.items():
        if col_name in df.columns:
            try:
                df[col_name] = encoder_model.transform(df[col_name])
            except ValueError as e:
                print(f"ValueError during encoding column '{col_name}': {e}")
            except Exception as e:
                print(f"Unexpected error during encoding column '{col_name}': {e}")
        else:
            print(f"Warning: Column '{col_name}' not found in DataFrame for encoding.")


    # Scaling numerical columns
    scaler = None
    scaler_filepath = "models/scaler_models/standard_scaler.pkl"

    try:
        scaler = joblib.load(scaler_filepath)
    except FileNotFoundError:
        print(f"Error: Scaler model not found at '{scaler_filepath}'. Skipping numerical scaling.")
    except Exception as e:
        print(f"Error loading scaler model from '{scaler_filepath}': {e}")

    if scaler:
        # Filter col_to_scale to only include columns present in the current DataFrame
        cols_to_scale_present = [col for col in col_to_scale if col in df.columns]

        if cols_to_scale_present:
            try:
                # Transform all relevant numerical columns at once
                df[cols_to_scale_present] = scaler.transform(df[cols_to_scale_present])
            except ValueError as e:
                print(f"ValueError during scaling multiple columns: {e}")
            except Exception as e:
                print(f"Unexpected error during scaling numerical columns: {e}")
        else:
            print("No numerical columns from 'col_to_scale' found in the DataFrame for scaling.")
    else:
        print("Numerical scaling skipped due to missing or unreadable scaler model.")

    return df
