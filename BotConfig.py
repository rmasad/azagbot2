import os
import configparser

<<<<<<< HEAD:BotConfig.py
def main():
	if "config.cfg" in os.listdir('.'):
		os.remove("config.cfg")
	
	print(":: The default config will be add in config.cfg")
	config = configparser.RawConfigParser()
	
	config.add_section('Data')
	config.set('Data', 'nick', "AzagBot")
	config.set('Data', 'user', "NonRegisteredAzagBot")
	config.set('Data', 'password', "PASSWORD")
	
	#config.add_section("Settings")
	
	config.add_section("Womans")
	config.set("Womans", "maria", "")
	config.set("Womans", "juana", "")
	config.set("Womans", "elisa", "")
	
	config.add_section("Operators")
	config.set("Operators", "Azag", "")
	config.set("Operators", "AzagBot", "")
	
	config.add_section("Channels")
	config.set("Channels", "Supremos", "off")

	config.add_section("Plugins")
	config.set("Plugins", "math", "")
	config.set("Plugins", "kick", "")
	config.set("Plugins", "autojoin", "")

	with open('config.cfg', 'w') as configfile:
		config.write(configfile)
	
	print(":: Edit config.cfg with the data of the Bot Account")
=======
def account():
	print(":: The data of the account.")
	user = input("User name: ")
	nick = input("Nick to use: ")
	password = input("Password of the account: ")
	
	config = configparser.RawConfigParser()
	config.add_section('Data')
	config.set('Data', 'user', user)
	config.set('Data', 'nick', nick)
	config.set('Data', 'password', password)

	channel = input("Channel to join: ")
	is_op = "lol"
	non_flood = "lol"
	while is_op not in ['yes', 'no']:
		is_op = input("Is the AzagBot channel operator? (yes/no): ")
	while non_flood not in ['yes', 'no']:
		if is_op == "yes":
			non_flood = input("Active the anti-flood? (yes/no): ")
		else:
			non_flood = "no"

	config.add_section("Settings")
	config.set("Settings", "channel", channel)
	config.set("Settings", "is_op", is_op)
	config.set("Settings", "non_flood", non_flood)
	
	with open('config.cfg', 'w') as configfile:
		config.write(configfile)

	return user

def channel_settings(user):
	op = user
	ops = open('ops.dat', 'a')
	print(":: Write the users of the operators. If you want to stop writing operators, ENTER.") 
	while op:
		ops.write(op + "\n")
		op = input("User name: ")
	
	woman = "maria"
	womans = open('womans.dat', 'a')
	print(":: Write the womans nicks of the channel. If you want to stop writing womans, ENTER.") 
	while woman:
		womans.write(woman + "\n")
		woman = input("Nickname: ")



def main():
	if "config.cfg" in os.listdir('.'):
		os.remove("config.cfg")
	if "ops.dat" in os.listdir('.'):
		os.remove("ops.dat")
	if "womans.dat" in os.listdir('.'):
		os.remove("womans.dat")

	user = account()
	channel_settings(user)
>>>>>>> 82b338862860eb47c0a9830d1cf96c80a0e3594e:BotConfig.py

if __name__ == "__main__":
	main()
		
