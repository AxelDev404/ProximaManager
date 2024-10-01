#print(dataBase)
#result = cursor.fetchall() #searching the query instructin

#for x in result: #printing the result with a cycle
 #   print(x)
 #user = User('test','testtest' , 'testtest' , '1234567890')



from termcolor import colored
import pwinput 
import mysql.connector
import os
from models import  User
from DataBaseManagement import UserManager

def main():

    usrManager = UserManager()

    dataBase = mysql.connector.connect( 
        host = "localhost",
        user = "root",
        password = "root2234A03",
        database = "credentials_management"
    )

    cursor = dataBase.cursor()

    loop = True
    loopUser = True

    while loop:
        os.system('cls')
        print(colored("+_____<CREDENTIALS MANAGER>_____+","magenta"))
        print(colored("|                               |","green"))
        print("|           [1] LogIn           |")
        print("|                               |")
        print("|           [2] Register        |")
        print("|                               |")
        print("|           [3] Quit            |")
        print("+_______________________________+")

        selection = input(">_ : ")

        if selection == "1":
         os.system('cls')

         username = input("Username : ")
         password = pwinput.pwinput(prompt=("Passowrd : "))

            
         if usrManager.logIn(username,password) == True:
            while loopUser:
                os.system('cls')
                print("TEST STRING [2] TO EXIT")

                selectionUser = input(">_ : ")

                if selectionUser == "2":
                 loopUser = False

                elif selectionUser == "1":
                   print(usrManager.profile(username,password))

                   enter = input("Press enter to quit :")
                   os.system('cls')
                   
                        
        elif selection == "2":
            print("2")
            os.system('cls')
        elif selection == "3":
            print("3")
            os.system('cls')
            loop = False

    print("Goodbye")

if __name__ == "__main__":

    main()