
import mysql.connector

class UserManager:

    def logIn(self, username,password):
       controll = False

       dataBase = mysql.connector.connect(
           host= "localhost",
           user= "rootALEX",
           password = "root2234A03",
           database = "credentials_management"
       )

       cursor = dataBase.cursor()

       sql_query = 'SELECT id_user FROM user WHERE username = %s AND pwd = %s'
       cursor.execute(sql_query,(username,password))

       usr = cursor.fetchone()
       dataBase.close()
       cursor.close()

       if usr: 
           print("Succesfully LogIn")

           controll = True
           id_user = usr[0]

           return controll
       else:
           print("Failed LogIn : invalid credentials")

    
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
           print("Failed LogIn : invalid credentials")

    