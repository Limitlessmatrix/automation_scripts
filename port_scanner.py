from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting to scan host:', t_IP)

    for i in range (50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
            s.close()
print('Time taken:', time.time() - startTime)
""" 
WARNING:
    When we run the above script, it will prompt for the hostname, you can provide any hostname like name of any website but be careful because port scanning can be seen as, or construed as, a crime. 
We should never execute a port scanner against any website or IP address without explicit, written permission from the owner of the server or computer that you are targeting. 
Port scanning is akin to going to someone’s house and checking their doors and windows. 
That is why it is advisable to use port scanner on localhost or your own website (if any). 
"""
""" Port Scanner using TCP scan
    To establish a TCP connection, the host must perform a three-way handshake. Follow these steps to perform the action −
Step 1 − Packet with SYN flag set
In this step, the system that is trying to initiate a connection starts with a packet that has the SYN flag set.
Step 2 − Packet with SYN-ACK flag set
In this step, the target system returns a packet with SYN and ACK flag sets.
Step 3 − Packet with ACK flag set
At last, the initiating system will return a packet to the original target system with the ACK flag set.
Nevertheless, the question that arises here is if we can do port scanning using ICMP echo request and reply method (ping sweep scanner) then why do we need TCP scan? 
The main reason behind it is that suppose if we turn off the ICMP ECHO reply feature or using a firewall to ICMP packets then ping sweep scanner will not work and we need TCP scan. 
"""

import socket
from datetime import datetime
net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         
run1()
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)

""" The above script works in three parts. 
It selects the range of IP address to ping sweep scan by splitting it into parts. 
This is followed by using a function for scanning the address, which further uses the socket. Later, it gives the response about the host and time taken for completing the scanning process. 
The result = s. connect_ex((addr,135)) statement returns an error indicator. 
The error indicator is 0 if the operation succeeds, otherwise, it is the value of the errno variable. Here, we used port 135; this scanner works for the Windows system. 
Another port which will work here is 445 (Microsoft-DSActive Directory) and is usually open. """