import joblib

def load_model(path="models\\main_models\\xgboost_model.pkl"):
    model = joblib.load(path)
    return model
