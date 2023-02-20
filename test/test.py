# Description: Test script 
import requests
import os
# ---------------------------------------------------------------------------------------------------- #
TEST_INPUT_RF ={"Model": "RF","HT": {"Mean": 48.43,"STD": 23.34}, "PPT": { "Mean": 120.43, "STD": 37.41}, "RRT": {"Mean": 124.43,"STD": 45.34},  "RPT": {"Mean": 132.56, "STD": 47.12}}
TEST_INPUT_SVM ={"Model": "SVM","HT": {"Mean": 48.43,"STD": 23.34}, "PPT": { "Mean": 120.43, "STD": 37.41}, "RRT": {"Mean": 124.43,"STD": 45.34},  "RPT": {"Mean": 132.56, "STD": 47.12}}
TEST_INPUT_XGB ={"Model": "XGB","HT": {"Mean": 48.43,"STD": 23.34}, "PPT": { "Mean": 120.43, "STD": 37.41}, "RRT": {"Mean": 124.43,"STD": 45.34},  "RPT": {"Mean": 132.56, "STD": 47.12}}

URL_DOCKER = "http://localhost:8080/2015-03-31/functions/function/invocations"
URL_LAMBDA = "https://9t3cvckvk0.execute-api.us-east-1.amazonaws.com/Dev_v1"
# ---------------------------------------------------------------------------------------------------- #
# Send requests
#docker_resp = requests.post(URL_DOCKER, json=TEST_INPUT).json()
lambda_resp_svm = requests.post(URL_LAMBDA, json=TEST_INPUT_SVM).json()
lambda_resp_rf = requests.post(URL_LAMBDA, json=TEST_INPUT_RF).json()
lambda_resp_xgb = requests.post(URL_LAMBDA, json=TEST_INPUT_XGB).json()
# ---------------------------------------------------------------------------------------------------- #
# Print results
print("--------------------")
#print("Docker Child Response: ", docker_resp)
print("Lambda Response for RF: ", lambda_resp_rf)
print("Lambda Response for SVM", lambda_resp_svm)
print("Lambda Response for XGB ", lambda_resp_xgb)
print("--------------------")
# ---------------------------------------------------------------------------------------------------- #
