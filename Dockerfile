FROM python:3.8-bullseye

RUN pip install pipenv

WORKDIR /app

ADD Pipfile* .

RUN pipenv install

ADD . .

RUN cd infra && pipenv run python manage.py collectstatic

ENTRYPOINT cd infra && pipenv run gunicorn infra.wsgi:application -b 0.0.0.0:8000 --log-file - --access-logfile -
