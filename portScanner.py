# Juan Carlos Ramirez
# Port Scanner for remote hosts
import argparse
import socket
import struct
import sys
import threading
import queue
from datetime import datetime

parser = argparse.ArgumentParser( description="Scan's the ports on a specific target")
parser.add_argument("-t", default="",  help="Name of the target")
parser.add_argument("-i", default="",  help="IP of the target")
parser.add_argument("-minPort", default=1, type=int, help="Name of the target")
parser.add_argument("-maxPort", default=65535,
                    type=int,  help="IP of the target")
parser.add_argument("-c", action='store_true',  help="Show Closed Ports")
args = parser.parse_args()

if(args.t == "" and args.i == ""):
    sys.exit(parser.print_help())

if(args.i == ""):
    remoteServer = socket.gethostbyname(args.t)
else:
    remoteServer = socket.gethostbyname(args.i)

def tcpScan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.pack("ii", 1, 0))
        sock.settimeout(timeout)

        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        else:
            if args.c:
                print("Port {}:     Closed/Blocked".format(port))
        sock.close()

    except socket.gaierror:
        sys.exit(host, " could not be resolved. Exiting now")

    except socket.error:
        sys.exit("Couldn't connect to ", host)


timeout = .1

print("~" * 80)
print("Scanning ", remoteServer, " please hold on")
print("~" * 80)

startTime = datetime.now()


def multi_threader_tcp():
    while True:
        host_port = q.get()
        host = host_port[0]
        port = host_port[1]
        tcpScan(host,port)
        q.task_done()

q = queue.Queue()

for x in range(30):
    t = threading.Thread(target=multi_threader_tcp)
    t.daemon = True
    t.start()

for port in range(args.minPort, args.maxPort):
    q.put((remoteServer,port))

q.join()


stopTime = datetime.now()

elapsedTime = stopTime - startTime

print("Scanning competed in: ", elapsedTime)
