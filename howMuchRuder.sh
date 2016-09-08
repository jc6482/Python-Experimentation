#!/bin/sh
user=$1
terminal=$2
while [ 1 ]; do echo "$(python dirtyWordDay.py -noSarcasm)" | write $user $terminal; done
