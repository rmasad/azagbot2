import irclib
from time import ctime

class main():
	def __init__(self, irc):
		self.irc = irc
		self.do = irclib.commands(irc)
		self.flood_array = []


	def main(self, msg_data, bot_data):
		type_msg = msg_data["type"]
		channel = msg_data["receiver"]
		name = msg_data["nick"]
		if type_msg == "PRIVMSG":

			channel_in_list = False
			
			for i in range(0,len(self.flood_array)):
				if self.flood_array[i][0] == channel:
					channel_in_list = True
					if name == self.flood_array[i][1]:
						self.flood_array[i][2] += 1
						if self.flood_array[i][2] == 10:
							self.do.kick(channel, name)
							self.flood_array[i][2] = 1
					else:
						self.flood_array[i][1] = name
						self.flood_array[i][2] = 1

			if not channel_in_list:
				self.flood_array += [[channel, name, 0]]
		
