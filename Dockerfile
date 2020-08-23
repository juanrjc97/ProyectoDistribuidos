FROM python:3.8
ENV PYTHONUNBUFFERED 1
MAINTAINER juanj121297@gmail.com

RUN mkdir /backendApp
WORKDIR /backendApp
COPY requirements.txt /backendApp/

RUN pip3 install -r requirements.txt
COPY . /backendApp/





