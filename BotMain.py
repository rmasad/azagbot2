import socket
import logging
from time import ctime
import configparser


def parse_data(data):
	if "PRIVMSG" in data:
		msg_nick = data[1:data.find("!")]
		msg_user = data[data.find("!n=") + 3:data.find("@")]
		msg = data[data.find("PRIVMSG")+8:].split(" :")[1].strip()
		msg_channel = data[data.find("PRIVMSG")+8:].split(" :")[0]
		return ("PRIVMSG", msg, msg_channel, msg_nick, msg_user)
	elif not 'freenode' in data:
		if 'JOIN' in data:
			msg_channel = data[data.find("JOIN")+6:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "JOIN", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'PART' in data:
			msg_channel = data[data.find("PART")+6:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "PART", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'QUIT' in data:
			msg_channel = data[data.find("QUIT")+6:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "QUIT", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'KICK' in data:
			msg_channel = data[data.find("KICK")+6:]
			msg_channel = msg_channel.split(" ")
			msg = msg_channel[1]
			msg_channel = msg_channel[0]
			return ("KICK", msg.strip(), msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		else:
			return("OTHER", data.strip(), "irc.freenode.org", "freenode", "freenode")
	else:
		return("OTHER", data.strip(), "irc.freenode.org", "freenode", "freenode")


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
