import random
from scapy.all import  IP, sr1, TCP, sr

class PortScanner:
    def __init__(self, hosts):
        self.hosts = hosts


    def scan(self):
        result = []
        for host in self.hosts:
            for dst_port in range(1025):
                src_port = random.randint(1025,65534)
                resp = sr1(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
                    verbose=0,
                )

                if resp is None:
                    #if response is None
                    continue
                elif(resp.haslayer(TCP)):
                    if(resp.getlayer(TCP).flags == 0x12):
                        #send closing request
                        send_rst = sr(
                            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                            timeout=1,
                            verbose=0,
                        )
                        result.append({'IP': host, 'Port': dst_port, 'Status': 'Open'})
                else:
                    continue
        return result

if __name__ == "__main__":
    host = []
    scanner = PortScanner(host)
    scanner.scan()