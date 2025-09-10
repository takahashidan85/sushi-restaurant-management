FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app_factory.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
