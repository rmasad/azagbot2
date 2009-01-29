<<<<<<< HEAD:plugins/response.py
from BotMain import IrcSend

def main(data, irc):
	msg = data["msg"]
	user = data["msg_user"]
	name = data["msg_nick"]
	nick = data["bot_nick"]
	channel = data["msg_channel"]
	OPs = data["ops"]
=======
def IrcSend(irc, text):
    irc.send(str.encode(text))

def main(nick, name,msg,user,advice,was_kick, channel,irc, OPs, womans, is_op):
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/response.py
	version = 2.1
	response = {'hola {0}'.format(nick.lower()): 'Hola señor {0}\r\n'.format(name),
				'hi {0}'.format(nick.lower()): 'Hi {0}\r\n'.format(name),
				'ping': 'pong\r\n',
				'!v': 'AzagBot versión {0}\r\n'.format(version),
				'!version': 'AzagBot versión {0}\r\n'.format(version)}
		
<<<<<<< HEAD:plugins/response.py
	op_response = {'!op': 'El señor {0} ahora es operado de {1}\r\n'.format(name, channel),
=======
	op_response = {'!kick {0}'.format(was_kick): 'El señor {0} ha sido expulsado por mi\r\n'.format(was_kick),
				   '!op': 'El señor {0} ahora es operado de {1}\r\n'.format(name, channel),
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/response.py
				   '!deop': 'El señor {0} ya no es operado de {1}\r\n'.format(name, channel),
				   '!chao': 'Adios señores y señoras de {0}.\r\n'.format(channel)}
	
	if msg:
		if user in OPs:
			if msg == '!chao':
				IrcSend (irc, "QUIT AzagBot {0}\r\n".format(version))
				exit()
<<<<<<< HEAD:plugins/response.py
	
=======

			if '!kick' in msg:
				kick(msg, name, channel, irc)
					
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/response.py
			if msg == '!op':
				IrcSend (irc, "PRIVMSG ChanServ :OP {0} {1}\r\n".format(channel, name))

			if msg == '!deop':
				IrcSend (irc, "PRIVMSG ChanServ :DEOP {0} {1}\r\n".format(channel, name))
								
			if msg.lower() in op_response:
				IrcSend(irc, "PRIVMSG {0} :{1}".format(channel, op_response[msg.lower()]))
				
		if msg.lower() in response:
			IrcSend(irc, "PRIVMSG {0} :{1}".format(channel, response[msg.lower()]))
