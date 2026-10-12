from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP, Raw

VICTIM_IP = "10.30.0.20"
SERVER_IP = "10.30.0.30"
SERVER_PORT = 8080

# Same-length replacement avoids changing TCP payload length.
OLD = b"Lab-Token: original"
NEW = b"Lab-Token: ncyu_hacker"

def packet_callback(nfpacket):
    raw = nfpacket.get_payload()

    try:
        pkt = IP(raw)

        if not (pkt.haslayer(IP) and pkt.haslayer(TCP)):
            nfpacket.accept()
            return

        ip = pkt[IP]
        tcp = pkt[TCP]

        # Restrict changes to the intended lab traffic.
        if not (
            ip.src == VICTIM_IP
            and ip.dst == SERVER_IP
            and tcp.dport == SERVER_PORT
            and pkt.haslayer(Raw)
        ):
            nfpacket.accept()
            return

        #TODO: Modify only an exact header value already in this packet.

        nfpacket.accept()

    except Exception as exc:
        print(f"[MITM] Packet processing error: {exc}")
        # Fail open for this lab: preserve the original packet.
        nfpacket.accept()

nfqueue = NetfilterQueue()

try:
    nfqueue.bind(1, packet_callback)
    print("[MITM] Listening on NFQUEUE 1")
    nfqueue.run()
except KeyboardInterrupt:
    print("\n[MITM] Stopped")
finally:
    nfqueue.unbind()
