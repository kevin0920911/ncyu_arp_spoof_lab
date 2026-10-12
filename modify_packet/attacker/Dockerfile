FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y \
    gcc \
    g++ \
    make \
    python3-dev \
    libnetfilter-queue-dev \
    iproute2 \
    iputils-ping \
    tcpdump  \
    vim \
    iptables \ 
    net-tools && \
    rm -rf /var/lib/apt/lists/*

RUN pip install scapy NetfilterQueue
COPY ./arp_script.py /
COPY ./modify_script.py /


CMD ["sleep", "infinity"]