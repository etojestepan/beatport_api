FROM python:3.12-slim
LABEL authors="stgal"
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . beatport
WORKDIR /beatport

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]