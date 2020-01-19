FROM python:3.6.4

EXPOSE 5000

RUN useradd republic

RUN pip install flask gunicorn requests

COPY /app /app

WORKDIR /app

ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--log-level=info", "--threads=1", "--workers=1", "--timeout=30"]
