import socket
import logging
from time import ctime
import configparser





def kick(kicked, kicker, reason, channel, irc):
	IrcSend (irc, 'KICK {0} :{1}\r\n'.format(channel, kicked))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a KICK to {2} becouse {3} in the channel {4}".format(ctime(), kicker, kicked, reason, channel))


def ban(banned, banner, reason, channel, irc):
	IrcSend (irc, 'PRIVMSG ChanServ :AKICK {0} ADD {1}\r\n'.format(channel, banned))
	kick(banned, banner, reason, channel, irc)
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a AKICK ADD to {2} becouse {3} in the channel {4}".format(ctime(), banner, banned, reason, channel))

def unban(banned, banner, mask, channel, irc):
	IrcSend (irc, 'PRIVMSG ChanServ :AKICK {0} DEL {1}\r\n'.format(channel, banned))
	IrcSend (irc, 'MODE {0} -b *!*{1}\r\n'.format(channel, mask))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a AKICK DEL to {2} in the channel {3}".format(ctime(), banner, banned, channel))
