import json
import boto3

# Define the client to interact with AWS Lambda
client = boto3.client('lambda')
arn_dict = {
    "SVM": "arn:aws:lambda:us-east-1:742904401704:function:lambda_child_svm_v1",
    "RF": "arn:aws:lambda:us-east-1:742904401704:function:lambda_child_rf_v1",
    "XGB": "arn:aws:lambda:us-east-1:742904401704:function:lambda_child_xgb_v1",
}


def call_child(model_name, event):
    response = client.invoke(
        FunctionName=arn_dict[model_name],
        InvocationType="RequestResponse",
        Payload= json.dumps(event),
    )
    responseFromChild = json.load(response["Payload"])
    return responseFromChild


def handler(event, context):
    # Extract the features that will be passed
    # on to the child lambda function
    model_name = event["Model"]
    # Validate model name and return prediction for the model
    if model_name not in ["SVM", "RF", "XGB"]:
        return {"Invalid Model Name"}
    #Call the child lambda function
    response = call_child(model_name, event)
    return response

