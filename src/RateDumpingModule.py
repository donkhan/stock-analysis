import sys
import time
import NSERateModule
import MoneyControlRateModule
from datetime import datetime

stocks=[]
stocks.append("GMRINFRA")
stocks.append("RICOAUTO")
#stocks.append("SUNPHARMA")
stocks.append("RELINFRA")
#stocks.append("TATAMOTORS")
stocks.append("BATAINDIA")
stocks.append("GLENMARK")
#stocks.append("ONGC")

mcstocks = []
mcstocks.append({ 'url' : "http://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/ricoauto/RA04", 'name' : 'RICO'})
mcstocks.append({ 'url' : "http://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/ricoauto/RA04", 'name' : 'RICO'})



#https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=GMRINFRA


def nse(args):
    _pass = 0
    while _pass < 7*60:
        t = str(datetime.now())
        for stock in mcstocks:
            url = stock.get('url')
            name = stock.get('name')
            rate = MoneyControlRateModule.get_rate(url)
            fd = open("data/"+name+"-NSE.dat","a")
            fd.write(t + "  " + str(rate) + "\n")
            fd.close()
            _pass = _pass + 1
        time.sleep(60)

def mc(args):
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
    nse(sys.argv)
