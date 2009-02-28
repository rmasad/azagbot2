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
import irclib
import pluginlib
import configparser
import imp


__version = 0.3


try:
	config = configparser.RawConfigParser()
	config.read('config.cfg')
	bot_data = {"user": config.get('Data', 'user'),
				"nick": config.get('Data', 'nick'),
				"ops": config.options("Operators"),
				"version": __version}
except:
	import BotConfig
	BotConfig.main()
	exit()

# Connect and loggin
irc = irclib.main(config.get('Server', 'host'), int(config.get('Server', 'port')))
irc.identify(config.get('Data', 'password'), bot_data["nick"], bot_data["user"])
for channel in config.get("Channels", "channel_list").replace('"',"").replace(' ',"").split(","):
	irc.join(channel)

plugin = pluginlib.main(config.options("Plugins"), irc)

# Funcion principal
while __name__ == "__main__":
	try:
		data = irc.get_data()
		print(data)
		msg_data = irclib.parse(data)
		msg_data.update({"data":data})
		plugin.signal(msg_data, bot_data)
		
	except UnicodeDecodeError:
		pass
