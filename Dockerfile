FROM python:3-slim

COPY ninjadisplay /app/ninjadisplay
ADD requirements.txt /app
WORKDIR /app
RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]
CMD ["gunicorn", "ninjadisplay:app", "--preload", "-b", "0.0.0.0:8000"]
