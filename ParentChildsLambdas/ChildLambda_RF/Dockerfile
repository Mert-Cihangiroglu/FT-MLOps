FROM public.ecr.aws/lambda/python:3.8

# Copy necesssary files
COPY requirements.txt .
COPY predict.py .
COPY rf.pkl .

# Install dependencies
RUN pip3 install -r requirements.txt --no-cache
CMD [ "predict.handler" ]