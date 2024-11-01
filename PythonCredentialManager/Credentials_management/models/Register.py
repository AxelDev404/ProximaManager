import time 
import os

from termcolor import colored
from colorama import Style ,Fore

from DataBaseManagement import UserManager
from DataBaseManagement import CredentialManager
from models.User import  User
from models.Credential import Credentials

class Register:

    def registrationUSER(self):
        usrManager = UserManager()

        loopRegistration = True      
        while loopRegistration: #USERNAME LOOP

            usrName = input(colored("Username : " , "green"))
            os.system("cls")
            if usrName == "" or len(usrName) > 50:
                print(colored("[ Username can't be empty]" , "red"))
                time.sleep(4.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True
        while loopRegistration: #PASSWORD LOOP

            pwd = input(colored("Password : " , "green"))
            os.system("cls")

            if len(pwd) < 8 or len(pwd) > 50 :
                print(colored("[ Password can't be empty and it must be more or equal to 8 characters and can't have blank space ]","red"))
                time.sleep(5.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True
        while loopRegistration: #NAME LOOP

            name = input(colored("Name : " , "green"))
            os.system("cls")

            if name == "":
                print(colored("[ Name can't be empty ]", "red"))
                time.sleep(4.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True
        while loopRegistration: #EMAIL LOOP

            email = input(colored("Eamil : " , "green"))
            os.system("cls")
            if email == "" or len(email) > 200:
                print(colored("[ Email can,t be empty ]", "red"))
                time.sleep(4.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True      
        while loopRegistration: #NUMBER PHONE LOOP
                
            numberPhone = input(colored("Phone : " , "green"))
            os.system("cls")
            if len(numberPhone) < 10 or len(numberPhone) > 10 : 
                print(colored("[ Invalid number phone ]", "red"))
                time.sleep(4.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")

        userClass = User(usrName , pwd , name , email , numberPhone)
            
        if usrManager.checkUserExistance(usrName , email):
            print()
        else:
            usrManager.registerUser(userClass)

    
    def registerCredentials(self):
        print()

        loop = True

        while loop:

            email = input(colored("Email : " , "green"))
            os.system('cls')

            if email == "" or len(email) > 200:
                print(colored("[ Email can,t be empty ]", "red"))
                time.sleep(4.3)
                os.system("cls")
            else:
                loop = False
        
        loop = True

        while loop:

            username = input(colored("Username : " , "green"))
            os.system('cls')

            if username == "" or len(username) > 50:
                print(Style.BRIGHT+colored("[ ADVISE (Empty Value) : Username can be added leater in < Settings-credentials > ]" , "yellow"))
                time.sleep(3.3)
                os.system("cls")
                loop = False

        loop = True

        while loop:

            password = input(colored("Password : " , "green"))
            os.system('cls')

            if password == "" or len(password) > 50:
                print(colored("[ Password can't be empty ]" , "red"))
                time.sleep(4.1)
                os.system("cls")
            else:
                loop = False

        loop = True

        while loop:

            product = input(colored("Service : " , "green"))
            os.system('cls')

            if product == "" or len(product) > 200:
                print(colored("[ Product can't be empty ]" , "red"))
                time.sleep(4.1)
                os.system("cls")
            else:
                loop = False


        credentials = Credentials(password , username , email , product)

        credentialsManager = CredentialManager()
        userManager = UserManager()
        userManager.getId()

        credentialsManager.addCredentials(credentials , userManager.getId())
        


            

            

