from BotMain import IrcSend

def main(data, irc):

	if data["type_data"] == "PRIVMSG":
		pass
	else:
		if data["msg"] == "JOIN":
			if data["msg_nick"] in data["womans"]:
				IrcSend(irc, "PRIVMSG {0} :Hola señora {0}".format(data["msg_channel"], data["msg_nick"]))
			else:
				IrcSend(irc, "PRIVMSG {0} :Hola señor {0}".format(data["msg_channel"], data["msg_nick"]))
