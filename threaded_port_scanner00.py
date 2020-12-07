#port_Scanner try #2
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# def pscan(port):
#     try:
#         s.connect((server,port))
#         return True
#     except:
#         return False

# for x in range(1, 26):
#     if pscan(x):
#         print("Port",x, "is open..!")
#     else:
#         print("Port", x, "is closed")

#threaded
import threading
from queue import Queue
import time
import socket

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()

target = "limitlessmatrix.com"
ip = socket.gethostbyname(target)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port',port, "is open")
            con.close()
    except:
        pass
# The threader thread pulls an worker from the queue and process
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

# Creates the queue and threader 
q = Queue()

for x in range(30):
    
# how many threads are we going to allow for
    t =threading.Thread(target = threader)
# classifying as a daemon, so they will die when the main
    t.deamon = True
    
# begins, must come after daemon definition
    t.start()
# 100 jobs assigned.
for worker in range(1, 5001):
    q.put(worker)
# wait until the thread terminates.
q.join()