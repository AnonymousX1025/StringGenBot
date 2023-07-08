FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD bash start
