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


##Prints out items from proudct table
# reads data base, puts desired elements into sectioned lists. 
# @return None
def displayProducts(c):
    names=['NAMES']
    price=['PRICES']
    description=['DESCRIPTION']
    stock=['STOCK']
    c.execute("SELECT * FROM product")
    result= c.fetchall()
    for r in result:
        names.append(r[2])
        price.append(r[1])
        description.append(r[3])
        stock.append(r[4])
    
    for i in range(len(names)):
        line_new = '{:<20}  {:<20}  {:<20}  {:<20}'.format(str(names[i]),str(price[i]), str(description[i]),str(stock[i]))
        print(line_new)
'''
    c.execute("SELECT * FROM member")
    result =c.fetchall()
    print(result)
'''
##Prints out items from cart table
# reads data base, puts desired elements into sectioned lists. 
# @return None
def displayCart(c):
        items=['ITEMS']  #items 
        amount=['AMOUNT'] #amountItem
        c.execute("SELECT * FROM cart")
        result=c.fetchall()
        for r in result:
                items.append(r[1])
                amount.append(r[2])
        for i in range(len(items)):
                line_new = '{:<20}  {:<20}\n'.format(str(items[i]),str(amount[i]))
                print(line_new)
          

##ADDS TO CART given user input
#will use sql method to put desired data into table
#@return none 
def addToCart(name, amount, pricePer, c):
        c.execute("INSERT INTO cart (cartID, itemName, amountItem, pricePerUnit) values (NULL,?,?,?)",(name, amount, pricePer))#add info to database table "cart"
        print("added: ",name, "in the quanity of: ",str(amount), " at the price per unit of: ", str(pricePer)) #printing confirmation



##checks if product name user entered is in database, will return the price. Returns -1 if not in database 
def checkInProd(item,c):
        try:
                c.execute('''SELECT price FROM product WHERE name=?''',(item,))       #statement to access the item name the user entered
                retrieved=c.fetchall() #retrieves line if it is there
                if(retrieved is not None):
                        retrieved=float(list(retrieved[0])[0]) #retrieved returned as a list of tuples, so converting tuple down to element to cast to float
                        return retrieved
                
        except:      #if not found, returns dummy value that will be caught 
                return -1

##
def updateStock(c, numToTake, itemName):
       
                c.execute('''SELECT stock from product WHERE name=?''',(itemName,))
                retrieved=c.fetchall()
                if(retrieved is not None):
                        retrieved=int(list(retrieved[0])[0])
                if(numToTake<=retrieved):
                        remaining=retrieved-numToTake
                        c.execute(''' UPDATE product SET stock =? WHERE name=?''',(remaining,itemName))
                        return True                 #return True means successfully updated 
                else:
                        return False
                



#checks if product in cart based on user input
def deleteInCart(item,c):
        try:
                c.execute('''DELETE FROM cart WHERE itemName=?''',(item,)) #sql statement to delete 
                print("Deleted ",item," from your cart.") #printing confirmation
        except:
                print("Selected item is not in the cart.")


##calculats sum of all items in cart, and prints receipt 
def calcSumOfCart(c):
        itemNames=[]           #creating lists to store from table to print 
        itemAmount=[]
        itemPrice=[]
        subTotal=[]
        totalPrice=0
        c.execute("SELECT  * FROM cart")
        result=c.fetchall()
        for x in result:                        #storing info into lists to use to calculate price total
                itemNames.append(x[1])
                itemAmount.append(x[2])
                itemPrice.append(x[3])
        print(itemNames)
        print(itemAmount)
        print(itemPrice)
        for i in range(len(itemNames)):           #looping through list and calculating price, summing them up all together 
                totalPrice=totalPrice+(int(itemAmount[i])*float(itemPrice[i]))
                subTotal.append(round((int(itemAmount[i])*float(itemPrice[i])),2))   #calculating item price *amount purchased to get subtotal of that item, adds to list 
        print(subTotal)
        print("SNACKOVERFLOW RECEIPT: \n")
        line_new = '{:<20}  {:<18}  {:<18}  {:<18}'.format(" ITEM "," AMOUNT "," PRICE/UNIT "," SUBTOTAL ")
        print(line_new)
        for x in range(len(itemNames)):
                line_new = '{:<20}  {:<20}  {:<20}  {:<20}'.format(str(itemNames[x]),str(itemAmount[x]), str(itemPrice[x]),str(subTotal[x]))
                print(line_new)
        totalPrice=round(totalPrice,2)
        print("THE TOTAL TO BE PAID: $",totalPrice)
        

        
