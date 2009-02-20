from BotMain import unban

# Funcion para sacar (kick) a alguien del canal
def main(data, irc):
	if "@unban" == data["msg"][:6] and data["msg_user"].lower() in data["ops"]:
		msg = data["msg"].replace("@unban ", "")
		end_name = msg.find(" ")
		if end_name == -1:
			unban(msg, data["msg_nick"], "", data["msg_channel"])
		else:
			unban(msg[:end_name], data["msg_nick"], msg[end_name+1:], data["msg_channel"], irc)
