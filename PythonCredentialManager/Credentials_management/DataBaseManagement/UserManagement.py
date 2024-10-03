
import mysql.connector 
from mysql.connector import Error
from colorama import Style ,Fore
from termcolor import colored
import time
import os


class UserManager:

    def connect_db():
        return mysql.connector.connect(
           host= "localhost",
           user= "rootALEX",
           password = "root2234A03",
           database = "credentials_management"
       )
       

    def logIn(self, username,password):

       db = mysql.connector.connect(
           host= "localhost",
           user= "rootALEX",
           password = "root2234A03",
           database = "credentials_management"
       )

       cursor = db.cursor()

       sql_query = 'SELECT id_user FROM user WHERE username = %s AND pwd = %s'
       cursor.execute(sql_query,(username,password))

       usr = cursor.fetchone()
       db.close()
       cursor.close()

       if usr: 
           return True
       else:    
           print(colored("Failed LogIn : invalid credentials","red"))
           time.sleep(1.3)
           os.system('cls')

           return False
       
    
    def profile(self, username,password):
       controll = False

       dataBase = mysql.connector.connect(
           host= "localhost",
           user= "rootALEX",
           password = "root2234A03",
           database = "credentials_management"
       )

       cursor = dataBase.cursor()

       sql_query = 'SELECT id_user , nome , username , email , number_phone  FROM user WHERE username = %s AND pwd = %s'
       cursor.execute(sql_query,(username,password))

       usr = cursor.fetchone()
       dataBase.close()
       cursor.close()

       if usr:  
           controll = True

           id_user = usr[0]
           name = usr[1]
           username_db = usr[2]
           email = usr[3]
           numberPhone = usr[4]

           return f"\n\n| ID : {id_user} \n|\n| NAME : {name} \n|\n| USERNAME : {username_db} \n|\n| EMAIL : {email} \n|\n| PHONE : {numberPhone} \n\n"
       else:
           print(colored("Failed LogIn : invalid credentials","red"))


    def registerUser(self, userClass):
        
        values = (userClass.username , userClass.password , userClass.name , userClass.email , userClass.numberphone)

        dataBase = mysql.connector.connect(
            host ="localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )

        #try:
        cursor = dataBase.cursor()
        sql_query = "INSERT INTO user (username , pwd , nome , email , number_Phone) VALUES (%s , %s , %s , %s , %s)"

        cursor.execute(sql_query, (values))
        dataBase.commit() #to push in db

        print("Registartion complete! Welcome in Credentials Manager")  
        time.sleep(1.3)

        #except mysql.connector.Error as err :
        #    print("SQL error!")
        #    time.sleep(1.3)

       # finally:
        #    cursor.close()
        #    dataBase.close()


    def checkUserExistance(self, username , email):

        controllCheckUser = False

        dataBase = mysql.connector.connect(
            host ="localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )

        cursor = dataBase.cursor()
            
        sql_query = "SELECT username , email FROM user WHERE username = %s OR email = %s"
        cursor.execute(sql_query , (username,email))

        usr = cursor.fetchone()

        cursor.close()
        dataBase.close()

        if usr:
            controllCheckUser = True
            print(Style.BRIGHT+colored("User already exist! Try again" ,"red"))
            return controllCheckUser
        else:
            controllCheckUser = False
            return controllCheckUser
            
     
    def getUsername(self, username,password): #do get id method
        controll = False

        dataBase = mysql.connector.connect(
            host ="localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )

        sql_query = 'SELECT username  FROM user WHERE username = %s AND pwd = %s'

        cursor = dataBase.cursor()
        cursor.execute(sql_query,(username , password))

        usr = cursor.fetchone()

        cursor.close()
        dataBase.close()

        if usr:
            controll = True

            usern = usr[0]
            return usern


    def getId(self,username , password):

        dataBase = mysql.connector.connect(
            host = "localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )    

        cursor = dataBase.cursor()

        sql_query = "SELECT id_user FROM user WHERE username = %s AND pwd = %s"

        cursor.execute(sql_query , (username , password))

        usr = cursor.fetchone()

        if usr:
            id_user = usr[0]
            return id_user
        else:
            print("FATAL ERROR : No user was found")
        
    