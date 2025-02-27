FROM python:3.8.5

WORKDIR /code

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /code

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
ARG DJANGO_ENV=settings
ENV DJANGO_SETTINGS_MODULE=api_yamdb.${DJANGO_ENV}