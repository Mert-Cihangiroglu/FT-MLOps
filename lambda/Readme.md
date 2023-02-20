## MLOPS Challenge

This was a fast upront solution. Better (final) implementation is at [ParentChildsLambdas directory.](../ParentChildsLambdas)
<br>
<br>
<p>------------------------------------------------------------</p>
REST API lambda 1: https://oa3luyp1hf.execute-api.us-east-1.amazonaws.com/Dev_v1
<p>
Cold Start:
<ul>
    <li>Container for the function is initialized. This process takes some time, for the first Invoke the time range is between 8 seconds to 12 seconds.</li>
</ul>
Subsequent requests:
<ul>
    <li>Subsequent requests takes approximetely 20-30 ms.</li>
</ul>
</p>
<p>
Pros of this lambda:
<ul>
    <li>Very straightforward and complexity is low.</li>
</ul>
Cons of this lambda:
<ul>
    <li>Initialization of the function takes long.</li>
    <li>Adding new models to workflow requires creating the image and lambda function from start.</li>
</ul>
What can be done?
<ul>
    <li>
    Create 4 lambda functions:
    1- Parent Lambda
    2- ChildLambdaRF
    3- ChildLambdSVM
    4- ChildLambdaXGB
    You can find the implementation of this lambda functions in ParentChildsLambdas folder.
    </li>


</ul>
</p>