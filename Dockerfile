# set base image (host OS)
FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD gunicorn --worker-class gthread \
  --preload \
  --workers 1 \
  --threads 4 \
  --bind 0.0.0.0:8080 \
  --timeout 600 \
  wsgi:app
