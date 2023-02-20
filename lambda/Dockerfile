FROM public.ecr.aws/lambda/python:3.8
# Copy all the necessary files
COPY predict.py .
COPY requirements.txt .
COPY xgb.json .
COPY svm.pkl .
COPY rf.pkl .

# Install dependencies
RUN pip3 install -r requirements.txt --no-cache
CMD [ "predict.handler" ]