#Juan Carlos Ramirez
#Port Scanner for remote hosts
import argparse, socket, sys
from datetime import datetime
parser = argparse.ArgumentParser(description="Scan's the ports on a specific target")
parser.add_argument("-t", default="",  help="Name of the target")
parser.add_argument("-i", default="",  help="IP of the target")
parser.add_argument("-minPort", default=1, type=int, help="Name of the target")
parser.add_argument("-maxPort", default=65535, type=int,  help="IP of the target")
args = parser.parse_args()

if(args.t == "" and args.i == ""):
    sys.exit(parser.print_help())

if(args.i == ""):
    remoteServer = socket.gethostbyname(args.t)
else:
    remoteServer = socket.gethostbyname(args.i)


print "~" * 80
print "Scanning ", remoteServer, " please hold on"
print "~" * 80

startTime = datetime.now()

try:
    for port in range(args.minPort,args.maxPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServer,port))
        if result == 0:
            print "Port {}:     Open".format(port)
        sock.close()

except socket.gaierror:
    sys.exit(remoteServer, " could not be resolved. Exiting now")

except socket.error:
    sys.exit("Couldn't connect to ", remoteServer)

stopTime = datetime.now()

elapsedTime = stopTime - startTime

print "Scanning competed in: ", elapsedTime