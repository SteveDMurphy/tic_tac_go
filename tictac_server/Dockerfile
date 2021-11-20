FROM python:3.8-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /tictac_server

WORKDIR /tictac_server/tictac_server
