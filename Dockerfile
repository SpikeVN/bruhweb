# syntax=docker/dockerfile:1

FROM python:3.10.9-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt install -y nodejs
COPY . .
RUN chmod +x run.sh
CMD [ "pc", "init", "&&", "pc", "run", "--env", "prod"]
