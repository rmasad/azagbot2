from plugins import math
from plugins import flood

def main(name, msg, user, advice, channel, irc):
	math.main(msg, channel, irc)
	flood.main(msg, channel, name, irc)
