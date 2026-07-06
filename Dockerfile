FROM python:3.9-slim-bookworm

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Spark_app.py .
COPY tips.csv .

CMD ["spark-submit", "--master", "local[*]", "Spark_app.py"]
