import sys
import time
import NSERateModule
import MoneyControlRateModule
from datetime import datetime

stocks = []
stocks.append(
    { 'money-control-url' : "http://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/ricoauto/RA04", 'name' : 'RICO'}
)
stocks.append(
    { 'money-control-url' : "http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/gmrinfrastructure/GI27", 'name' : 'GMR'}
)
stocks.append(
    { 'money-control-url' : "http://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/relianceinfrastructure/RI38", 'name' : 'RELINFRA'}
)
stocks.append(
    { 'money-control-url' : "http://www.moneycontrol.com/india/stockpricequote/leather-products/bataindia/BI01", 'name' : 'BATAINDIA'}
)


def get_price_nse(stock):
    url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + stock.get('name')
    return NSERateModule.get_rate(url)


def get_price_money_control_stock(stock):
    url = stock.get('money-control-url')
    return MoneyControlRateModule.get_rate(url)


def get_price(stock,provider):
    if provider == 'nse':
        return get_price_nse(stock)
    return get_price_money_control_stock(stock)


def run(args):
    _pass = 0
    provider = sys.argv[1]
    if provider is None:
        provider = 'mc'
    while _pass < 7*60:
        t = str(datetime.now())
        for stock in stocks:
            rate = get_price(stock,provider)
            fd = open("data/"+stock.get('name')+"-NSE.dat","a")
            print stock.get('name') + "->" + str(rate)
            fd.write(t + "  " + str(rate) + "\n")
            fd.close()
            _pass = _pass + 1
        time.sleep(60)


if __name__ == "__main__":
    print sys.argv
    run(sys.argv)
