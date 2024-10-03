from termcolor import colored
from colorama import Style ,Fore

class MenuManagement:

    def exportMenuPrincipal(self):

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


    def exportUserMenu(self):
        print(colored("+","green")+colored("__________________________________","red")+colored("+","green"))
        print(colored("|                                 |","red"))
        print(colored("|     ","red")+Style.BRIGHT+colored(" <     MAIN MENU     >" , "red")+colored("      |","red"))
        print(colored("|_________________________________|","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [1] Profile           ","green",)+colored("     |","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [2] Add Credentials      ","green")+colored("  |","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [3] View All Credentials   ","green")+colored("|","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [4] Quit          ","green")+colored("         |","red"))
        print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
        print()
        