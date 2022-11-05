# Opdracht week 4
## Install requriments
## Methods
### ARP
Host detection
### TCP
Port scan (can take a while) range port 1-1024
### OS
OS detection
### PCAP
PCAP analysis
### TCP+ARP
TCP+ARP scan (can take a while) range port 1-1024

## How to use scapy (main.py)
### ARP
Host detection
Go to folder toplevel
Run python ./main.py ARP or python.exe ./main.py ARP
Enter  correct the ip (range) address and the subnetmask
### TCP
Port scan (can take a while) range port 1-1024
Go to folder toplevel
Run python ./main.py TCP or python.exe ./main.py TCP
Enter  correct the ip address then you can choose to add another ip address or not (y/n)

### OS
Create foder (/var/run/p0f/)
OS detection
Go to folder toplevel
Run python ./main.py OS or python.exe ./main.py OS
Enter  correct target ip address

### PCAP
PCAP analysis
Go to folder toplevel
Run python ./main.py PCAP or python.exe ./main.py PCAP
PCAP scan can now get only HTTP traffic

### TCP+ARP
TCP+ARP scan (can take a while) range port 1-1024
Go to folder toplevel
Run python ./main.py TCP+ARP or python.exe ./main.py TCP+ARP
Enter  correct the ip (range) address and the subnetmask

### Logger
Logger
There is a logger in the package/logger
The logger is used to log the output of the scapy scripts

## For each method there is a folder with the same name
You can run the script in the folder with the same name
