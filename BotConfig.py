import os
import configparser

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

if __name__ == "__main__":
	main()
		
