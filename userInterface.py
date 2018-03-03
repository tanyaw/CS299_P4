#Authors: Kim Krishnan, Tanya Wanwatanakool, and Derek Yee
#Assignment: Group Project #1
#Completed: 03/02/2018


##Creates connection to sqlite DB
# @param None
# @return sqlite cursor
import sqlite3
def setSQLConnection():
	#Add Database name
	connection = sqlite3.connect("company.db")
	cursor = connection.cursor()
	return cursor


##Displays Registration Form to console
# @param None
# @return None
def register():
	print("--- SNACKER REGISTRATION ---")
	name = input("Please enter your username: ")
	email = input("Please enter your email address: ")
	address = input("Please enter your address: ")
	BoD = input("Please enter your birthday day(MM/DD/YYYY): ")
	credit = input("Please enter your credit card number: ")
	pin = int(input("Please enter a 4-digit passcode: "))
	
	#SQL COMMAND: Add info to database

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

##Verify that userName and pin match in DB
# @param userName and pin 
# @return Boolean
# def verifyPin(userName, pin):
# 	if(userName and pin in DB):
# 		return True
# 	else: 
# 		return False


##Main Function
def main():
	print("                      _                        __ _               ")
	print(" ___ _ __   __ _  ___| | _______   _____ _ __ / _| | _____      __")
	print("/ __| '_ \ / _` |/ __| |/ / _ \ \ / / _ \ '__| |_| |/ _ \ \ /\ / /")
	print("\__ \ | | | (_| | (__|   < (_) \ V /  __/ |  |  _| | (_) \ V  V / ")
	print("|___/_| |_|\__,_|\___|_|\_\___/ \_/ \___|_|  |_| |_|\___/ \_/\_/  ")
	
	print("\n***** WECLOME TO SNACKOVERFLOW *****")                                                              	
	print("We have an assortment of snacks to satisfy your every craving.\n")

	while (True): 
		menu()
		userChoice = int(input("Please enter a menu selection (1|2|3): "))

		if (userChoice == 1):
			register()
		elif (userChoice == 2):
			ERROR = 0
			while ( ERROR< 3 ):
				userName = input("Please enter your username: ")
				pin = int(input("Please enter your pin: "))
				# if (verifyPin(userName, pin)):

				# else:
				# 	ERROR += 1

			print("Sorry, you inputted the wrong pin too many times.\nWe're returning you to the main menu.\n")
		elif (userChoice == 3):
			print("Thank you for snacking with us today.\nWe look forward to seeing you again!\n")
			exit(0)
		else:
			print("ERROR: This is an invalid choice, please try again.\n")

#Calls main function
main()
