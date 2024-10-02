
from termcolor import colored
from colorama import Style ,Fore
import pwinput 
import mysql.connector
import os
from models.User import  User
import time 
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
        print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
        print(colored("|                                 |","red"))
        print(colored("|     ","red")+Style.BRIGHT+colored("< CREDENTIALS MANAGER >" , "red")+colored("     |","red"))
        print(colored("|_________________________________|","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("           [1] LogIn        ","green",)+colored("     |","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("           [2] Register        ","green")+colored("  |","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("           [3] Quit        ","green")+colored("      |","red"))
        print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
        print()
        selection = input(Style.BRIGHT+colored("root","green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

        if selection == "1":
         os.system('cls')

         username = input("Username : ")
         password = pwinput.pwinput(prompt=("Passowrd : "))

            
         if usrManager.logIn(username,password) == True:
            while loopUser:
                os.system('cls')
                print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
                print(colored("|                                 |","red"))
                print(colored("|     ","red")+Style.BRIGHT+colored(" <     MAIN MENU     >" , "red")+colored("      |","red"))
                print(colored("|_________________________________|","red"))
                print(colored("|                                 |","red"))
                print(colored("|","red")+Style.BRIGHT+colored("        [1] Profile        ","green",)+colored("      |","red"))
                print(colored("|                                 |","red"))
                print(colored("|","red")+Style.BRIGHT+colored("        [2] Add Credentials   ","green")+colored("   |","red"))
                print(colored("|                                 |","red"))
                print(colored("|","red")+Style.BRIGHT+colored("        [3] Quit        ","green")+colored("         |","red"))
                print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
                print()

                selectionUser = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                
                if selectionUser == "1":
                  os.system('cls')

                  print(usrManager.profile(username,password))
                  enter = input("Press enter to quit :")

                  os.system('cls')

                elif selectionUser == "3":
    
                   loopUser = False
                   
        elif selection == "2":
            os.system('cls')

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

            os.system("cls")
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

            enter = input(Style.BRIGHT+colored("Press enter to exit : ","green"))

        elif selection == "3":
            os.system('cls')
            loop = False

    print("Goodbye")

if __name__ == "__main__":

    main()