FROM python:3.8.13-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD flask run --port 8080 --host=0.0.0.0
