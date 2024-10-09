
from termcolor import colored
from colorama import Style ,Fore
import pyfiglet
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

    #PROXIMA SECURITY MANAGER TITOLO PROGETTO
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
                
                usrManager.getId(username , password)

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

                    loopUserManager = True

                    while loopUserManager:
                        print()
                        menuManagement.exportManagerMenuUser()
                        userManagerMenu = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

                        if userManagerMenu == "1":
                            os.system('cls')
                            crdManager.deleteAllWithUser(usrManager.getId(username , password))
                            usrManager.deleteUser(usrManager.getId(username,password))
                            time.sleep(4.1)

                        elif userManagerMenu == "2":
                            os.system('cls')

                            loopNewPassword = True
                            while loopNewPassword:

                                print(colored("Insert the new password : ","green"))
                                print()

                                logInNewPasword = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system('cls')
                                if len(logInNewPasword) < 8 or len(logInNewPasword) > 50:
                                    print(colored("[ Password can't be empty and it must be more or equal to 8 characters ]","red"))
                                    time.sleep(4.3)
                                    os.system("cls")
                                else:
                                    os.system('cls')
                                    usrManager.updatePassword(usrManager.getId(username , password) , logInNewPasword)
                                    time.sleep(4.1)
                                    os.system('cls')
                                    loopNewPassword = False

                        elif userManagerMenu == "3":
                            os.system('cls')

                            loopNewEmail = True
                            while loopNewEmail:

                                print(colored("Insert the new email : ","green"))
                                print()

                                logInNewEmail = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system('cls')
                                if logInNewEmail == "" or len(logInNewEmail) > 200:
                                    print(colored("[ Email can,t be empty ]", "red"))
                                    time.sleep(4.3)
                                    os.system("cls")
                                else:
                                    os.system('cls')
                                    usrManager.updateEmail(usrManager.getId(username , password) , logInNewEmail)
                                    time.sleep(4.1)
                                    os.system('cls')
                                    loopNewEmail = False

                        elif userManagerMenu == "4": 
                            os.system('cls')
                            
                            loopNewUsername = True
                            while loopNewUsername:

                                print(colored("Insert the new username : ","green"))
                                print()

                                logInNewUsername = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system("cls")
                                if logInNewUsername == "" or len(logInNewUsername) > 50:
                                    print(colored("[ Username can,t be empty ]", "red"))
                                    time.sleep(4.3)
                                    os.system("cls")
                                else:     
                                    os.system('cls')
                                    usrManager.updateUsername(usrManager.getId(username , password) , logInNewUsername)
                                    time.sleep(4.1)
                                    os.system('cls')
                                    loopNewUsername = False
                        
                        elif userManagerMenu == "5":
                            os.system('cls')
                            usrManager.profile(username,password)
                            print(colored("Press eneter to quit" , "green"))
                            print()
                            enter = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                            os.system('cls')

                        elif userManagerMenu == "6":
                            loopUserManager = False
                            counterAlert+=1
                            os.system('cls')
                        
                        elif not(userManagerMenu == "1" or userManagerMenu == "2" or userManagerMenu == "3" or userManagerMenu == "4" or userManagerMenu == "5" or userManagerMenu == "6"):
                            os.system('cls')
                            print(Style.BRIGHT+colored("Invalid Choice","red"))
                            time.sleep(1.1)
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
                            time.sleep(5.3)
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
                    print(colored("Press enter to quit" , "green"))
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

                                    time.sleep(2.1)
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
                    # _____              _            _   _       _      ___  ___                                  
                    #/  __ \            | |          | | (_)     | |     |  \/  |                                  
                    #| /  \/_ __ ___  __| | ___ _ __ | |_ _  __ _| |___  | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
                    #| |   | '__/ _ \/ _` |/ _ \ '_ \| __| |/ _` | / __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
                    #| \__/\ | |  __/ (_| |  __/ | | | |_| | (_| | \__ \ | |  | | (_| | | | | (_| | (_| |  __/ |   
                    # \____/_|  \___|\__,_|\___|_| |_|\__|_|\__,_|_|___/ \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                    #                                                                               __/ |          
                    #                                                                              |___/                                                                         

                    os.system('cls')
                    loopManagerMenuCredentials = True

                    while loopManagerMenuCredentials:
                        os.system('cls')    

                        menuManagement.exportManagerMenuCredentials()

                        managerMenu = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))

                        if managerMenu == "1":
                            os.system('cls')

                            loopIntCheck = True
                            while loopIntCheck:
                                try:
                                    print(colored("Insert the credential id : ","green"))
                                    print()
                                    idToDelete = int(input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green")))
                                    loopIntCheck = False
                                    os.system('cls')
                                except ValueError:
                                    print(colored("Invalid value!","red")) 
                                    time.sleep(1.1)
                                    os.system('cls')

                            crdManager.deleteRow(usrManager.getId(username,password) , idToDelete)

                        elif managerMenu == "2":
                            os.system('cls')

                            loopIntCheck = True
                            while loopIntCheck:
                                try:
                                    print(colored("Insert the credential id : ","green"))
                                    print()
                                    idToUpdate = int(input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green")))
                                    loopIntCheck = False
                                    os.system('cls')
                                except ValueError:
                                    print(colored("Invalid value!","red")) 
                                    time.sleep(1.1)
                                    os.system('cls')


                            loopPasswordToUpdate = True

                            while loopPasswordToUpdate:
                                print()
                                print(colored("Insert the new password : ","green"))
                                print()

                                updatePassword = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system("cls")

                                if updatePassword == "" or len(updatePassword) > 50:
                                    print(colored("[ Password can't be empty ]" , "red"))
                                    time.sleep(4.3)
                                    os.system('cls')
                                else: 
                                    os.system('cls')
                                    crdManager.updatePassword(usrManager.getId(username,password) , idToUpdate , updatePassword)
                                    time.sleep(4.2)
                                    loopPasswordToUpdate = False
                        
                        elif managerMenu == "3":
                            os.system('cls')

                            loopIntCheck = True
                            while loopIntCheck:
                                try:
                                    print(colored("Insert the credential id : ","green"))
                                    print()
                                    idToUpdate = int(input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green")))
                                    loopIntCheck = False
                                    os.system('cls')
                                except ValueError:
                                    print(colored("Invalid value!","red")) 
                                    time.sleep(1.1)
                                    os.system('cls')

                            loopEmailToUpdate = True

                            while loopEmailToUpdate:
                                print()
                                print(colored("Insert the new email : ","green"))
                                print()

                                updateEmail = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system('cls')

                                if updateEmail == "" or len(updateEmail) > 200:
                                    print(colored("[ Eamil can't be empty ]" , "red"))
                                    time.sleep(4.3)
                                    os.system('cls')
                                else:
                                    os.system('cls')
                                    crdManager.updateEmail(usrManager.getId(username,password) , idToUpdate , updateEmail)
                                    time.sleep(4.2)
                                    loopEmailToUpdate = False

                        elif managerMenu == "4":
                            os.system('cls')


                            loopIntCheck = True
                            while loopIntCheck:
                                try:
                                    print(colored("Insert the credential id : ","green"))
                                    print()
                                    idToUpdate = int(input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green")))
                                    loopIntCheck = False
                                    os.system('cls')
                                except ValueError:
                                    print(colored("Invalid value!","red")) 
                                    time.sleep(1.1)
                                    os.system('cls')


                            loopUsernameToUpdate = True
                            while loopUsernameToUpdate:
                                print()
                                print(colored("Insert the new username : ","green"))
                                print()

                                updateUsername = input(Style.BRIGHT+colored(usrManager.getUsername(username , password),"green")+Style.BRIGHT+colored("@","red")+Style.BRIGHT+colored(">_ ","green"))
                                os.system('cls')
                                if updateUsername == "" or len(updateUsername) > 50:
                                    print(colored("[ Username can't be empty ]" , "red"))
                                    time.sleep(4.3)
                                    os.system('cls')
                                else:
                                    os.system('cls')
                                    crdManager.updateUsername(usrManager.getId(username,password) , idToUpdate , updateUsername)
                                    time.sleep(4.2)
                                    loopUsernameToUpdate = False

                        elif managerMenu == "5":
                            loopManagerMenuCredentials = False
                            counterAlert=+1
                            os.system('cls')

                        elif not(managerMenu == "1" or managerMenu == "2" or managerMenu == "3" or managerMenu == "4" or managerMenu == "5"):
                            os.system('cls')

                            print(Style.BRIGHT+colored("Invalid Choice","red"))
                            time.sleep(1.1)
                            os.system('cls')


                elif selectionUser == "6":
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
