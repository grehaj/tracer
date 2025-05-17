FROM python:3.11-slim

ENV HOSTNAME=1.1.1.1
ENV USERNAME=aaa
ENV PASSWORD=bbb

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY audit audit
COPY cli cli
COPY config config
COPY ssh ssh
COPY trace trace

ENTRYPOINT ["python", "main.py"]