import os
import configparser

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

if __name__ == "__main__":
	main()
		
