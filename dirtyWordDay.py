#Juan Carlos Ramirez
#What do you think this does? Doesn't compliment your mother.
#Add to your startup script for maximum effect....
from urllib2 import Request, urlopen, URLError
import string
import random
import argparse

parser = argparse.ArgumentParser(description="Dirty words to tell your lover...or enemies I get them confused")
parser.add_argument("-noSarcasm", action="store_true",  help="no phrasing before the word")
args = parser.parse_args()

def runSystem():
    try:
        response = urlopen(Request("https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"))
        sarcasm = ""
        dirtyWords = string.split(response.read(),"\n")
        if(not args.noSarcasm):
                sarcasm="Your dank word of the day: "
        

        print sarcasm + dirtyWords[random.randint(0,len(dirtyWords))]
    except URLError,e:
            print "An error has occured, check the URL?", e
    



runSystem()
