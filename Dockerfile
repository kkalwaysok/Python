FROM python:3

WORKDIR /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install --upgrade werkzeug

CMD ["python", "./app.py"]