from BotMain import IrcSend

def main(data, irc):

	if data["type_data"] == "PRIVMSG":
		pass
	else:
		if msg == "JOIN":
			if data["msg_nick"] in data["womans"]:
				print("Hola señora {0}".format(data["msg_nick"]))
			else:
				print("Hola señor {0}".format(data["msg_nick"]))
