FROM public.ecr.aws/lambda/python:3.8
# Copy all the necessary files
COPY parent.py .
COPY requirements.txt .
# Install dependencies
RUN pip3 install -r requirements.txt --no-cache
CMD [ "parent.handler" ]