##Displays Registration Form to console
# @param None
# @return None
def register(c):
        print("--- SNACKER REGISTRATION ---")
        name = input("Please enter your username: ")
        email = input("Please enter your email address: ")
        pin = input("Please enter a 4-digit passcode: ")
        BoD = input("Please enter your birthday day(MM/DD/YYYY): ")
        address = input("Please enter your address: ")
        
        #SQL COMMAND: Add info to database
        c.execute("INSERT INTO member (memberID, name, email, password, berf, address) values (NULL,?,?,?,?,?)", (name, email, pin, BoD, address))
        print("Thank you for registering today!\nWe're returning you to the main menu")
        
#Displays Menu Options to console
# @param None
# @return None
def mainMenu():
        print("\n--- MENU OPTIONS ---")
        print("1. Register as new snacker.")
        print("2. Go shopping.")
        print("3. Exit.\n")


def shoppingMenu(c):
        c.execute(''' DELETE FROM cart''')  #clears cart table for new user 
        while (True):
                print("\n--- SNACKS IN STOCK ---")
                displayProducts(c)

                print("\n--- Shopping Options ---")
                print("1. Add item to Cart.")
                print("2. Remove item from Cart.")
                print("3. View Cart items.")
                print("4. Go to checkout.")
                print("5. Exit shopping.")
                userShop = int(input("Please enter a shopping selection (1|2|3|4|5): "))

                if (userShop == 1):
                        #SQL COMMAND: Insert item from cart
                        item=input("Please enter the name of the product you would like to add: ")
                        priceOfItem=checkInProd(item, c)       #gets price of item from database, it will be -1 if not in db
                        if(priceOfItem==-1):
                                print("We do not carry this item. Returning back to shopping menu.")
                        else:
                                amount=int(input("Please enter the amount you would like to get: "))
                                if(not updateStock(c,amount,item)):
                                        print("We do not have enough in stock.")
                                else:
                                        addToCart(item,amount,priceOfItem,c)
                elif (userShop == 2):
                        #SQL COMMAND: Delete item from cart
                        itemName=input("Please enter the item name in your cart that you would like to delete: ")
                        deleteInCart(itemName,c)
                elif (userShop == 3):
                          print("\ncart contains: ")
                          displayCart(c)
                elif (userShop == 4):
                        #Calcualte total of all items in shoppingCart
                        calcSumOfCart(c)
                        
                elif (userShop == 5):
                        print("Thank you for your purchase(s)!\n")
                        return
                else:
                        print("ERROR: This is an invalid choice, please try again.\n")



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
                                return True             #Correct password
                        else:
                                return False    #Wrong password
        else:
                print("You are not a registered snacker!\n")
                return False


##Displays exit prompt to console
# @param None
# @return None
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
#@method: isInt
#@param: a string
#description: tests to see if string is integer, return False if isnt 
def isInt(x):
        try:
                int(x)
                return True
        except:
                return False 

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
                mainMenu()
                userChoice =(input("Please enter a menu selection (1|2|3): "))
                if(isInt(userChoice)):
                        userChoice=int(userChoice)
                elif(not isInt(userChoice)):
                        print("ERROR: Invalid choice, please try again.\n")
                        continue
                if (userChoice == 1):
                        register(cursor)
                elif (userChoice == 2):
                        ERROR = 0
                        while ( ERROR< 3 ):
                                print("\n--- PLEASE LOGIN ---")
                                userName = input("Please enter your username: ")
                                pin = input("Please enter your pin: ")

                                if ( verifyPin(userName, pin, cursor) ):
                                        shoppingMenu(cursor)
                                        break
                                else:
                                        ERROR += 1

                        if(ERROR == 3):
                                print("Sorry, you inputted the wrong pin too many times.\nWe're returning you to the main menu.\n")

                elif (userChoice == 3):
                        print("Thank you for snacking with us today.\nWe look forward to seeing you again!\n")
                        exitDisplay()
                        exit(0)
                elif (userChoice==4):
                        displayProducts(cursor)
                else:
                        print("ERROR: This is an invalid choice, please try again.\n")


#Calls main function
main()


