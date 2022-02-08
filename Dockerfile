FROM python:3.9-slim

WORKDIR /opt/flask_course_project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python create_tables.py
RUN python load_fixtures.py
