from math import *
import irclib

class main():
	def __init__(self, irc):
		self.irc = irc

	def main(self, msg_data, bot_data):

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

		def c_interest(initial, percentage, periods):
			return initial*(1 + percentage/100)**periods
		
		def el(x,y):
			if y > 10:
				return 'Error'
			else:
				return x**y	
		
		commands = irclib.commands(self.irc)
		
		if msg_data["type"] == "PRIVMSG" and '@math' in msg_data["msg"]:
			msg = msg_data["msg"][6:] 
			danger = msg.strip()	
			for element in safe_list:
				danger = danger.replace(element, "")

			if '**' in msg:
				danger = True
			
			try:
				if not danger and eval(msg) < 10**100:
					if msg_data["receiver"][:1] == "#":
						commands.send(msg_data["receiver"], ">> {0}".format(eval(msg)))
					else:
						commands.send(msg_data["nick"], ">> {0}".format(eval(msg)))
				else:
					raise NonSafeExpression
			except:
					if msg_data["receiver"][:1] == "#":
						commands.send(msg_data["receiver"], ">> Error")
					else:
						commands.send(msg_data["nick"], ">> Error")
