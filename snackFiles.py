#import database
import sqlite3
connection=sqlite3.connect("snackOverFlow.db")   #name of file where data is stored, and is name of db
cursor=connection.cursor()

# read in txt file
try:
	snackFile = open("snacks.txt", "r") #open file
  	# get price, name, description, and stock values
	for line in snackFile:
		currentLine = line.split(",")
		price = currentLine[0]
		name = currentLine[1]
		description = currentLine[2]
		stock = currentLine[3]
		#insert values into database table
		cursor.execute("INSERT INTO product (bar_code, price, name, description, stock) values (NULL,?,?,?,?)", (price, name, description, stock))
	#save changes to database
	connection.commit() 
	connection.close()
except:
	print("Error, cannot open text file.")