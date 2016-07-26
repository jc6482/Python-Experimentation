#Juan Carlos Ramirez
#

import argparse
import socket
parser = argparse.ArgumentParser(description="Listens to an irc server/channel and stores the conversation...")
parser.add_argument("-host", help="Specify a host or else we will do local", default="localhost")
parser.add_argument("-port", help="Specify a host or else we will use 6667", type=int,  default=6667)

args = parser.parse_args()

def runSystem():

    host = args.host
    port = args.port




runSystem()
