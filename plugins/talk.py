import irclib

def main(data, irc):

	if data["type_data"] == "PRIVMSG":
		pass
	else:
		if data["msg"] == "JOIN" and data["msg_nick"].lower() != data["bot_nick"].lower():
			if data["msg_nick"].lower() in data["womans"]:
				irc.send("PRIVMSG {0} :Hola señora {1}\r\n".format(data["msg_channel"], data["msg_nick"]))
			else:
				irc.send("PRIVMSG {0} :Hola señor {1}\r\n".format(data["msg_channel"], data["msg_nick"]))
