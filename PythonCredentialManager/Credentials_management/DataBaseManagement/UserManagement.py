from prettytable import PrettyTable
import mysql.connector 
from mysql.connector import Error
from colorama import Style ,Fore
from termcolor import colored
import time
import os

class UserManager:

    def connect_db(self):
        return mysql.connector.connect(
           host= "localhost",
           user= "username",
           password = "password",
           database = "credentials_management",
        )
       

    def logIn(self, username,password):

      #prova dinamico ovvero chiedi all utente di collegrsi al host senza farlo da codice user e pwd // metdo con query per fare il db personale senza farlo da sql alleggerire l utente

       db = self.connect_db()
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
       prettyTable = PrettyTable()

       db = self.connect_db()
       cursor = db.cursor()

       sql_query = 'SELECT id_user , nome , username, pwd , email , number_phone  FROM user WHERE username = %s AND pwd = %s'
       cursor.execute(sql_query,(username,password))
       
       usr = cursor.fetchall()

       column = [colored(desc[0] , "red") for desc in cursor.description]
       prettyTable.field_names = column

       if usr:  
            for row in usr:
             rowColored = [colored(x , "light_green") for x in row]
             prettyTable.add_row(rowColored)

            print(prettyTable ,  Fore.GREEN)   
       else:
           print(colored("Failed LogIn : invalid credentials","red"))


    def registerUser(self, userClass):
        
        values = (userClass.username , userClass.password , userClass.name , userClass.email , userClass.numberphone)

        db = self.connect_db()
        cursor = db.cursor()

        
        sql_query = "INSERT INTO user (username , pwd , nome , email , number_Phone) VALUES (%s , %s , %s , %s , %s)"

        cursor.execute(sql_query, (values))
        db.commit() #to push in db

        print("Registartion complete! Welcome in Credentials Manager")  
        time.sleep(1.3)


    def checkUserExistance(self, username , email):

        controllCheckUser = False
        db = self.connect_db()
        cursor = db.cursor()

        cursor = db.cursor()
            
        sql_query = "SELECT username , email FROM user WHERE username = %s OR email = %s"
        cursor.execute(sql_query , (username,email))

        usr = cursor.fetchone()

        cursor.close()
        db.close()

        if usr:
            controllCheckUser = True
            print(Style.BRIGHT+colored("User already exist! Try again" ,"red"))
            return controllCheckUser
        else:
            controllCheckUser = False
            return controllCheckUser
            
     
    def getUsername(self, username,password): #do get id method

        db = self.connect_db()
        cursor = db.cursor()

        sql_query = 'SELECT username  FROM user WHERE username = %s AND pwd = %s'

        cursor.execute(sql_query,(username , password))

        usr = cursor.fetchone()

        cursor.close()
        db.close()

        if usr:
            usern = usr[0]
            return usern


    def getId(self,username , password):

        db = self.connect_db()
        cursor = db.cursor()   

        sql_query = "SELECT id_user FROM user WHERE username = %s AND pwd = %s"

        cursor.execute(sql_query , (username , password))

        usr = cursor.fetchone()

        if usr:
            id_user = usr[0]
            return id_user
        else:
            print("FATAL ERROR : No user was found")

    def updateUsername(self , id_user , logInNewUsername):
        db = self.connect_db()
        cursor = db.cursor()

        sql_query = "UPDATE user SET username = %s WHERE id_user = %s"
        cursor.execute(sql_query , (logInNewUsername , id_user))
        
        db.commit()

        if cursor.rowcount > 0:
            print(colored("Username correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    def updatePassword(self, id_user , logInNewPassword):
        db = self.connect_db()
        cursor = db.cursor()

        sql_query = "UPDATE user SET pwd = %s WHERE id_user = %s"
        cursor.execute(sql_query , (logInNewPassword , id_user))
        
        db.commit()

        if cursor.rowcount > 0:
            print(colored("Passsword correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    def updateEmail(self , id_user , logInNewEmail):
        db = self.connect_db()
        cursor = db.cursor()

        sql_query = "UPDATE user SET email = %s WHERE id_user = %s"
        cursor.execute(sql_query , (logInNewEmail , id_user))

        db.commit()

        if cursor.rowcount > 0:
            print(colored("Email correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))


    def deleteUser(self , id_user):
        db = self.connect_db()
        cursor = db.cursor()

        sql_query = "DELETE FROM user WHERE id_user = %s"
        cursor.execute(sql_query , (id_user,))

        db.commit()

        if cursor.rowcount > 0:
            print(colored("Accout deleted","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    