#  Network Packet Analyzer Tool


## Note: 

 This tool is intended for educational purposes only. It is essential to use this tool in compliance with applicable laws and regulations. Unauthorized capture and analysis of network packets without permission is illegal.

## Requirements:

Python 3.x

scapy library (install using `pip install scapy`)

## Explanation:

1. The packet_sniffer function takes a packet as input and extracts   the source and destination IP addresses, protocol, and payload data using Scapy's packet parsing capabilities.

2. The extracted information is printed to the console.

3. The `start_sniffer` function starts the packet sniffer on the specified interface using Scapy's `sniff` function.

4. The `prn` parameter specifies the function to call for each captured packet, which in this case is the packet_sniffer function.


## Example Use Case:

1. Save the code in a file named `packet_sniffer.py`.

2. Run the script using python `packet_sniffer.py`.

3. Enter the interface to sniff (e.g., `eth0` or `wlan0`) when prompted.

4. The packet sniffer will start capturing and analyzing packets on the specified interface.

5. Press `Ctrl+C`. to stop the packet sniffer.