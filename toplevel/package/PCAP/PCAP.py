from scapy.layers.http import HTTPRequest
from scapy.all import  IP,sniff

class PCAP:
    def __init__(self):
        self.result = []

    def pcap_sniffing(self):
        # Set limit to 100 packets
        sniff(filter="tcp port 80", prn=self.process_packet,count=100)

    def process_packet(self,packet):
        if packet.haslayer(HTTPRequest):
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            ip = packet[IP].src
            method = packet[HTTPRequest].Method.decode()
            self.result.append(f"[+] {ip} Requested {url} with {method}")

    def get_result(self):
        return self.result
if __name__ == "__main__":
    pcap=PCAP()
    pcap.pcap_sniffing()


