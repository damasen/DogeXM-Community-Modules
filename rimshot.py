from util.hook import *

@hook(cmds="rimshot", rate=15)
def rimshot(code, input):
	return code.say("ba dum tss")
