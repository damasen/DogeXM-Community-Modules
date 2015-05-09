from util.hook import *
import json
import os
import sys
import urllib2


__author__ = "cr5315"


HEADERS = {'User-Agent': 'Mozilla/5.0'}
URL = "https://www.cryptonator.com/api/ticker/%s-%s"


@hook(cmds=["convert"], args=True, rate=15)
def convert(code, input):
    try:
        args = input.group(2).split()
        amount = float(args[0])
        start = args[1]
        end = args[2]
    except IndexError:
        return code.reply("Invalid arguments: try something like %sconvert 5000 doge btc" % code.prefix)
    except ValueError:
        return code.reply("Invalid arguments: try something like %sconvert 5000 doge btc" % code.prefix)

    try:
        response = json.load(get(URL % (start.lower(), end.lower())))
    except Exception as e:
        with open("convert.txt", "a") as f:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            f.write("%s, %s, %s\n" % (exc_type, fname, exc_tb.tb_lineno))
        return code.reply("Network error.")

    if response["success"] is not True:
        return code.reply("Error: %s" % response["error"])

    price = response["ticker"]["price"]

    try:
        price = float(price)
    except ValueError:
        return code.reply("API error, please try again later.")

    value = price * amount

    return code.reply("%f %s = %f %s (Cryptonator)" % (amount, start.upper(), value, end.upper()))


def get(url, headers=HEADERS):
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request)