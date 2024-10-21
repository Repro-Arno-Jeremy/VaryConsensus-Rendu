FROM python:3.12-alpine

WORKDIR /app

COPY runtime_parameter_approach.py /app
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

CMD ["python", "runtime_parameter_approach.py"]