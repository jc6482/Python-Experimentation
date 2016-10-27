#Juan Carlos Ramirez
#This is a sample script
import sys
import time
from urllib2 import Request, urlopen, URLError
def runSystem():
    print "Starting up"
    stall(3)
    print "."
    print "Finished!"

    if len(sys.argv) == 1:
        print "Please specify a url: python practice.py www.yoururl"
        return
    print "Reading "  + sys.argv[1]
    stall(3)
    try:
        response = urlopen(Request(sys.argv[1]))
        
        print remove_html_markup(response.read())
    except URLError,e:
            print "An error has occured, check the URL?", e
    

    print "Unloading HTTP connection"
    stall(3)
    print "Finished!"

def stall(timer):
    
    while timer != 0:
        timer = timer - 1
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(timer)
def remove_html_markup(s):
        tag = False
        quote = False
        out = ""

        for c in s:
           if c == '<' and not quote:
                tag = True
           elif c == '>' and not quote:
               tag = False
           elif (c == '"' or c == "'") and tag:
              quote = not quote
           elif not tag:
              out = out + c
        return out

runSystem()
