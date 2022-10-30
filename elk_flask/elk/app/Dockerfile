FROM python:3.11-alpine

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--log-config", "gunicorn.conf"]