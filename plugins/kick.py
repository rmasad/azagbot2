import irclib
class main():
	def __init__(self, irc):
		self.irc = irc
		self.do = irclib.commands(irc)

	def main(self, msg_data, bot_data):
		if "@kick" == msg_data["msg"][:5] and msg_data["user"].lower() in bot_data["ops"]:
			msg = msg_data["msg"].replace("@kick ", "")
			self.do.kick(msg_data["receiver"],msg)
