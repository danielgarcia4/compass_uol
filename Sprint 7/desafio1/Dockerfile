FROM python:3.8

WORKDIR /app

COPY script.py .
COPY movies.csv .
COPY series.csv .

RUN pip install boto3

CMD ["python", "script.py"]