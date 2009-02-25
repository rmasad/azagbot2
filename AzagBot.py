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
import imp
import socket
import logging
import BotMain
import irclib
import configparser
from time import ctime



logging.basicConfig(filename="everything.log",level=logging.NOTSET)

try:
	# Get information from the config file
	config = configparser.RawConfigParser()
	config.read('config.cfg')
except:
	import BotConfig
	BotConfig.main()
	exit()

bot_data = {"bot_user": config.get('Data', 'user'),
			"bot_nick": config.get('Data', 'nick'),
			"ops": config.options("Operators"),
			"womans": config.options("Womans")}

	
# Connect and loggin
irc = irclib.irc(config.get('Server', 'host'), int(config.get('Server', 'port')))
irc.identify(config.get('Data', 'password'), bot_data["bot_nick"], bot_data["bot_user"])
for channel in config.get("Channels", "channel_list").replace('"',"").replace(' ',"").split(","):
	irc.join(channel)

for plugin in config.options("Plugins"):
	exec("from plugins import {0}".format(plugin))

plugins_list = config.options("Plugins")

# Funcion principal
while __name__ == "__main__":
	try:
		data = irc.get_data()
		print(data)
		type_data, msg, msg_channel, msg_nick, msg_user = BotMain.parse_data(data)
		
		if msg_user in bot_data["ops"]:
			if type_data == "PRIVMSG" and msg.lower() == "@exit":
				exit()
			if "@start " == msg[:7]:
				try:
					print(exec("dir({0})".format(msg[7:])))
				except:
					exec("from plugins import {0}".format(msg[7:]))			
					if msg[7:] not in plugins_list:
						plugins_list += [msg[7:]]
			
			if "@restart " == msg[:9]:
				try:
					print(exec("dir({0})".format(msg[7:])))
					exec("imp.reload({0})".format(msg[7:]))
				except:
					exec("from plugins import {0}".format(msg[7:]))			
					if msg[7:] not in plugins_list:
						plugins_list += [msg[7:]]
			
			if "@stop " == msg[:6]:
				if msg[7:] in plugins_list:
					del plugins_list[plugins_list.index(msg[7:])]
				
		
		msg_data = {"type_data": type_data,
					"msg": msg,
					"data": data,
					"channel_list": config.options("Channels"),
					"msg_channel": msg_channel,
					"msg_nick": msg_nick,
					"msg_user": msg_user}
		
		bot_data.update(msg_data)
		for plugin in plugins_list:
			exec("{0}.main(bot_data, irc)".format(plugin))
		
	except UnicodeDecodeError:
		logging.basicConfig(level="logging.ERROR")
		logging.error("{0}: UnicodeDecodeError".format(ctime()))
