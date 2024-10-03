
from termcolor import colored
from colorama import Style ,Fore
import pwinput 

import os
import time

from Menu.MenuManagement import MenuManagement
from DataBaseManagement import UserManager
from models.User import  User
from models.Register import Register

def main():

    usrManager = UserManager()
    menuManagement = MenuManagement()
    
    loop = True
    
    while loop:
        os.system('cls')
        menuManagement.exportMenuPrincipal()
        selection = input(Style.BRIGHT+colored("root","green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

        if selection == "1":
            os.system('cls')
            
            username = input("Username : ")
            password = pwinput.pwinput(prompt=("Passowrd : "))

            loopUser = True
            counterAlert = 0

            while usrManager.logIn(username , password) and loopUser:

                if counterAlert < 1:
                    print(colored("Sucessfull logIn","green"))
                    time.sleep(1.3)
                    os.system('cls')   
                elif counterAlert > 1:
                    print()

                menuManagement.exportUserMenu()
                selectionUser = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                
                if selectionUser == "1":
                    os.system('cls')

                    print(usrManager.profile(username,password))
                    enter = input("Press enter to quit :")

                    counterAlert+=1
                    os.system('cls')
                elif selectionUser == "2":
                    os.system('cls')

                    print(colored("WORK IN PROGRESS!","red"))
                    time.sleep(1.3)
                    os.system('cls')
                    
                    counterAlert+=1
                elif selectionUser == "3":
                    loopUser = False

                elif not (selectionUser == "1" or selectionUser == "2" or selectionUser == "3"):
                    os.system('cls')

                    print(Style.BRIGHT+colored("Invalid Choice","red"))
                    time.sleep(1.3)
                    os.system('cls')

                    counterAlert+=1

        elif selection == "2":
            os.system('cls')

            register = Register()
            
            register.registration()

            enter = input(Style.BRIGHT+colored("Press enter to exit : ","green"))

        elif selection == "3":
            os.system('cls')
            loop = False

        elif not(selection == "1" or selection == "2" or selection == "3"):
            os.system('cls')

            print(Style.BRIGHT+colored("Invalid Choice","red"))
            time.sleep(1.1)
            os.system('cls')


    print("Goodbye")

if __name__ == "__main__":

    main()