from BotMain import kick

# Funcion para sacar (kick) a alguien del canal
def main(data, irc):
	if "@kick" in data["msg"] and data["msg_user"] in data["ops"]:
		msg = data["msg"].replace("@kick ", "")
		end_name = msg.find(" ")
		if end_name == -1:
			kick(msg, data["msg_nick"], "No reason", data["msg_channel"], irc)
		else:
			kick(msg[:end_name], data["msg_nick"], msg[end_name+1:], data["msg_channel"], irc)
