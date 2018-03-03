#Authors: Kim Krishnan, Tanya Wanwatankol, Derek Yee
#Topic: Using databases to create an online store
#=========================================================
import sqlite3
connection=sqlite3.connect("snackOverFlow.db")   #name of file where data is stored, and is name of db
cursor=connection.cursor()
cursor.execute("""DROP TABLE product""")        #for each table
cursor.execute("""DROP TABLE cart""")
cursor.execute("""DROP TABLE member""")
################################################################################     start creating tables 
#creating product table using python to sql
#table for product 
sql_command="""
CREATE TABLE product (                 
bar_Code INTEGER PRIMARY KEY,
price VALUE,  
name VARCHAR(20),
description VARCHAR(50),
stock AMOUNTSTOCK );"""
cursor.execute(sql_command)   #tells sql to create table
#table for cart 
sql_command="""                
CREATE TABLE cart  (               
cartID INTEGER PRIMARY KEY ,  
memberID CUSTOMER ,
items PRODUCTNAME
amountItem QUANTITYBOUGHT);"""#end 
cursor.execute(sql_command) 
#table for member                   NEEDS LOOKING AT 
sql_command="""
CREATE TABLE member (
memberID INTEGER PRIMARY KEY,
name VARCHAR(20),  
email VARCHAR(30),
password PIN 
dOB VARCHAR(9),
address VARCHAR(40));"""
cursor.execute(sql_command)    #end 
#######################################################################       end creating tables 



####################################################################### Inserting data into tables via files








######################################################################### end inserting data 


sql_command="""INSERT INTO product (bar_code, price, name, description, stock)
        VALUES (NULL, 5.32, "egg", "nice and yokey",30);"""
cursor.execute(sql_command)
connection.commit()           #do this to save changes

#GETTING DATA FROM TABLE SPECIFIED 
cursor.execute("SELECT * FROM product")
print("fetchall: ")
result= cursor.fetchall()
for x in result:
    print(x)


connection.close()


