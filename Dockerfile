FROM python:3.11.5
ADD bot1.py .
ADD requirements.txt .
ADD resources ./resources/
RUN pip install -r requirements.txt
CMD ["python","bot1.py", "hello from docker"] 
# Or enter the name of your unique directory and parameter set.
