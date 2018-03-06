import requests
import re

token = "(lastPrice\":)(\")([0-9\.]+)(\")"
debug = False


def dig_rate(content):
    reg_ex = re.search(token, content)
    if reg_ex is not None:
        r = reg_ex.group(3)
        return float(r)
    return -1

def from_file():
    fd = open("/tmp/c.html")
    content = fd.read()
    print dig_rate(content)


def get_rate(url):
    print url
    content = requests.get(url).content
    content = str(content)
    r = dig_rate(content)
    print r
    return r

stock = "RICOAUTO"
url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock
print  get_rate(url)
#from_file()