FROM python:alpine

COPY personal_shopper /app
WORKDIR /app

RUN apk add --no-cache build-base postgresql-dev
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:3000
