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
import configparser
from time import ctime

logging.basicConfig(filename="everything.log",level=logging.NOTSET)

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
channel_list = config.get("Channels", "channel_list").replace('"',"").replace(' ',"").split(",")
for channel in chs:
	BotMain.join(channel, config, irc)

for plugin in config.options("Plugins"):
	exec("from plugins import {0}".format(plugin))

# Funcion principal
while __name__ == "__main__":
	try:
		data = bytes.decode(irc.recv(4096))
		print(data)
		
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
					   "data": data,
					   "channel_list": config.options("Channels"),
					   "msg_channel": msg_channel,
					   "msg_nick": msg_nick,
					   "msg_user": msg_user}
		
		for plugin in config.options("Plugins"):
			exec("{0}.main(parsed_data,irc)".format(plugin))
		
	except UnicodeDecodeError:
		logging.basicConfig(level="logging.ERROR")
		logging.error("{0}: UnicodeDecodeError".format(ctime()))
