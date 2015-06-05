"""
tx_chk.py
Something something.
!tx txid
"""
import requests
from util.hook import *

@hook(cmds="txchk", ex='tx txid', rate=15, args=True)
def txchk(code, input):
	"""Get tx details. example: !tx txid"""
	if len(input) == 0:
		return code.reply('No arguments supplied. !help txchk')
	query = 'https://chain.so/api/v2/is_tx_confirmed/DOGE/%s' % input
	try:
		response = requests.get(query)
		if reponse.status_code == 200:
			content = response.json()
			if content['data']['is_confirmed']:
				return code.reply("%r is {bold}{green}confirmed (confirmations: %d)" % (content['data']['txid'], content['data']['confirmations']))
			else:
				return code.reply("%r is {bold}{red}not confirmed" % (content['data']['txid']))
		else:
			return code.reply("You may have entered an incorrect txid. Try again?")
	except:
		return code.reply("An error occurred while fetching data. Try again?")