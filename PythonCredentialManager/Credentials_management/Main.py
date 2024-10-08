
from termcolor import colored
from colorama import Style ,Fore
import pwinput 
import os
import time
from Menu.MenuManagement import MenuManagement
from DataBaseManagement import UserManager
from DataBaseManagement import CredentialManager
from models.User import  User
from models.Credential import Credentials
from models.Register import Register

def main():
    os.system('cls')

    usrManager = UserManager()
    crdManager = CredentialManager()

    menuManagement = MenuManagement()
    register = Register()

    loop = True

    while loop:
        os.system('cls')
        menuManagement.exportMenuPrincipal()
        selection = input(Style.BRIGHT+colored("root","green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))


        if selection == "1":
            #  _                ___       
            # | |    ___   __ _|_ _|_ __  
            # | |   / _ \ / _` || || '_ \ 
            # | |__| (_) | (_| || || | | |
            # |_____\___/ \__, |___|_| |_|
            #             |___/           

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

                #MAIN MENU

                menuManagement.exportUserMenu()
                selectionUser = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                

                if selectionUser == "1":
                    # __     ___                 ____             __ _ _      
                    # \ \   / (_) _____      __ |  _ \ _ __ ___  / _(_) | ___ 
                    #  \ \ / /| |/ _ \ \ /\ / / | |_) | '__/ _ \| |_| | |/ _ \
                    #   \ V / | |  __/\ V  V /  |  __/| | | (_) |  _| | |  __/
                    #    \_/  |_|\___| \_/\_/   |_|   |_|  \___/|_| |_|_|\___|
                                                                                                  
                    os.system('cls')

                    print(usrManager.profile(username,password))
                    enter = input("Press enter to quit :")

                    counterAlert+=1
                    os.system('cls')

                elif selectionUser == "2":
                    #  ____                    ____              _            _   _       _     
                    # |  _ \ _ __ ___  __ _   / ___|_ __ ___  __| | ___ _ __ | |_(_) __ _| |___ 
                    # | |_) | '__/ _ \/ _` | | |   | '__/ _ \/ _` |/ _ \ '_ \| __| |/ _` | / __|
                    # |  _ <| | |  __/ (_| | | |___| | |  __/ (_| |  __/ | | | |_| | (_| | \__ \
                    # |_| \_\_|  \___|\__, |  \____|_|  \___|\__,_|\___|_| |_|\__|_|\__,_|_|___/
                    #                 |___/                                                     
                                                                                                                                                                                    
                    os.system('cls')
                                
                    loop = True
                    while loop:
                        emailCredentials = input(colored("Email : " , "green"))
                        os.system('cls')
                        if emailCredentials == "":
                            print(colored("[ Email can,t be empty ]", "red"))
                            time.sleep(1.3)
                            os.system("cls")
                        else:
                            loop = False
                    loop = True
                    while loop:
                        usernameCredentials = input(colored("Username : " , "green"))
                        os.system('cls')
                        if usernameCredentials == "" or not(usernameCredentials == ""):
                            print(Style.BRIGHT+colored("[ ADVISE : Username can be olso added leater in < Settings-credentials > ]" , "yellow"))
                            time.sleep(3.3)
                            os.system("cls")
                            loop = False
                    loop = True
                    while loop:
                        passwordCredentials = input(colored("Password : " , "green"))
                        os.system('cls')
                        if passwordCredentials == "":
                            print(colored("[ Password can't be empty ]" , "red"))
                            time.sleep(1.1)
                            os.system("cls")
                        else:
                            loop = False
                    loop = True
                    while loop:
                        product = input(colored("Service : " , "green"))
                        os.system('cls')
                        if product == "":
                            print(colored("[ Product can't be empty ]" , "red"))
                            time.sleep(1.1)
                            os.system("cls")
                        else:
                            loop = False

                            time.sleep(1.3)
                            os.system('cls')
                    

                    credentials = Credentials(passwordCredentials , usernameCredentials , emailCredentials , product)

                    crdManager.addCredentials(credentials , usrManager.getId(username , password))

                    counterAlert+=1


                elif selectionUser == "3":
                    
                    #__   ___                _   _ _    ___            _          _ _        _    
                    #\ \ / (_)_____ __ __   /_\ | | |  / __|_ _ ___ __| |___ _ _ (_) |_ __ _| |___
                    # \ V /| / -_) V  V /  / _ \| | | | (__| '_/ -_) _` / -_) ' \| |  _/ _` | (_-<
                    #  \_/ |_\___|\_/\_/  /_/ \_\_|_|  \___|_| \___\__,_\___|_||_|_|\__\__,_|_/__/
                                                                              
                    os.system('cls')

                    crdManager.noFilterSearch(usrManager.getId(username , password))
                    print()
                    print("Press enter to quit")
                    print()
                    selectionUser = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

                    counterAlert+=1
                    os.system('cls')

                elif selectionUser == "4":
                    #______ _ _ _              _____                     _     
                    #|  ___(_) | |            /  ___|                   | |    
                    #| |_   _| | |_ ___ _ __  \ `--.  ___  __ _ _ __ ___| |__  
                    #|  _| | | | __/ _ \ '__|  `--. \/ _ \/ _` | '__/ __| '_ \ 
                    #| |   | | | ||  __/ |    /\__/ /  __/ (_| | | | (__| | | |
                    #\_|   |_|_|\__\___|_|    \____/ \___|\__,_|_|  \___|_| |_|
                                                                                 
                    os.system('cls')
                    loopSearchMenu = True

                    while loopSearchMenu:
                     
                        menuManagement.exportSerchMenu()
                        menuFilterSeacrh = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                     
                        if menuFilterSeacrh == "1":
                            os.system('cls')

                            print(colored("Insert the [Credentials ID]","green"))
                            loopValue = True

                            while loopValue:
                                try:
                                    id_credential = int(input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green")))
                                    loopValue = False
                                    os.system('cls')
                                except ValueError:
                                    print(colored("Invalid value!","red")) 

                                    time.sleep(1.1)
                                    os.system('cls')

                            crdManager.idFilterSearch(usrManager.getId(username , password) , id_credential)

                            print()

                            print(colored("Press enter to quit","green"))
                            enter = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

                            os.system('cls')
                            counterAlert+=1

                        elif menuFilterSeacrh == "2":
                            os.system('cls')
                            print(colored("Insert the [username]","green"))
                            
                            usernameCredentials = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))  
                            crdManager.usernameFilterSearch(usrManager.getId(username,password) , usernameCredentials)

                            print()

                            print(colored("Press enter to quit","green"))
                            enter = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            os.system('cls')

                        elif menuFilterSeacrh == "3":
                            os.system('cls')
                            print(colored("Insert the [email]","green"))

                            email_Credentials = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            crdManager.emailFilterSearch(usrManager.getId(username , password) , email_Credentials)

                            print()

                            print(colored("Press enter to quit","green"))
                            enter = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            os.system('cls')

                        elif menuFilterSeacrh == "4":
                            os.system('cls')

                            productCredentials = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            crdManager.productFilterSeacrh(usrManager.getId(username , password) , productCredentials)

                            print()

                            print(colored("Press enter to quit","green"))
                            enter = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            os.system('cls')


                        elif menuFilterSeacrh == "5":
                            loopSearchMenu = False
                            os.system('cls')
                        
                        elif not(menuFilterSeacrh == "1" or menuFilterSeacrh == "2" or menuFilterSeacrh == "3" or menuFilterSeacrh == "4" or menuFilterSeacrh == "5"):
                            os.system('cls')

                            print(Style.BRIGHT+colored("Invalid Choice","red"))
                            time.sleep(1.1)
                            os.system('cls')



                elif selectionUser == "5":
                    loopManagerMenuCredentials = True

                    while loopManagerMenuCredentials:

                        menuManagement.exportManagerMenuCredentials()

                        managerMenu = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

                        if managerMenu == "1":
                            print()
                    
                        
                    loopUser = False

                elif selectionUser == "":
                    #QUIT SELECTION
                    loopUser = False


                elif not (selectionUser == "1" or selectionUser == "2" or selectionUser == "3" or selectionUser == "4" or selectionUser == "5" or selectionUser == "6"):

                    #ERROR SELECTION MANAGEMENT
                    
                    os.system('cls')

                    print(Style.BRIGHT+colored("Invalid Choice","red"))
                    time.sleep(1.3)
                    os.system('cls')

                    counterAlert+=1

        elif selection == "2":

            #______           _     _              _   _               
            #| ___ \         (_)   | |            | | | |              
            #| |_/ /___  __ _ _ ___| |_ ___ _ __  | | | |___  ___ _ __ 
            #|    // _ \/ _` | / __| __/ _ \ '__| | | | / __|/ _ \ '__|
            #| |\ \  __/ (_| | \__ \ ||  __/ |    | |_| \__ \  __/ |   
            #\_| \_\___|\__, |_|___/\__\___|_|     \___/|___/\___|_|   
            #            __/ |                                         
            #          |___/                                          
                                                                    
            os.system('cls')

            register.registrationUSER()
            enter = input(Style.BRIGHT+colored("Press enter to exit : ","green"))

        elif selection == "3":

            #QUIT SELECTION

            os.system('cls')
            loop = False

        elif not(selection == "1" or selection == "2" or selection == "3"):
            
            #ERROR SELECTION MANAGEMENT

            os.system('cls')

            print(Style.BRIGHT+colored("Invalid Choice","red"))
            time.sleep(1.1)
            os.system('cls')


    print("Goodbye")

if __name__ == "__main__":

    main()