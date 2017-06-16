#Juan Carlos Ramirez
#Crawls a web page for a list of all links referenced in the page

import argparse, re
from urllib2 import Request, urlopen, URLError
from pprint import pprint
parser = argparse.ArgumentParser(description="Crawls a web page for a list of all links referenced in the page")
parser.add_argument("-host", help="Specify a host", default="www.google.com")

args = parser.parse_args()

if args.host == "" or not args.host.startswith('http://'):
    print "Format of host is corrupt or needs http:// at the begginning"
    exit()

def remove_html_markup(s):
    out = re.findall("src=\"(.*?)\"",s)
    return out

try:
    response = urlopen(Request(args.host))
    pprint(remove_html_markup(response.read()))
except URLError, e:
    print "An error has occured, check the URL?", e
