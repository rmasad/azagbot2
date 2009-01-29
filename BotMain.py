import socket
import logging
from time import ctime
<<<<<<< HEAD:BotMain.py
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
=======
import plugin
import configparser


version = 2.1

# Funcion que extrae el nombre del usuario.
def get_name(data, channel):
	try:
		return data[1:data.find("!")]
	except:
		return False

# Funcion que extrae el nombre del usuario.
def get_user(data, channel):
	try:
		return data[data.find("!n=") + 3:data.find("@")]
	except:
		return False

# Funcion que extrae el mensaje
def get_msg(data, channel):
	if 'PRIVMSG {0} :'.format(channel) in data:
		msg_start = data.find('PRIVMSG {0} :'.format(channel))
		msg_start += len('PRIVMSG {0} :'.format(channel))
		if data[msg_start:].strip() == " ":
			return "Blank"
		return data[msg_start:].strip()
	return False

# Funcion que extrae el aviso
def get_advice(data, channel, name):
	if not 'freenode' in data:
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:BotMain.py
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

<<<<<<< HEAD:BotMain.py
def kick(kicked, kicker, reason, channel, irc):
	IrcSend (irc, 'KICK {0} {1}\r\n'.format(channel, kicked))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a KICK to {2} becouse {3} in the channel {4}".format(ctime(), kicker, kicked, reason, channel))
=======
# Funcion para sacar (kick) a alguien del canal
def kick(msg, name, channel, irc):
	msg = msg.replace("!kick ", "")
	end_name = msg.find(" ")
	IrcSend (irc, 'KICK {0} {1}\r\n'.format(channel, msg[:end_name]))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a KICK to {2} becouse {3}".format(ctime(), name, msg[:end_name] ,msg[end_name+1:]))

# Funcion principal
def main(data, nick, channel, irc, is_op):
	try:
		# Get information from the configs files
		OPs = open("ops.dat", "r")
		OPs = OPs.read().split("\n")
		womans = open("womans.dat", "r")
		womans = womans.read().split("\n")
		
		print (data)

		name = get_name(data, channel)
		user = get_user(data, channel)
		msg = get_msg(data, channel)
		if not msg:
			advice, was_kick = get_advice(data, channel, name)
		else:
			advice, was_kick = False, 'None'
		
		if 'PRIVMSG {0}'.format(nick) in data:
			IrcSend(irc, "PRIVMSG {0} :No acepto mensajes privados.".format(name))
			raise ValueError()

		if advice == 'KICK':
			if was_kick == nick:
				IrcSend (irc, "JOIN {0}\r\n".format(channel))
				IrcSend (irc, "PRIVMSG ChanServ :OP {0}\r\n".format(channel))

		if advice == "JOIN" and name != nick:
			if name not in womans:
				IrcSend (irc, "PRIVMSG {0} :Hola señor {1}\r\n".format(channel, name))
			if name in womans:
				IrcSend (irc, "PRIVMSG {0} :Hola señora {1}\r\n".format(channel, name))
		
		plugin.main(nick, name,msg,user,advice,was_kick,channel,irc, OPs, womans, is_op)
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:BotMain.py

