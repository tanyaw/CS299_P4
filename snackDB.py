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
password PIN, 
berf DOB,
address VARCHAR(40));"""
cursor.execute(sql_command)    #end
#######################################################################       end creating tables 



####################################################################### Inserting data into tables via files








######################################################################### end inserting data 

''
sql_command="""INSERT INTO product (bar_code, price, name, description, stock)
        VALUES (NULL, 5.32, "egg", "nice and yokey",30);"""
cursor.execute(sql_command)

sql_command="""INSERT INTO product (bar_code, price, name, description, stock)
        VALUES (NULL, 5.32, "bacon", "bacony",30);"""
cursor.execute(sql_command)

sql_command="""INSERT INTO product (bar_code, price, name, description, stock)
        VALUES (NULL, 5.32, "cheese", "cheesey",30);"""
cursor.execute(sql_command)


sql_command="""INSERT INTO member (memberID,name,email,password,berf,address)
            VALUES (NULL,"Tanya","tanya@cpp.edu", 0000, "01/02/03",111);"""
cursor.execute(sql_command) 

sql_command="""INSERT INTO member (memberID,name,email,password,berf,address)
            VALUES (NULL,"Tanya2","tanya1@cpp.edu", 0001, "02/02/03",113);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO member (memberID,name,email,password,berf,address)
            VALUES (NULL,"Tanya3","tanya13@cpp.edu", 0002, "03/02/03",114);"""
cursor.execute(sql_command)

connection.commit()           #do this to save changes

#GETTING DATA FROM TABLE SPECIFIED 
cursor.execute("SELECT * FROM member")
print("fetchall: ")
result= cursor.fetchall()
for x in result:
    print(x)


connection.close()


