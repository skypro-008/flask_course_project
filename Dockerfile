FROM python:3.9-slim

WORKDIR /opt/flask_course_project

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off
ENV FLASK_APP=run.py

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
      libpq-dev \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install -r requirements.txt


COPY *.py .
COPY fixtures.json .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]
