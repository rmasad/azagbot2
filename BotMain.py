# Developed by Rafik Mas'ad (Azag).
# AzagBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# AzagBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Importar modulos 
import socket
import logging
import os
from time import ctime
import plugin
import configparser


version = 2.1

# Funcion que extrae el nombre del usuario.
def get_name(data, channel):
	try:
		return data[1:data.find("!")]
	except:
		return False

# Funcion que extrae el nombre del usuario.
def get_user(data, channel):
	try:
		return data[data.find("!n=") + 3:data.find("@")]
	except:
		return False

# Funcion que extrae el mensaje
def get_msg(data, channel):
	if 'PRIVMSG {0} :'.format(channel) in data:
		msg_start = data.find('PRIVMSG {0} :'.format(channel))
		msg_start += len('PRIVMSG {0} :'.format(channel))
		if data[msg_start:].strip() == " ":
			return "Blank"
		return data[msg_start:].strip()
	return False

# Funcion que extrae el aviso
def get_advice(data, channel, name):
	if not 'freenode' in data:
		if 'JOIN' in data:
			return ('JOIN', 'None')
		if 'PART' in data:
			return ('QUIT', 'None')
		if 'QUIT' in data:
			return ('QUIT', 'None')
		if 'KICK' in data:
			advice_start = data.find('KICK {0} '.format(channel))
			advice_start += len('KICK {0} '.format(channel))
			advice_end = data.find(' :')
			return ('KICK', data[advice_start:advice_end])
	return (False, 'None')

# Funcion que combierte el string en bytes y envia el texto.
def IrcSend(irc, text):
	irc.send(str.encode(text))

# Funcion para sacar (kick) a alguien del canal
def kick(msg, name, channel, irc):
	msg = msg.replace("!kick ", "")
	end_name = msg.find(" ")
	IrcSend (irc, 'KICK {0} {1}\r\n'.format(channel, msg[:end_name]))
	# Registro de la expulsion.
	logging.basicConfig(level="logging.INFO")
	logging.info("{0}: {1} make a KICK to {2} becouse {3}".format(ctime(), name, msg[:end_name] ,msg[end_name+1:]))

# Funcion principal
def main(data, nick, channel, irc, is_op):
	try:
		# Get information from the configs files
		OPs = open("ops.dat", "r")
		OPs = OPs.read().split("\n")
		womans = open("womans.dat", "r")
		womans = womans.read().split("\n")
		
		print (data)

		name = get_name(data, channel)
		user = get_user(data, channel)
		msg = get_msg(data, channel)
		if not msg:
			advice, was_kick = get_advice(data, channel, name)
		else:
			advice, was_kick = False, 'None'
		
		if 'PRIVMSG {0}'.format(nick) in data:
			IrcSend(irc, "PRIVMSG {0} :No acepto mensajes privados.".format(name))
			raise ValueError()

		if advice == 'KICK':
			if was_kick == nick:
				IrcSend (irc, "JOIN {0}\r\n".format(channel))
				IrcSend (irc, "PRIVMSG ChanServ :OP {0}\r\n".format(channel))

		if advice == "JOIN" and name != nick:
			if name not in womans:
				IrcSend (irc, "PRIVMSG {0} :Hola señor {1}\r\n".format(channel, name))
			if name in womans:
				IrcSend (irc, "PRIVMSG {0} :Hola señora {1}\r\n".format(channel, name))
		
		plugin.main(nick, name,msg,user,advice,was_kick,channel,irc, OPs, womans, is_op)

	except UnicodeDecodeError:
		logging.basicConfig(level="logging.ERROR")
		logging.error("{0}: UnicodeDecodeError".format(ctime()))
	
	except ValueError:
		logging.basicConfig(level="logging.WARNING")
		logging.warning("{0}: Private msg send by {1} (User: {2})".format(ctime(), name, user))
