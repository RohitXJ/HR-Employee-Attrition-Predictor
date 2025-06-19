import xgboost

def load_model(path="models/main_model/xgboost_model.json"):
    model = xgboost.XGBClassifier()
    model.load_model(path)
    return model

load_model()