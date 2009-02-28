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

import irclib
import imp


class main:
	def __init__(self, plugin_list, irc):
		for plugin in plugin_list:
			exec("from plugins import {0}".format(plugin))
			exec("self.{0} = {0}.main(irc)".format(plugin))
		self.plugin_list = plugin_list
		self.irc = irc
		self.do = irclib.commands(irc)
	
	def signal(self, msg_data, bot_data):
		
		def start(self, module, receiver):
			print("START")
			try:
				exec("print(dir({0}))".format(module))
			except:
				exec("from plugins import {0}".format(module))
			
			if module not in self.plugin_list:
				self.plugin_list += [module]
				self.do.send(receiver, "{0} started".format(module))
			else:
				self.do.send(receiver, "{0} already started".format(module))
		
		def stop(self, module, receiver):
			if module in self.plugin_list:
				del(self.plugin_list[self.plugin_list.index(module)])
				self.do.send(receiver, "{0} stoped".format(module))
			else:
				self.do.send(receiver, "{0} is not already started".format(module))
		
		def restart(self, module, receiver):
			try:
				exec("imp.reload({0})".format(module))
				self.do.send(receiver, "{0} restarted".format(module))
			except:
				self.do.send(receiver, "{0} is not already started".format(module))
				start(self, module, receiver)
				self.do.send(receiver, "{0} started".format(module))
				
		if msg_data["nick"].lower() in bot_data["ops"]:
			if msg_data["msg"][:7] == "@start ":
				start(self, msg_data["msg"][7:], msg_data["receiver"])

			if msg_data["msg"][:6] == "@stop ":
				stop(self, msg_data["msg"][6:], msg_data["receiver"])

			if msg_data["msg"][:9] == "@restart ":
				restart(self, msg_data["msg"][9:], msg_data["receiver"])

		for plugin in self.plugin_list:
			exec("self.{0}.main(msg_data, bot_data)".format(plugin))
