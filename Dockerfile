FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y default-jdk && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY spark_app.py .
COPY tips.csv 

CMD ["spark-submit", "--master", "local[*]", "spark_app.py"]
