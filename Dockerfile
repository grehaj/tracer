FROM python:3.11-slim

ENV AUDIT_HOSTNAME=1.1.1.1
ENV AUDIT_USERNAME=client
ENV AUDIT_PASSWORD=client1

ENV TRACE_HOSTNAME=2.2.2.2
ENV TRACE_USERNAME=client
ENV TRACE_PASSWORD=client2

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