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
import BotConnect
from BotData import *

# Conectarse al servidor IRC
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
irc.connect(("irc.freenode.org", 6667))
# Ingresar al canal IRC
BotConnect.join(irc, nick, user, channel, password)

# Log file
LOG_FILENAME = "everything.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.NOTSET)


# Funcion principal
while __name__ == "__main__":
	BotMain.main(nick, channel, irc)
