FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y \
    curl \
    iproute2 \
    iputils-ping \
    net-tools  \ 
    python3 && \
    rm -rf /var/lib/apt/lists/*

COPY victim.py /victim.py

CMD ["python3", "/victim.py"]