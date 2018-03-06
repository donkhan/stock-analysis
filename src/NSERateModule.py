import requests
import re

token = "(lastPrice\":)(\")([0-9\.]+)(\")"
debug = False


def get_rate(url):
    r = re.search(token,requests.get(url).content).group(3)
    if debug :
        print "Current Rate " + str(r)
    return float(r)