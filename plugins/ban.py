from BotMain import ban

# Funcion para sacar (akick) a alguien del canal
def main(data, irc):
	if "@ban" in data["msg"] and data["msg_user"] in data["ops"]:
		msg = data["msg"].replace("@ban ", "")
		end_name = msg.find(" ")
		if end_name == -1:
			ban(msg, data["msg_nick"], "No reason", data["msg_channel"], irc)
		else:
			ban(msg[:end_name], data["msg_nick"], msg[end_name+1:], data["msg_channel"], irc)
