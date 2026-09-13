FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y \
    iproute2 \
    iputils-ping \
    tcpdump && \
    net-tools && \
    rm -rf /var/lib/apt/lists/*

RUN pip install scapy
COPY ./script.py /

CMD ["sleep", "infinity"]