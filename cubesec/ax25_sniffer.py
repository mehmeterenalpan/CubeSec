from scapy.all import sniff, Raw
from binascii import hexlify
import logging

def ax25_sniffer(interface='lo', count=10):
    def packet_callback(packet):
        if Raw in packet:
            raw_data = packet[Raw].load
            logging.info(f"AX.25 Packet: {hexlify(raw_data)}")

    logging.info("Starting AX.25 packet sniffing...")
    sniff(iface=interface, prn=packet_callback, count=count)
