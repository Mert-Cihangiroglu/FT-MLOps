This is our Parent Lambda:

    1- It receives the payload
    2- Checks if the called model is valid
    3- Checks if the features are valid
    4- if second and third points pass, it calls the correct lambda function
    5- It redirects the child lambda response to AWS API GATEWAY
