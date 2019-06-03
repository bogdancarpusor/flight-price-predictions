FROM python:3
WORKDIR /app
COPY ./api /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]


