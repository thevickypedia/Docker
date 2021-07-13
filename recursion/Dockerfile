FROM python:3.8-slim

ENV shutter="Vignesh" \
    number="v1gn35H"

RUN mkdir /opt/recursion
COPY . /opt/recursion

WORKDIR /opt/recursion

ENTRYPOINT ["/usr/local/bin/python", "recursion.py"]
