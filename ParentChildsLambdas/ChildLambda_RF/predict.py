import joblib
import numpy as np
import sklearn

#Load model
model = joblib.load('rf.pkl')

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
    #Extract features
    feature_values = extract_features(event)
    #Predict
    proba = model.predict_proba([feature_values])
    prediction = int(proba.argmax(axis=1))
    return {
        "Random Forest": prediction
    }
