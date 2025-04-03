FROM python:3.12.3

WORKDIR /app

RUN apt-get update
RUN apt-get install -y netcat-traditional

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["sh", "entrypoint.sh"]
