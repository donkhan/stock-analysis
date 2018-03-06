import sys
import time
import NSERateModule
from datetime import datetime

stocks=[]
stocks.append("GMRINFRA")
stocks.append("RICOAUTO")
stocks.append("SUNPHARMA")
stocks.append("RELINFRA")
stocks.append("GLENMARK")

#https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=GMRINFRA


def main(args):
    _pass = 0
    while _pass < 7*60:
        t = str(datetime.now())
        for stock in stocks:
            url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock
            rate = NSERateModule.get_rate(url)
            fd = open("data/"+stock+"-NSE.dat","a")
            fd.write(t + "  " + str(rate) + "\n")
            fd.close()
            _pass = _pass + 1
        time.sleep(60)

if __name__ == "__main__":
    main(sys.argv)