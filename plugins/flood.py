import configparser
import pickle
import logging
from time import ctime
from BotMain import IrcSend
from BotMain import kick, ban
from time import ctime

def main(data, irc):
	type_msg = data["type_data"]
	channel = data["msg_channel"]
	name = data["msg_nick"]
	if type_msg == "PRIVMSG":
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
				config = configparser.RawConfigParser()
				config.read('config.cfg')
				if config.get('Plugins', 'flood') == "kick":
					kick(name, data["bot_nick"], "flood", data["msg_channel"], irc)
				if config.get('Plugins', 'flood') == "ban":
					ban(name, data["bot_nick"], "flood", data["msg_channel"], irc)
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
		
