FROM python:3.6-alpine
WORKDIR /app
COPY . /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install psycopg2 && pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["main.py"]


