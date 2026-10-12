FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y \
    curl \
    iproute2 \
    iputils-ping \
    net-tools && \
    rm -rf /var/lib/apt/lists/*

COPY victim.sh /victim.sh
RUN chmod +x /victim.sh

CMD ["/victim.sh"]