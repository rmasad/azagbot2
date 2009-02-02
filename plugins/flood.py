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
			flood_file = open("plugins/flood.dat","br")
			flood_array = pickle.load(flood_file)
			flood_file.close()
		except:
			flood_file = open("plugins/flood.dat","bw")
			pickle.dump([[channel, name, 0]], flood_file)
			flood_file.close()
			return
		
		
		channel_in_list = False
		
		for i in range(0,len(flood_array)):
			if flood_array[i][0] == channel:
				channel_in_list = True
				if name == flood_array[i][1]:
					flood_array[i][2] += 1
					if flood_array[i][2] == 10:
						config = configparser.RawConfigParser()
						config.read('config.cfg')
						if config.get('Plugins', 'flood') == "kick":
							kick(name, data["bot_nick"], "flood", data["msg_channel"], irc)
						if config.get('Plugins', 'flood') == "ban":
							ban(name, data["bot_nick"], "flood", data["msg_channel"], irc)
						flood_array[i][2] = 1
				else:
					flood_array[i][1] = name
					flood_array[i][2] = 1

		if not channel_in_list:
			flood_array += [[channel, name, 0]]
		
		flood_file = open("plugins/flood.dat","bw")
		pickle.dump(flood_array, flood_file)
		flood_file.close()
		
