FROM iron/python:2.7
MAINTAINER Franciscon Santos - francisconp@gmail.com
RUN groupadd grpsvc && useradd -g grpsvc svc-user
RUN apk update
RUN apk add py-pip gcc python-dev musl-dev libffi-dev openssl-dev
RUN rm -rf /var/cache/apk/*
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
COPY src /app/
USER svc-user
ENTRYPOINT python /app/simplehelloworld.py
