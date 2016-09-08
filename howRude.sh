#!/bin/sh
user=$1
terminal=$2
while [[ 1 ]]; do echo "$(python spiral.py -width 50)" | write $user $terminal; done
