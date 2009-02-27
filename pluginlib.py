#!/usr/bin/env python3

# Developed by Rafik Mas'ad (Azag).
# PluginLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# PluginLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/

class main:
	def __init__(self, plugin_list, irc):
		for plugin in plugin_list:
			exec("from plugins import {0}".format(plugin))
			exec("self.{0} = {0}.main(irc)".format(plugin))
		self.plugin_list = plugin_list
		self.irc = irc
	
	def signal(self, msg_data, bot_data):
		for plugin in self.plugin_list:
			exec("self.{0}.main(msg_data, bot_data)".format(plugin))
