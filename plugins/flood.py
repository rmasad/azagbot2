import pickle
import logging
from time import ctime
from BotMain import IrcSend
from BotMain import kick
from time import ctime

def main(data, irc):
	msg = data["msg"]
	channel = data["msg_channel"]
	name = data["msg_nick"]
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
				kick(name, data["bot_nick"], "flood", data["msg_channel"], irc)
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
		
