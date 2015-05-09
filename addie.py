from util.hook import *
import urllib2

# addie.py
#
# Fetches crypto addresses from addie.cc
#
# Version: 2.0

@hook(cmds=["addie"], ex="addie cr5315 doge", rate=15)
def addie(code, input):
    """addic.cc address fetcher - use !addie username coin ex. !addie cr5315 doge"""
    try:
        args = input.group(2).split()
    except:
        args = []

    if len(args) == 0:
        user = input.nick
        coin = "doge"
    elif len(args) == 1:
        user = args[0]
        coin = "doge"
    elif len(args) >= 2:
        user = args[0]
        coin = args[1]
    else:
        return code.reply("{red}{b}Invalid usage. Use %shelp addie" % code.prefix)

    query = "http://addie.cc/api/%s/%s" % (user, coin)

    try:
        response = urllib2.urlopen(query)
        address = response.read()

        if len(address) > 0:
            return code.say("The %s address for %s is %s" % (coin.upper(), user, address))
        else:
            return code.reply("There was an error fetching the address. Do you have an account on addie.cc?")
    except:
        return code.reply("There was an error fetching the address. Do you have an account on addie.cc?")