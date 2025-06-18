import pandas as pd
from src.data_preprocessing import process_data
from src.model_loader import load_model  

def predict_attrition(input_df: pd.DataFrame) -> str:
    """
    """

    processed_df = process_data(input_df)
    model = load_model()
    prediction = model.predict(processed_df)

    return prediction
