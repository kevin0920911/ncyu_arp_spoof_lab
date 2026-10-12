FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y \
    curl \
    iproute2 \
    iputils-ping \
    net-tools 

WORKDIR /app

COPY server.py .

CMD ["python", "server.py"]