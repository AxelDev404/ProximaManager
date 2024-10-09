import mysql.connector
import time
from termcolor import colored
from colorama import Style ,Fore
from prettytable import PrettyTable


class CredentialManager:
    
    def conncet_db(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "username",
            password = "password",
            database = "credentials_management",
        )
    

    def addCredentials(self , credentials , id_user_credentials):

        values = (id_user_credentials , credentials.password , credentials.username , credentials.email ,  credentials.product)

        db = self.conncet_db()

        cursor = db.cursor()

        sql_query = "INSERT INTO credentials (id_user_credentials , pwd , username , email , product) VALUES (%s , %s , %s , %s , %s)"

        cursor.execute(sql_query, (values))

        db.commit()

        print("Registartion complete!")
        time.sleep(3.2) 

    def noFilterSearch(self , id_user_credentials):
        prettytab = PrettyTable()

        sql_query = "SELECT id_credential , email , username, pwd , product FROM credentials WHERE id_user_credentials = %s"

        db = self.conncet_db()
        cursor = db.cursor()

        cursor.execute(sql_query , (id_user_credentials,)) #virgola

        credentials = cursor.fetchall()
        
        columns = [colored(desc[0],"red") for desc in cursor.description]
        prettytab.field_names = columns
        
        if credentials:
           for row in credentials:
               rowColored = [colored(x , 'light_green') for x in row]
               prettytab.add_row(rowColored)

           print(prettytab,Fore.GREEN)
        else:
            print(colored("no credentials found!" ,"red"))


    def idFilterSearch(self , id_user_credentials , id_credential):
            
        prettytab = PrettyTable()

        sql_query = "SELECT email , username , pwd , product FROM credentials WHERE id_user_credentials = %s AND id_credential = %s"

        db = self.conncet_db()

        cursor = db.cursor()

        cursor.execute(sql_query , (id_user_credentials , id_credential))

        credentials = cursor.fetchall()
        columns = [colored(desc[0],'red') for desc in cursor.description]
        prettytab.field_names = columns
            
        if credentials:

            for row in credentials:
                rowColored = [colored(x , 'light_green') for x in row]
                prettytab.add_row(rowColored)

            print(prettytab , Fore.GREEN)
        else:
            print(colored("no credentials found for this id!" , "light_red"))
        

    def usernameFilterSearch(self ,id_user_credentials , username):
        prettyTable = PrettyTable()

        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "SELECT email , username , pwd , product FROM credentials WHERE id_user_credentials = %s AND username = %s"

        cursor.execute(sql_query , (id_user_credentials , username))
        credentials = cursor.fetchall()

        columns = [colored(desc[0],"red") for desc in cursor.description]

        prettyTable.field_names = columns

        if credentials:

            for row in credentials:
                rowColored = [colored(x , "light_green") for x in row]
                prettyTable.add_row(rowColored)

            print(prettyTable , Fore.GREEN)
        else: 
            print(colored("no credentials found for this username!","red"))
    

    def emailFilterSearch(self, id_credentials_user , email):
        prettyTable = PrettyTable()

        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "SELECT email , username , pwd , product FROM credentials WHERE id_user_credentials = %s AND email = %s"
        cursor.execute(sql_query , (id_credentials_user , email))

        credetials = cursor.fetchall() 

        columns =[colored(desc[0] , "red") for desc in cursor.description]
        prettyTable.field_names = columns

        if credetials:
            for row in credetials:
                rowColored = [colored(x , "light_green") for x in row]
                prettyTable.add_row(rowColored)

            print(prettyTable , Fore.GREEN)  
        else:
            print(colored("no credentials found for this email!","red"))


    def productFilterSeacrh(self , id_user_credentials , product):
        prettyTable = PrettyTable()

        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "SELECT email , username , pwd , product FROM credentials WHERE id_user_credentials = %s AND product = %s"
        cursor.execute(sql_query , (id_user_credentials , product))

        credentials = cursor.fetchall()

        columns = [colored(desc[0] , "red") for desc in cursor.description]
        prettyTable.field_names = columns

        if credentials:
            for row in credentials:
                rowColored = [colored(x , "light_green") for x in row]
                prettyTable.add_row(rowColored)

            print(prettyTable , Fore.GREEN)
        else:
            print(colored("no credentials was found for this service!" , "red"))


    def deleteRow(self , id_user_credentials , id_credential):
        
        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "DELETE FROM credentials WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sql_query , (id_user_credentials , id_credential))

        credential = cursor.fetchone()

        db.commit()

        if credential:
            print(colored("Credential correctly deleted!","green"))
            time.sleep(4.1)
        else:
            print(colored("no credentials found for this id!","red"))
    

    def updatePassword(self, id_user_credentials , id_credential , updatePassword):
        
        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "UPDATE credentials SET pwd = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sql_query , (updatePassword , id_user_credentials , id_credential))

        db.commit()

        if cursor.rowcount>0: #controll on id user
            print(colored("Password was correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))


    def updateEmail(self, id_user_credentials , id_credential , updateEmail):

        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "UPDATE credentials SET email = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sql_query , (updateEmail , id_user_credentials , id_credential))

        db.commit()

        if cursor.rowcount>0: #controll on id user
            print(colored("Email was correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))


    def updateUsername(self, id_user_credentials , id_credential , updateUsername):

        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "UPDATE credentials SET username = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sql_query , (updateUsername , id_user_credentials , id_credential))

        db.commit()

        if cursor.rowcount > 0:
            print(colored("Username was correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    def updateProduct(self , id_user_credentials, id_credential , updateProduct): #DECIDE TO USE
        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "UPDATE credentials SET product = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sql_query , (updateProduct , id_user_credentials , id_credential))

        db.commit()

        if cursor.rowcount > 0:
            print(colored("Product was correctly updated!","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    
    def deleteAllWithUser(self , id_user_credentials):
        db = self.conncet_db()
        cursor = db.cursor()

        sql_query = "DELETE FROM credentials WHERE id_user_credentials = %s"
        cursor.execute(sql_query , (id_user_credentials,))

        db.commit()

        if cursor.rowcount > 0:
            print(colored("All credentials was deleted from database","green"))
        else:
            print(colored("invald to update for this id because it dosen't exist!" , "red"))

    