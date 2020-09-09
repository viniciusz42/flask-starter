FROM python:3.7-alpine

COPY . /server
WORKDIR /server

RUN pip install gunicorn

RUN pip install -r requirements.txt

ENTRYPOINT [ "gunicorn", "-b 0.0.0.0:5000", "wsgi:server" ]
