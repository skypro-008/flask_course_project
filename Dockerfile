FROM python:3.9-alpine3.14
MAINTAINER Vadim Mescheryakov <painassasin@icloud.com>

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    FLASK_ENV=production \
    PROJECT_DIR=/opt/backend

RUN adduser -D user

RUN apk update; \
    apk add --no-cache libpq; \
    apk add --no-cache --virtual .build-deps gcc postgresql-dev python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip; \
    pip install --no-cache-dir -r requirements.txt; \
    apk del .build-deps

WORKDIR $PROJECT_DIR

COPY . .
RUN chown user:user -R ${PROJECT_DIR}; \
    chmod 755 -R ${PROJECT_DIR}; \
    chmod +x ${PROJECT_DIR}/entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]
EXPOSE 5000
