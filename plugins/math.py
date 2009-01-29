from math import *
<<<<<<< HEAD:plugins/math.py
from BotMain import IrcSend
=======

def IrcSend(irc, text):
    irc.send(str.encode(text))
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/math.py

def math(msg, channel, irc):

	def el(x,y):
		if y > 10:
			return 'Error'
		else:
			return x**y
    
	def c_interest(initial, percentage, periods):
		return initial*(1 + percentage/100)**periods

	msg = msg[6:] 

	safe_list = ['+', '-', '*', '/', '%',
				 # Numeros
				 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
				 # Financias
				 'c_interest',
				 # Elevado, raiz y logaritmo
				 'el', 'sqrt',
				 'log', 'log10',
				 # Geometria
				 'acos', 'cosh', 'cos',
				 'asin', 'sinh', 'sin',
				 'atan2', 'atan', 'tanh', 'tan',
				 'hypot',
				 'radians',
				 # Simbolos
				 '(', ')',
				 '.', ',',
				 ' ',
				 '=',
				 # Constantes matematicas
				 'e', 'pi',
				 # Aproximaciones
				 'ceil', 'floor']

	danger = msg
	
	for element in safe_list:
		danger = danger.replace(element, "")

	if '**' in msg:
		danger = True

	try:
		if not danger and eval(msg) < 10**100:
			IrcSend (irc, "PRIVMSG {0} :>> {1}\r\n".format(channel,eval(msg)))
		else:
			raise NonSafeExpression
	except:
		IrcSend (irc, "PRIVMSG {0} :>> Error\r\n".format(channel))

<<<<<<< HEAD:plugins/math.py
def main(parsed_data, irc):
	if parsed_data["type_data"] == "PRIVMSG" and '@math' in parsed_data["msg"]:
		math(parsed_data["msg"], parsed_data["msg_channel"], irc)
=======
def main(nick, name,msg,user,advice,was_kick,channel,irc, OPs, womans, is_op):
	if msg and '!math' in msg:
		math(msg, channel, irc)
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:plugins/math.py
