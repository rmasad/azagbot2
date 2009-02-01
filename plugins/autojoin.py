from BotMain import IrcSend, join

def main(data, irc):
		if data["type_data"] == 'KICK' and data["bot_nick"] in data["msg"]:
			join(data["msg_channel"], "off", data["config"], irc)
