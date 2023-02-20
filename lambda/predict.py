import os
import joblib
import xgboost as xgb
import numpy as np

def load_rf_model():
    model = joblib.load('rf.pkl')
    return model

def load_xgb_model():
    model_xgb = xgb.Booster()
    model_xgb.load_model('xgb.json')
    # Return Feature Names for XGB Model
    return model_xgb, [
        "Mean_HT",
        "Mean_PP",
        "Mean_RR",
        "Mean_RP",
        "Std_HT",
        "Std_PP",
        "Std_RR",
        "Std_RP"
    ]

def load_svm_model():
    return joblib.load('svm.pkl')

def predictions_svm(feature_values):
    model_svm = load_svm_model()
    return int(model_svm.predict([feature_values]))

def predictions_rf(feature_values):
    model_rf = load_rf_model()
    proba = model_rf.predict_proba([feature_values])
    return int(proba.argmax(axis=1))

def predictions_xgb(feature_values):
    model_xgb, feature_names = load_xgb_model()
    feature_values = np.array(feature_values)
    dmat = xgb.DMatrix(feature_values.reshape(1, -1), feature_names=feature_names)
    predictions  = model_xgb.predict(dmat)
    return int(predictions.argmax(axis=1)[0])

def extract_features(event):
    # Validate model name
    input_dict = event
    # Extract features from input_dict
    feature_values = [
            input_dict["HT"]["Mean"],
            input_dict["PPT"]["Mean"],
            input_dict["RRT"]["Mean"],
            input_dict["RPT"]["Mean"],
            input_dict["HT"]["STD"],
            input_dict["PPT"]["STD"],
            input_dict["RRT"]["STD"],
            input_dict["RPT"]["STD"]
    ]
    return feature_values

def handler(event, context):
    # Extract model name and feature values from input
    model_name = event["Model"]
    feature_values = extract_features(event)
    if model_name not in ["SVM", "RF", "XGB"]:
        return {"Invalid Model Name"}
    if model_name == "SVM":
        prediction = predictions_svm(feature_values)
    elif model_name == "RF":
        prediction = predictions_rf(feature_values)
    elif model_name == "XGB":
        prediction = predictions_xgb(feature_values)

    return {
            "Model's User Prediction": prediction
            }