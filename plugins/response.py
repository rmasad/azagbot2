from BotMain import IrcSend

def main(data, irc):
	msg = data["msg"]
	user = data["msg_user"]
	name = data["msg_nick"]
	nick = data["bot_nick"]
	channel = data["msg_channel"]
	OPs = data["ops"]
	version = 2.1
	response = {'hola {0}'.format(nick.lower()): 'Hola señor {0}\r\n'.format(name),
				'hi {0}'.format(nick.lower()): 'Hi {0}\r\n'.format(name),
				'ping': 'pong\r\n',
				'!v': 'AzagBot versión {0}\r\n'.format(version),
				'!version': 'AzagBot versión {0}\r\n'.format(version)}
		
	op_response = {'!op': 'El señor {0} ahora es operado de {1}\r\n'.format(name, channel),
				   '!deop': 'El señor {0} ya no es operado de {1}\r\n'.format(name, channel),
				   '!chao': 'Adios señores y señoras de {0}.\r\n'.format(channel)}
	
	if msg:
		if user in OPs:
			if msg == '!chao':
				IrcSend (irc, "QUIT AzagBot {0}\r\n".format(version))
				exit()
	
			if msg == '!op':
				IrcSend (irc, "PRIVMSG ChanServ :OP {0} {1}\r\n".format(channel, name))

			if msg == '!deop':
				IrcSend (irc, "PRIVMSG ChanServ :DEOP {0} {1}\r\n".format(channel, name))
								
			if msg.lower() in op_response:
				IrcSend(irc, "PRIVMSG {0} :{1}".format(channel, op_response[msg.lower()]))
				
		if msg.lower() in response:
			IrcSend(irc, "PRIVMSG {0} :{1}".format(channel, response[msg.lower()]))
