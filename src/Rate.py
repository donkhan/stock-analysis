import time
import sys
import NSERateModule

time_rate = []

simulated_rates = [573,577,582,587,584,594,600,595,593,591,590]
#simulated_rates = [82.9,82.7,82.85,82.9,82.8,83]
simulation = False
debug = True


def grep_rate(url,_pass):
    if simulation:
        return simulated_rates[_pass]
    return NSERateModule.get_rate(url)


def my_print(str):
    if debug:
        print str


def go_ahead(_pass):
    if simulation:
        return _pass < len(simulated_rates)
    return True


def reverse_buy_process(args):
    _pass = 0
    peak_rate = 0
    url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + args[2]
    quantity = int(args[3])
    buy_price = float(args[4])
    min_profit = float(args[5])
    peak_diff = float(args[6])
    sleep_time = float(args[7])

    while go_ahead(_pass):
        current_time = time.time()
        current_rate = grep_rate(url,_pass)
        if peak_rate < current_rate:
            peak_rate = current_rate
        if len(time_rate) > 0:
            prev_rate = time_rate[len(time_rate)-1][1]
            if current_rate - buy_price > min_profit:
                my_print("We are in Profit with rate as " + str(current_rate))
                if current_rate > prev_rate:
                    my_print(str(current_rate) + " is more than " + str(prev_rate) +  " so let me wait")
                else:
                    my_print("Dip starts with diff with peak " + str(peak_rate - current_rate)
                         + " Profit " + str(current_rate - buy_price))
                    if (peak_rate - current_rate) >= peak_diff and  current_rate - buy_price >= min_profit:
                        print("Wake up. This is the time to sell Current Rate is " + str(current_rate)
                              + "Peak Rate is " + str(peak_rate))
            else:
                print "we are not in profit as rate is " + str(current_rate)
        time_rate.append((current_time,current_rate))
        time.sleep(sleep_time)
        _pass = _pass + 1


def reverse_sell_process(args):
    _pass = 0
    dip_rate = 0
    url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=" + args[2]
    quantity = int(args[3])
    sell_price = float(args[4])
    min_profit = float(args[5])
    dip_diff = float(args[6])

    while go_ahead(_pass):
        current_time = time.time()
        current_rate = grep_rate(url,_pass)
        if dip_rate < current_rate:
            dip_rate = current_rate
        if len(time_rate) > 0:
            prev_rate = time_rate[len(time_rate)-1][1]
            if sell_price - current_rate > min_profit:
                my_print("We are in Profit with rate as " + str(current_rate))
                if current_rate < prev_rate:
                    my_print(str(current_rate) + " is less than " + str(prev_rate) +  " so let me wait")
                else:
                    my_print("Dip starts with diff with peak " + str(current_rate - dip_rate)
                         + " Profit " + str(sell_price - current_rate))
                    if (current_rate - dip_rate  ) >= dip_diff and  sell_price - current_rate  >= min_profit:
                        print("Wake up. This is the time to sell Current Rate is " + str(current_rate)
                          + " Dip Rate is " + str(dip_rate))
            else:
                print "we are not in profit as rate is " + str(current_rate)

        time_rate.append((current_time,current_rate))
        time.sleep(int(args[7]))
        _pass = _pass + 1


def main(args):
    if sys.argv[1] == 'B':
        reverse_buy_process(args)
    if sys.argv[1] == 'S':
        reverse_sell_process(args)


if __name__ == "__main__":
    if len(sys.argv) < 8:
        print "Usage Python Rate.py B/S Stock Quantity Price MinimumProfit PeekDiff PollingInterval(secs)"
        exit(-1)

    main(sys.argv)
    #print grep_rate("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=SUNPHARMA",1)