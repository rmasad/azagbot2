import irclib

class main:
	def __init__(self, irc):
		self.irc = irc

	def main(self, msg_data, bot_data):
		if msg_data["type"] == 'KICK' and bot_data["nick"] in msg_data["receiver"].split()[1]:
			self.irc.join(msg_data["receiver"].split()[0])
