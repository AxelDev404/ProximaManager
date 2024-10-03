import mysql.connector
from termcolor import colored

class CredentialManager:
    
    def conncet_db(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )
    

    def addCredentials(self , credentials , id_user_credentials):

        values = (id_user_credentials , credentials.password , credentials.username , credentials.email ,  credentials.product)

        db = self.conncet_db()

        cursor = db.cursor()

        sql_query = "INSERT INTO credentials (id_user_credentials , pwd , username , email , product) VALUES (%s , %s , %s , %s , %s)"

        cursor.execute(sql_query, (values))

        db.commit()

        print("Registartion complete!") 

    def noFilterSearch(self , id_user_credentials):

        sql_query = "SELECT id_credential , email , username, pwd , product FROM credentials WHERE id_user_credentials = %s"

        db = self.conncet_db()
        cursor = db.cursor()

        cursor.execute(sql_query , (id_user_credentials,)) #virgola

        credentials = cursor.fetchone()

        if credentials:
            id_credential = credentials[0]
            email = credentials[1]
            username = credentials[2]
            pwd = credentials[3]
            product = credentials[4]

            return colored(f"_______________________\n|\n| ID CREDENTIAL : {id_credential} \n|\n| EMAIL : {email} \n|\n| USERNAME : {username} \n|\n| PASSWORD : {pwd} \n|\n| PRODUCT : {product} \n|\n|_______________________\n","light_cyan")
        else:
            print("FATAL ERROR : no user was found!")

        