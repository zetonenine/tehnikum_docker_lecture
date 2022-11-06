FROM python:3.8

COPY . /tehnikum
WORKDIR /tehnikum/
ENV PYTHONPATH .
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY *.py /app/
CMD ["python", "./app/main.py"]