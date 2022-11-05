import argparse
from package.logger.logger import Logger
from package.ARP.ARPscan import ARPscan
from package.TCP.hostTCPscan import PortScanner
from package.OS.OSscan import OSscan
from package.PCAP.PCAP import PCAP

def main(logger):
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="method to use", choices=["ARP", "TCP", "OS", "PCAP","ARP+TCP"])
    args = parser.parse_args()
    if args.method == "ARP":
        arp = ARPscan()
        targertip= input("Enter the target IP address with subnetmask in format /24, /32: bv.192.168.0.1/24 ")
        detection_result=arp.detection_scan(targertip)
        arp_result_list=detection_result[0]
        logger.log(["ARP", arp_result_list,targertip])
        arp.result_printer(arp_result_list)

    elif args.method == "TCP":
        host = []
        while True:
            host.append(input("Enter the target IP address: "))
            if input("Do you want to add another IP address? (y/n) ") == "n":
                break
        scanner = PortScanner(host)
        result=scanner.scan()
        logger.log(["TCP", result,host])


    elif args.method == "OS":
        #requests worden geblokeerd door iets en werkt niet op windows wel op linux
        ip_adr = input("Enter the target IP address: ")
        osscan = OSscan(ip_adr)
        result = osscan.OSscan_result()
        logger.log(["OS", result,ip_adr])
    elif args.method == "PCAP":
        pcap=PCAP()
        pcap.pcap_sniffing()
        result=pcap.get_result()
        logger.log(["PCAP", result, ""])

    elif args.method == "ARP+TCP":
        arp = ARPscan()
        targertip= input("Enter the target IP address with subnetmask in format /24, /32: bv.192.168.0.1/24 ")
        detection_result=arp.detection_scan(targertip)
        arp_result_list=detection_result[0]
        IPlist=detection_result[1]
        arp.result_printer(arp_result_list)
        tcp = PortScanner(IPlist)
        result=tcp.scan()
        logger.log(["ARP+TCP", result,IPlist])

    else:
        print("Invalid method")


if __name__ == '__main__':
    logger = Logger('package/logger/log.csv', ["method","data,target IP"])
    #maakt een nieuwe logger aan met de naam log.csv en de header method dat kan oplossen door while loop te maken
    logger.log_header()
    main(logger)