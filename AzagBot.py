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

import socket
import logging
import BotMain
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

# Log file
LOG_FILENAME = "everything.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.NOTSET)

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
