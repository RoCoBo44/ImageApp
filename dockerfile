FROM python:3.9.1

ADD . /App
WORKDIR /App

ENV FLASK_APP App/app.py

RUN pip install -r App/requirements.txt