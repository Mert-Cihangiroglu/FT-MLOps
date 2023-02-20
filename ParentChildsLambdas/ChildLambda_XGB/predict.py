import joblib
import xgboost as xgb
import numpy as np

# Load XGB Model from disk
model_xgb = xgb.Booster()
model_xgb.load_model('xgb.json')

# Feature names for XGB Input
FEATURE_NAMES= ['Mean_HT', 'Mean_PP', 'Mean_RR', 'Mean_RP', 'Std_HT', 'Std_PP', 'Std_RR', 'Std_RP']

def extract_features(event):
    # Extract features from event
    feature_values = [
        event["HT"]["Mean"],
        event["PPT"]["Mean"],
        event["RRT"]["Mean"],
        event["RPT"]["Mean"],
        event["HT"]["STD"],
        event["PPT"]["STD"],
        event["RRT"]["STD"],
        event["RPT"]["STD"]
    ]
    # return feature_values
    return feature_values


def handler(event, context):
    # Extract the features that will be passed
    feature_values = np.array(extract_features(event))
    # Transform the features into a DMatrix
    dmat = xgb.DMatrix(feature_values.reshape(1, -1), feature_names=FEATURE_NAMES)
    prediction = model_xgb.predict(dmat)
    prediction = int(prediction.argmax(axis=1)[0])
    
    return {
        'XGB': prediction
    }

