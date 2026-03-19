FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask mysql-connector-python

EXPOSE 8080

CMD ["python", "http_serv.py"]
