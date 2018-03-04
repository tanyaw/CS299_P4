#Authors: Kim Krishnan, Tanya Wanwatankol, Derek Yee
#Assignment: Group Project #1
#Topic: Using SQLite3 and Python to simulate online store
#=========================================================

import sqlite3
connection=sqlite3.connect("snackOverFlow.db")   #Name of file where data is stored/Name of db
cursor=connection.cursor()
#cursor.execute("""DROP TABLE product""")        #for each table
#cursor.execute("""DROP TABLE cart""")
#cursor.execute("""DROP TABLE member""")

################################################################################     Start creating tables 
#Create tables in db

#Table for products
sql_command="""
CREATE TABLE product (                 
bar_Code INTEGER PRIMARY KEY,
price VALUE,  
name VARCHAR(20),
description VARCHAR(50),
stock AMOUNTSTOCK );"""
cursor.execute(sql_command)   #tells sql to create table

#Table for cart history
sql_command="""                
CREATE TABLE cart  (               
cartID INTEGER PRIMARY KEY ,  
memberID CUSTOMER ,
items PRODUCTNAME
amountItem QUANTITYBOUGHT);"""#end 
cursor.execute(sql_command) 

#Table for member
sql_command="""
CREATE TABLE member (
memberID INTEGER PRIMARY KEY,
name VARCHAR(20),  
email VARCHAR(30),
password VARCHAR(4), 
berf DOB,
address VARCHAR(40));"""
cursor.execute(sql_command)

#Save and Close db connection
connection.commit()           #do this to save changes
connection.close()

