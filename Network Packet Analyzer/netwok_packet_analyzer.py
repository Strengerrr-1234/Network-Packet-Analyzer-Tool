import scapy.all as scapy

# Define a function to capture and analyze packets
def packet_sniffer(packet):
    # Extract relevant information from the packet
    src_ip = packet[scapy.IP].src
    dst_ip = packet[scapy.IP].dst
    protocol = packet[scapy.IP].proto
    payload = packet[scapy.Raw].load

    # Print the extracted information
    print("Source IP:", src_ip)
    print("Destination IP:", dst_ip)
    print("Protocol:", protocol)
    print("Payload:", payload)

# Define a function to start the packet sniffer
def start_sniffer(iface):
    print("Starting packet sniffer on interface", iface)
    scapy.sniff(iface=iface, prn=packet_sniffer)

# Main function
if __name__ == "__main__":
    iface = input("Enter the interface to sniff (e.g., eth0, wlan0): ")
    start_sniffer(iface)