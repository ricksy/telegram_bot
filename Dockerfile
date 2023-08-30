FROM python:3.11.5
ENV TZ Europe/Berlin
ADD bot1.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","bot1.py"] 
# Or enter the name of your unique directory and parameter set.
