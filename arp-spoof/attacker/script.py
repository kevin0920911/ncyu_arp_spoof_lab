from scapy.all import *
import re
import sys
import threading
import time


conf.debug_match = 0     
conf.debug_dissector = 0 
conf.verb = 0            

VICTIM_IP = "10.10.0.20"
SERVER_IP = "10.10.0.30"

VICTIM_MAC = "00:00:00:00:00:20"
SERVER_MAC = "00:00:00:00:00:30"

def arp_poison(victim_ip, victim_mac, server_ip, server_mac):
    # TODO: Implement ARP poisoning logic here
    pass

def packet_callback(packet):
    if packet.haslayer(Raw):
        data = packet[Raw].load.decode(errors="ignore")

        match = re.search(r"FLAG\{[^}]+\}", data)

        if match:
            print(f"\n[FLAG] {match.group(0)}\n")

if __name__ == "__main__":
    try:
        print("Starting ARP poisoning...")
        threading.Thread(
            target=lambda: arp_poison(VICTIM_IP, VICTIM_MAC, SERVER_IP, SERVER_MAC),
            daemon=True
        ).start()

        # check if the flag is in the packet payload
        sniff(
            iface="eth0",
            prn=packet_callback,
            filter=f"tcp and (host {VICTIM_IP} or host {SERVER_IP})",
            store=0
        )
    except KeyboardInterrupt:
        print("\nStopping ARP poisoning...")
        sys.exit(0)