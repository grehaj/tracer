FROM python:3.11-slim

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-warn-script-location -r requirements.txt

COPY main.py .
COPY audit audit
COPY cli cli
COPY config config
COPY ssh ssh
COPY trace trace

ENTRYPOINT ["python", "main.py"]