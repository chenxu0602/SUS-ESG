FROM python:3

RUN apt-get update && apt-get -y install netcat && apt-get clean

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.sh ./
COPY main.py ./
COPY templates ./templates
COPY static ./static

RUN chmod +x ./run.sh

CMD ["./run.sh"]
