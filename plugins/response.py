import irclib

class main():
	def __init__(self, irc):
		self.irc = irc
		self.do = irclib.commands(irc)

	def main(self, msg_data, bot_data):
		msg = msg_data["msg"]
		name = msg_data["nick"]
		nick = bot_data["nick"]
		channel = msg_data["receiver"]
		OPs = bot_data["ops"]
		version = bot_data["version"]
		 
		response = {'hola {0}'.format(nick.lower()): 'Hola señor {0}\r\n'.format(name),
					'hi {0}'.format(nick.lower()): 'Hi {0}\r\n'.format(name),
					'ping': 'pong\r\n',
					'!v': 'SPIB versión {0}\r\n'.format(version),
					'!version': 'SPIB versión {0}\r\n'.format(version),
					"!about": "Soy SPIB (Simple Python3 Irc Bot). Estoy bajo la GNU GPL 3.\r\n"}
			
		op_response = {'@op': 'El señor {0} ahora es operador de {1}\r\n'.format(name, channel),
					   '@deop': 'El señor {0} ya no es operador de {1}\r\n'.format(name, channel),
					   '@chao': 'Adios señores y señoras de {0}.\r\n'.format(channel),
					   "@get_op": 'Ahora soy operador de {0}.\r\n'.format(channel)}
		
		if msg:
			if name.lower() in OPs:
				if msg.lower() in op_response:
					self.do.send(channel, "{0}".format(op_response[msg.lower()]))
					
		
				if msg == '@op':
					self.do.send("ChanServ", "OP {0} {1}".format(channel, name))

				if msg == '@deop':
					self.do.send("ChanServ", "DEOP {0} {1}".format(channel, name))
				
				if msg == "@get_op":
					self.do.send("ChanServ", "OP {0} {1}".format(channel, nick))
					
			if msg.lower() in response:
				self.do.send(channel, "{0}".format(response[msg.lower()]))
