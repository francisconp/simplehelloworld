FROM iron/python:2.7
MAINTAINER Franciscon Santos - francisconp@gmail.com
RUN apk update
RUN apk add py-pip gcc python-dev musl-dev libffi-dev openssl-dev
RUN rm -rf /var/cache/apk/*
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
COPY simplehelloworld.py /app/simplehelloworld.py
EXPOSE 80
ENTRYPOINT python /app/simplehelloworld.py
