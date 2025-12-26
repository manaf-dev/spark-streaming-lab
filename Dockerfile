FROM apache/spark:4.1.0-scala2.13-java21-python3-r-ubuntu

RUN mkdir -p /streaming/spark/jars /streaming/spark/checkpoints

WORKDIR /streaming/app

COPY requirements.txt .

RUN apt update && apt upgrade -y && \
    wget https://jdbc.postgresql.org/download/postgresql-42.7.6.jar && \
    pip3 install --no-cache-dir -r requirements.txt

RUN mv postgresql-42.7.6.jar /streaming/spark/jarspostgresql-42.7.6.jar && \

COPY . /streaming/app

EXPOSE 8080

