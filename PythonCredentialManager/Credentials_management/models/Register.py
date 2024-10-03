import time 
import os

from termcolor import colored
from colorama import Style ,Fore

from DataBaseManagement import UserManager
from models.User import  User

class Register:

    def registration(self):
        usrManager = UserManager()

        loopRegistration = True      
        while loopRegistration: #USERNAME LOOP

            usrName = input(colored("Username : " , "green"))
            os.system("cls")
            if usrName == "":
                print(colored("[ Username can't be empty]" , "red"))
                time.sleep(1.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True
        while loopRegistration: #PASSWORD LOOP

            pwd = input(colored("Password : " , "green"))
            os.system("cls")

            if len(pwd) < 8:
                print(colored("[ Password can't be empty and it must be more or equal to 8 characters ]","red"))
                time.sleep(1.3)
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
                time.sleep(1.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True
        while loopRegistration: #EMAIL LOOP

            email = input(colored("Eamil : " , "green"))
            os.system("cls")
            if email == "":
                print(colored("[ Email can,t be empty ]", "red"))
                time.sleep(1.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")


        loopRegistration = True      
        while loopRegistration: #NUMBER PHONE LOOP
                
            numberPhone = input(colored("Phone : " , "green"))
            os.system("cls")
            if len(numberPhone) < 10 : 
                print(colored("[ Invalid number phone ]", "red"))
                time.sleep(1.3)
                os.system("cls")
            else:
                loopRegistration = False
                os.system("cls")

        userClass = User(usrName , pwd , name , email , numberPhone)
            
        if usrManager.checkUserExistance(usrName , email):
            print()
        else:
            usrManager.registerUser(userClass)