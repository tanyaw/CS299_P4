#import database
import sqlite3
connection=sqlite3.connect("snackOverFlow.db")   #name of file where data is stored, and is name of db
cursor=connection.cursor()

# read in txt file
try:
        snackFile = open("members.txt", "r") #open file
        # get memberID, name, email, berf, address values from text file
        for line in snackFile:
                currentLine = line.split(",")
                name = currentLine[0]
                email = currentLine[1]
                passCode=currentLine[2]
                berf = currentLine[3]
                address = currentLine[4]
                print(name, email, passCode, berf, address)
                #insert values into database table
                cursor.execute("INSERT INTO member (memberID, name, email, password, berf, address) values (NULL,?,?,?,?,?)", (name, email, passCode, berf, address))
        #save changes to database
        connection.commit() 
        connection.close()
        snackFile.close()               
except:
        print("Error, cannot open text file.")
