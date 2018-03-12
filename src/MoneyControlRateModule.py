import requests
import re
token = "(Nse_Prc)(.*)(strong)(\")"


def get_rate(url):
    content =  requests.get(url).content
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("<div  id=\"Nse_Prc_tick_div\""):
            line = line.rsplit("<strong>")[1]
            line = line.split("</strong>")[0]
            return float(line)

print get_rate("http://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/ricoauto/RA04")
