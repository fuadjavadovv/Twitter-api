FROM python:3.9-alpine

WORKDIR /myapp

RUN python3 -m pip install --upgrade pip
COPY . .
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["sh", "/myapp/setup.sh"]

