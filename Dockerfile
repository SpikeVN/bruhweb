# syntax=docker/dockerfile:1

FROM python:3.10.9-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt install nodejs npm
COPY . .
CMD [ "sh", "run.sh"]
