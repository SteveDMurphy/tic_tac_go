FROM python:3.8-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /tictac

WORKDIR /tictac/tictac

RUN pip install -e .
