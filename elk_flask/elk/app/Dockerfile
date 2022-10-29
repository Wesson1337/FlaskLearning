FROM python:3.11-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--log-config", "gunicorn.conf"]