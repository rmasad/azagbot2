#!/usr/bin/env python3

# Developed by Rafik Mas'ad (Azag).
# IRCLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# IRCLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/

import socket

class irc():
	def __init__(self, HOST, PORT = 6667):
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.irc.connect((HOST, PORT))
		self.data_list = []
	
	def identify(self, password, nick, user):
		self.irc.send(str.encode('PASS {0}\r\n'.format(password)))
		self.irc.send(str.encode('NICK {0}\r\n'.format(nick)))
		self.irc.send(str.encode('USER {0} {0} {0} :Python IRC\r\n'.format(user)))

	def join(self, channel):
		self.irc.send(str.encode('JOIN {0}\r\n'.format(channel)))
	
	def get_data(self):
		def get_first_data(self):
			data = self.data_list[0]
			del self.data_list[0]
			return data
			
		if not self.data_list:
			self.data_list += bytes.decode(self.irc.recv(4096)).split("\r\n")
		
		return get_first_data(self)
			
	
	def send(self, msg):
		self.irc.send(str.encode(msg))
