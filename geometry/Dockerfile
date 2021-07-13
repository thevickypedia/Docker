FROM python:3.8-slim

RUN mkdir /opt/geometry
COPY . /opt/geometry

RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install python-dotenv

WORKDIR /opt/geometry

ENTRYPOINT ["/usr/local/bin/python", "geometry.py"]
