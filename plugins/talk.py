from BotMain import IrcSend

def main(data, irc):

	if data["type_data"] == "PRIVMSG":
		pass
	else:
		if data["msg"] == "JOIN" and data["msg_nick"] != data["bot_nick"]:
			if data["msg_nick"] in data["womans"]:
				IrcSend(irc, "PRIVMSG {0} :Hola señora {1}\r\n".format(data["msg_channel"], data["msg_nick"]))
			else:
				IrcSend(irc, "PRIVMSG {0} :Hola señor {1}\r\n".format(data["msg_channel"], data["msg_nick"]))
