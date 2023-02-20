# Description: Test script 
import requests
import os
# ---------------------------------------------------------------------------------------------------- #
TEST_INPUT ={"Model": "RF","HT": {"Mean": 48.43,"STD": 23.34}, "PPT": { "Mean": 120.43, "STD": 37.41}, "RRT": {"Mean": 124.43,"STD": 45.34},  "RPT": {"Mean": 132.56, "STD": 47.12}}

URL_DOCKER = "http://localhost:8080/2015-03-31/functions/function/invocations"
URL_LAMBDA = "<URL_LAMBDA>"
# ---------------------------------------------------------------------------------------------------- #
# Send requests
docker_resp = requests.post(URL_DOCKER, json=TEST_INPUT).json()
#lambda_resp = requests.post(URL_LAMBDA, json=TEST_INPUT).json()
# ---------------------------------------------------------------------------------------------------- #
# Print results
print("--------------------")
print("Docker Child Response: ", docker_resp)
#print("Lambda Response: ", lambda_resp)
print("--------------------")
# ---------------------------------------------------------------------------------------------------- #
