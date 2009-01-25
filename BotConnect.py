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

from BotMain import IrcSend

# Funcion que ingresa el usuario al canal
def join(irc, nick, user, channel, password):
	IrcSend (irc, 'PASS {0}\r\n'.format(password))
	IrcSend (irc, 'NICK {0}\r\n'.format(nick))
	IrcSend (irc, 'USER {0} {0} {0} :Python IRC\r\n'.format(user))
	IrcSend (irc, 'JOIN {0}\r\n'.format(channel))
	IrcSend (irc, 'PRIVMSG ChanServ :OP {0}\r\n'.format(channel))
