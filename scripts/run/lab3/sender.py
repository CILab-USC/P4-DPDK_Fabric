from scapy.all import *
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="this script sends a packet to the specified host")

# Add arguments
parser.add_argument('-r', '--receiver', required=True, help="h1 or h2")
parser.add_argument('-ph', '--packet_header', required=True, help="eth or eth/ipv4 or eth/ipv4/tcp")

# Parse the arguments
args = parser.parse_args()

# Extract the arguments
receiver = args.receiver
packet_header = args.packet_header

# Print the result
print(f"Receiving host: {receiver}")
print(f"Packet headers: {packet_header}")


if receiver == 'h1':
    # Define the target IP address and port
    target_ip = '192.168.10.1'  # Replace with the actual target IP address
    target_mac = '00:00:00:00:00:01'  # Replace with the actual target MAC
    target_port = 80  # Replace with the actual target port
    # Define the network interface
    interface = 'dtap1'  # Replace with the actual network interface
elif receiver == 'h2':
    # Define the target IP address and port
    target_ip = '192.168.10.2'  # Replace with the actual target IP address
    target_mac = '00:00:00:00:00:02'  # Replace with the actual target MAC
    target_port = 80  # Replace with the actual target port
    # Define the network interface
    interface = 'dtap0'  # Replace with the actual network interface

    

if packet_header == 'eth':
    # Create an Ethernet frame and TCP packet
    packet_eth = Ether(dst=target_mac)
    # Send the packet_eth on the specified interface
    sendp(packet_eth, iface=interface)
elif packet_header == 'eth/ipv4':
    # Create an Ethernet frame and TCP packet
    packet_ipv4 = Ether(dst=target_mac) / IP(dst=target_ip, proto=17)
    # Send the packet_ipv4 on the specified interface
    sendp(packet_ipv4, iface=interface)
elif packet_header == 'eth/ipv4/tcp':
    # Create an Ethernet frame and TCP packet
    packet_tcp = Ether(dst=target_mac) / IP(dst=target_ip, proto=6)
    # Send the packet_tcp on the specified interface
    sendp(packet_tcp, iface=interface)