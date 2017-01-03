#!/bin/python
#Juan Carlos Ramirez
#Calculates the experience required for the input level.

import sys
import argparse

parser = argparse.ArgumentParser(description = "Manages Level or Experience points based on D&D 3rd Edition")
parser.add_argument("-lvl",help="Level to calculate to",type=int, default=-1)
parser.add_argument("-exp",help="Calculate Level from Experience",type=int, default=-1)

args = parser.parse_args()

if(args.lvl >= 0):
    expNeeded = 0
    for x in range(1,args.lvl+1):
        expNeeded += ((x-1) * 1000)

    print("Required EXP: " + expNeeded.__str__())

if(args.exp >= 0):
    expNeeded = 0
    for x in range(1, 1000):
        expNeeded += ((x - 1) * 1000)
        if(expNeeded > args.exp):
             print("Level: " + (x-1).__str__())
             break
        

