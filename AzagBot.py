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
def join(irc, nick, user, channel, password):
	BotMain.IrcSend (irc, 'PASS {0}\r\n'.format(password))
	BotMain.IrcSend (irc, 'NICK {0}\r\n'.format(nick))
	BotMain.IrcSend (irc, 'USER {0} {0} {0} :Python IRC\r\n'.format(user))
	BotMain.IrcSend (irc, 'JOIN {0}\r\n'.format(channel))
	BotMain.IrcSend (irc, 'PRIVMSG ChanServ :OP {0}\r\n'.format(channel))

# Config file
if "config.cfg" not in os.listdir('.'):
	config = configparser.RawConfigParser()

	config.add_section('Data')
	config.set('Data', 'channel', '#saffire-dev')
	config.set('Data', 'user', 'AzagBot')
	config.set('Data', 'nick', 'AzagBot')
	config.set('Data', 'password', 'gnu')
	
	config.add_section('Channel members')
	config.set('Channel members', 'womans', 'elisa')
	config.set('Channel members', 'OPs', 'azag')
	config.set('Channel members', 'moderators', ['srinux', 'carlosr'])
	
	with open('config.cfg', 'w') as configfile:
		config.write(configfile)

# Get information from the config file
config = configparser.RawConfigParser()
config.read('config.cfg')

channel = config.get('Data', 'channel')
user = config.get('Data', 'user')
nick = config.get('Data', 'nick')
password = config.get('Data', 'password')

# Conectarse al servidor IRC
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.freenode.org", 6667))
# Ingresar al canal IRC
join(irc, nick, user, channel, password)

# Log file
LOG_FILENAME = "everything.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.NOTSET)

# Funcion principal
while __name__ == "__main__":
	BotMain.main(nick, channel, irc)
