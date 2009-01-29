import pickle
import logging
from time import ctime
<<<<<<< HEAD:plugins/flood.py
from BotMain import IrcSend
from BotMain import kick
from time import ctime

def main(data, irc):
	msg = data["msg"]
	channel = data["msg_channel"]
	name = data["msg_nick"]
=======

def IrcSend(irc, text):
	irc.send(str.encode(text))

def main(msg, channel, irc,name):
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/flood.py
	if msg:
		try:
			flood = open("flood.dat","br")
			nick = pickle.load(flood)
			time = pickle.load(flood)
			flood.close()
			file = True
		except:
			time = 0
			file = False
	
		if not file or nick == name:
			time += 1
			flood = open("flood.dat","bw")

			if time == 10:
<<<<<<< HEAD:plugins/flood.py
				kick(name, data["bot_nick"], "flood", data["msg_channel"], irc)
=======
				IrcSend (irc, 'KICK {0} {1} {2}\r\n'.format(channel, name, "flood"))
				# Registro de la expulsion.
				logging.basicConfig(level="logging.INFO")
				logging.info("{0}: {1} make a KICK to {2} becouse {3}".format(ctime(), "AzagBot", name, "flood"))
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/flood.py
				time = 0

			pickle.dump(name, flood)
			pickle.dump(time, flood)
			flood.close()
		else:
			time = 1
			flood = open("flood.dat","bw")
			pickle.dump(name, flood)
			pickle.dump(time, flood)
			flood.close()
		
