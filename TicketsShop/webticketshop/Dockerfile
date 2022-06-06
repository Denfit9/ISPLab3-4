FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirments.txt /app/requirments.txt
RUN pip install --upgrade pip && pip install -r requirments.txt
COPY . /app
EXPOSE 8000