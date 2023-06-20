# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code

COPY requirements.txt /code
RUN pip3 install -r requirements.txt

COPY . /code

EXPOSE 8002

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8002" ]