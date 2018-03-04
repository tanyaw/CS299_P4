#Authors: Kim Krishnan, Tanya Wanwatanakool, Derek Yee
#Assignment: Group Project #1
#Topic: Using SQLite3 and Python to simulate online store
#=========================================================

##Creates connection to sqlite database
# @param None
# @return sqlite cursor
import sqlite3
def setSQLConnection():
	#Add Database name
	connection = sqlite3.connect("snackOverFlow.db")
	cursor = connection.cursor()
	return cursor


##Displays Registration Form to console
# @param None
# @return None
def register(c):
	print("--- SNACKER REGISTRATION ---")
	name = input("Please enter your username: ")
	email = input("Please enter your email address: ")
	pin = int(input("Please enter a 4-digit passcode: "))
	BoD = input("Please enter your birthday day(MM/DD/YYYY): ")
	address = input("Please enter your address: ")
	
	#SQL COMMAND: Add info to database
	c.execute("INSERT INTO member (memberID, name, email, password, berf, address) values (NULL,?,?,?,?,?)", (name, email, pin, BoD, address))
	print("Thank you for registering today!\nWe're returning you to the main menu")


##Displays Menu Options to console
# @param None
# @return None
def menu():
	print("How may we help you today?")
	print("--- MENU OPTIONS ---")
	print("1. Register as new snacker.")
	print("2. Go shopping.")
	print("3. Exit.\n")


##Verify that userName and pin match in database
# @param userName, pin, cursor 
# @return Boolean
def verifyPin(userName, pin, c):
	#SQL COMMAND: Select username from database
	c.execute('''SELECT name FROM member WHERE name=?''', (userName,)) 
	user = c.fetchone()
	
	if(user is not None):
		#SQL COMMAND: Select password from database
		c.execute('''SELECT password FROM member WHERE name=?''', (userName,)) 
		pw = c.fetchone()
		
		#Validate username and pin
		for i in pw:
			if (i == pin):
				return True		#Correct password
			else:
				return False	#Wrong password
	else:
		print("You are not a registered snacker!\n")
		return False


def exitDisplay():
	print("\n\nThis program was created by: ")

	print("   _     _      _     _      _     _   ")
	print("  (c).-.(c)    (c).-.(c)    (c).-.(c)  ")
	print("   / ._. \      / ._. \      / ._. \   ")
	print(" __\( Y )/__  __\( Y )/__  __\( Y )/__ ")
	print("(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)")
	print("   || K ||      || I ||      || M ||   ")
	print(" _.' `-' '._  _.' `-' '._  _.' `-' '._ ")
	print("(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)")
	print(" `-'     `-'  `-'     `-'  `-'     `-' \n")

	print("   _     _      _     _      _     _   ")
	print("  (c).-.(c)    (c).-.(c)    (c).-.(c)  ")
	print("   / ._. \      / ._. \      / ._. \   ")
	print(" __\( Y )/__  __\( Y )/__  __\( Y )/__ ")
	print("(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)")
	print("   || T ||      || A ||      || N ||   ")
	print(" _.' `-' '._  _.' `-' '._  _.' `-' '._ ")
	print("(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)")
	print(" `-'     `-'  `-'     `-'  `-'     `-' \n")

	print("   _     _      _     _      _     _   ")
	print("  (c).-.(c)    (c).-.(c)    (c).-.(c)  ")
	print("   / ._. \      / ._. \      / ._. \   ")
	print(" __\( Y )/__  __\( Y )/__  __\( Y )/__ ")
	print("(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)")
	print("   || D ||      || E ||      || R ||   ")
	print(" _.' `-' '._  _.' `-' '._  _.' `-' '._ ")
	print("(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)")
	print(" `-'     `-'  `-'     `-'  `-'     `-' ")


##Main Function
def main():
	print("                      _                        __ _               ")
	print(" ___ _ __   __ _  ___| | _______   _____ _ __ / _| | _____      __")
	print("/ __| '_ \ / _` |/ __| |/ / _ \ \ / / _ \ '__| |_| |/ _ \ \ /\ / /")
	print("\__ \ | | | (_| | (__|   < (_) \ V /  __/ |  |  _| | (_) \ V  V / ")
	print("|___/_| |_|\__,_|\___|_|\_\___/ \_/ \___|_|  |_| |_|\___/ \_/\_/  ")
	
	print("\n***** WECLOME TO SNACKOVERFLOW *****")                                                              	
	print("We have an assortment of snacks to satisfy your every craving.\n")
	
	#Create cursor
	cursor = setSQLConnection()

	while (True): 
		menu()
		userChoice = int(input("Please enter a menu selection (1|2|3): "))

		if (userChoice == 1):
			register(cursor)

		elif (userChoice == 2):
			ERROR = 0
			while ( ERROR< 3 ):
				print("\n--- PLEASE LOGIN ---")
				userName = input("Please enter your username: ")
				pin = input("Please enter your pin: ")

				if ( verifyPin(userName, pin, cursor) ):
					print("You exist.\n")
					break
				else:
					ERROR += 1

			if(ERROR == 3):
				print("Sorry, you inputted the wrong pin too many times.\nWe're returning you to the main menu.\n")

		elif (userChoice == 3):
			print("Thank you for snacking with us today.\nWe look forward to seeing you again!\n")
			exitDisplay()
			exit(0)

		else:
			print("ERROR: This is an invalid choice, please try again.\n")


#Calls main function
main()

