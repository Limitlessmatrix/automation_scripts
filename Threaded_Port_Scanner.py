""" 
Threaded Port Scanner for increasing efficiency
    As we have seen in the above cases, port scanning can be very slow. 
For example, you can see the time taken for scanning ports from 50 to 500, 
while using socket port scanner, is 452.3990001678467. 
To improve the speed we can use threading.

Following is an example of port scanner using threading − 
"""
import socket
import time
import threading

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', t_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = queue.Queue()

startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)

""" 
    In the above script, we need to import the threading module, which is inbuilt in the Python package. 
We are using the thread locking concept, 
thread_lock = threading.Lock() to avoid multiple modification at a time. 
Basically, threading.Lock() will allow single thread to access the variable at a time. 
Hence, no double modification occurs.

Later, we define one threader() function that will fetch the work (port) from the worker for loop. 
Then the portscan() method is called to connect to the port and print the result. 
The port number is passed as parameter. Once the task is completed the q.task_done() method is called.
Now after running the above script, we can see the difference in speed for scanning 50 to 500 ports.

It only took 1.3589999675750732 seconds, which is very less than 452.3990001678467, 
time taken by socket port scanner for scanning the same number of ports of localhost.
"""