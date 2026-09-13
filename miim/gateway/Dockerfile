FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y \
    iproute2 \
    iputils-ping \
    net-tools && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]