from math import *

def IrcSend(irc, text):
	irc.send(str.encode(text))

def math(msg, channel, irc):

	def el(x,y):
		if y > 10:
			return 'Error'
		else:
			return x**y

	msg = msg[6:] 

	safe_list = ['+', '-', '*', '/', '%',
				 # Numeros
				 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
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

def main(msg, channel, irc,name):
	if msg and '!math' in msg:
		math(msg, channel, irc)
