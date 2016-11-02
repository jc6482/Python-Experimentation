#!bin/
# Juan Carlos Ramirez
# Count's characters from input or a data file
import argparse
from operator import itemgetter

parser = argparse.ArgumentParser(description="Count occurrences of all characters in a string or file ")
parser.add_argument("-D", default="", help="Data to count occurences in")
parser.add_argument("-a", default=False, action="store_true", help="Sort in ascending")
parser.add_argument("-d", default=False, action="store_true", help="Sort in descending")

args = parser.parse_args()

if (args.D == ""):
    data = raw_input("Please enter the Test String: ")
else:
    dataFile = args.D
    open_file = open(dataFile)
    open_file.seek(0)
    data = open_file.read()

myMap  = {}

for i in range(0,data.__len__()):
    if data[i] in myMap:
        myMap[data[i]] = myMap[data[i]] + 1
    else:
        myMap[data[i]] = 1

if(args.a is True):
    myMap = sorted(myMap.items(),key=itemgetter(1),reverse=True)

if(args.d is True):
    myMap = sorted(myMap.items(),key=itemgetter(1),reverse=False)

for k,v in myMap:
    print(k,v)
