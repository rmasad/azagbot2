#!/usr/bin/env python3

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
# along with this program.  If not, see <http://www.gnu.org/licenses/

import os
import socket
import logging
import BotMain
<<<<<<< HEAD:AzagBot.py
import configparser
from time import ctime

logging.basicConfig(filename="everything.log",level=logging.NOTSET)
=======
import os
import configparser


# Funcion que ingresa el usuario al canal
def join(irc, nick, user, channel, password, is_op):
	BotMain.IrcSend (irc, 'PASS {0}\r\n'.format(password))
	BotMain.IrcSend (irc, 'NICK {0}\r\n'.format(nick))
	BotMain.IrcSend (irc, 'USER {0} {0} {0} :Python IRC\r\n'.format(user))
	BotMain.IrcSend (irc, 'JOIN {0}\r\n'.format(channel))
	if is_op:
		BotMain.IrcSend (irc, 'PRIVMSG ChanServ :OP {0}\r\n'.format(channel))

if "config.cfg" not in os.listdir('.'):
	import BotConfig
	BotConfig.main()

# Get information from the config file
config = configparser.RawConfigParser()
config.read('config.cfg')
channel = config.get("Settings", 'channel')
user = config.get('Data', 'user')
nick = config.get('Data', 'nick')
password = config.get('Data', 'password')
is_op = config.getboolean("Settings", "is_op")

# Conectarse al servidor IRC
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.freenode.org", 6667))
# Ingresar al canal IRC
join(irc, nick, user, channel, password, is_op)
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:AzagBot.py

try:
	# Get information from the config file
	config = configparser.RawConfigParser()
	config.read('config.cfg')
	bot_user = config.get('Data', 'user')
	bot_nick = config.get('Data', 'nick')
	bot_password = config.get('Data', 'password')
	ops = config.options("Operators")
	womans = config.options("Womans")
except:
	import BotConfig
	BotConfig.main()
	exit()
	
# Connect and loggin
irc = BotMain.connect(bot_nick, bot_user, bot_password)
for channel in config.options("Channels"):
	BotMain.join("#" + channel, config, irc)

<<<<<<< HEAD:AzagBot.py
for plugin in config.options("Plugins"):
	exec("from plugins import {0}".format(plugin))

# Funcion principal
while __name__ == "__main__":
	try:
		#data = bytes.decode(irc.recv(4096))
		data = bytes.decode(irc.recv(6667))
				
		type_data, msg, msg_channel, msg_nick, msg_user = BotMain.parse_data(data)
		if type_data == "PRIVMSG" and msg.lower() == "@exit" and msg_user in ops:
			exit()
		
		parsed_data = {"bot_nick": bot_nick,
					   "bot_user": bot_user,
					   "bot_password": bot_password,
					   "config": config,
					   "ops": ops,
					   "womans": womans,
					   "type_data": type_data,
					   "msg": msg,
					   "channel_list": config.options("Channels"),
					   "msg_channel": msg_channel,
					   "msg_nick": msg_nick,
					   "msg_user": msg_user}
		
		for plugin in config.options("Plugins"):
			exec("{0}.main(parsed_data,irc)".format(plugin))
		
		print(data)
		
	except UnicodeDecodeError:
		logging.basicConfig(level="logging.ERROR")
		logging.error("{0}: UnicodeDecodeError".format(ctime()))
=======
if config.getboolean("Settings", "non_flood"):
	flood_name = user
	flood_times = 0

# Funcion principal
while __name__ == "__main__":
	data = bytes.decode(irc.recv(4096))
	BotMain.main(data, nick, channel, irc, is_op)

	if config.getboolean("Settings", "non_flood"):
		if BotMain.get_msg(data, channel):
			if BotMain.get_name(data, channel) == flood_name:
				flood_times += 1
			else:
				flood_name = BotMain.get_name(data, channel)
				flood_time = 0
	
	if flood_times == 10:
		BotMain.kick("!kick {0} flood".format(flood_name), nick, channel, irc)
		flood_times = 0
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:AzagBot.py
