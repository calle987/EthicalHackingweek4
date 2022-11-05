from scapy.all import ARP, Ether, srp
class ARPscan:
    def __init__(self):
        self.result = []

    def detection_scan(self, ip_adr):
        try:
            arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_adr)
            answers, unanswers = srp(arp_request, timeout=3, retry=2)
            result = []
            IPlist=[]
            for sent, received in answers:
                result.append({' [+] IP adress': received.psrc, ' converted MAC adress': received.hwsrc})
                IPlist.append(received.psrc)

            return result,IPlist
        except:
            print("Invalid IP address or subnetmask")

    def get_result(self):
        return self.result
    def result_printer(self,resultlist):
        for result in resultlist:
            print(result)

if __name__ == "__main__":
    arp = ARPscan()
    detection_result=arp.detection_scan("ip/subnetmask")
    arp_result_list=detection_result[0]
    IPlist=detection_result[1]
    arp.result_printer(arp_result_list)

