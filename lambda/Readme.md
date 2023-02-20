## MLOPS Challenge

This was a fast upront solution. Better (final) implementation is at [ParentChildsLambdas directory.](../ParentChildsLambdas)
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
</p>