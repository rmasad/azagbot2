import socket
import logging
from time import ctime
import configparser

# Funcion que ingresa el usuario al canal
def connect(nick, user, password):
	irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	irc.connect(("irc.freenode.org", 6667))
	irc.send(str.encode('PASS {0}\r\n'.format(password)))
	irc.send(str.encode('NICK {0}\r\n'.format(nick)))
	irc.send(str.encode('USER {0} {0} {0} :Python IRC\r\n'.format(user)))
	return irc

def join(channel, config, irc):
	irc.send(str.encode('JOIN {0}\r\n'.format(channel)))
	if config.getboolean('Channels', channel[1:]):
		irc.send(str.encode('PRIVMSG ChanServ :OP {0}\r\n'.format(channel)))

def parse_data(data):
	if "PRIVMSG" in data:
		msg_nick = data[1:data.find("!")]
		msg_user = data[data.find("!n=") + 3:data.find("@")]
		msg = data[data.find("PRIVMSG")+8:].split(" :")[1].strip()
		msg_channel = data[data.find("PRIVMSG")+8:].split(" :")[0]
		return ("PRIVMSG", msg, msg_channel, msg_nick, msg_user)
	elif not 'freenode' in data:
		if 'JOIN' in data:
			msg_channel = data[data.find("JOIN")+5:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "JOIN", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'PART' in data:
			msg_channel = data[data.find("PART")+5:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "PART", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'QUIT' in data:
			msg_channel = data[data.find("QUIT")+5:]
			msg_channel = msg_channel.replace(" :","")
			return ("SERVERMSG", "QUIT", msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		elif 'KICK' in data:
			msg_channel = data[data.find("KICK")+5:]
			msg_channel = msg_channel.split(" :")
			msg = msg_channel[1]
			msg_channel = msg_channel[0]
			return ("KICK", msg.strip(), msg_channel, data[1:data.find("!")], data[data.find("!n=") + 3:data.find("@")])
		else:
			return("OTHER", data.strip(), "irc.freenode.org", "freenode", "freenode")
	else:
		return("OTHER", data.strip(), "irc.freenode.org", "freenode", "freenode")

# Funcion que combierte el string en bytes y envia el texto.
def IrcSend(irc, text):
	irc.send(str.encode(text))

def kick(kicked, kicker, reason, channel, irc):
	IrcSend (irc, 'KICK {0} {1}\r\n'.format(channel, kicked))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a KICK to {2} becouse {3} in the channel {4}".format(ctime(), kicker, kicked, reason, channel))

