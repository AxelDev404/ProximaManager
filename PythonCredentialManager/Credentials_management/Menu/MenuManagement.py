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
        print(colored("|","red")+Style.BRIGHT+colored("      [4] Filter search          ","green")+colored("|","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [5] Manage credentials     ","green")+colored("|","red"))
        print(colored("|                                 |","red"))
        print(colored("|","red")+Style.BRIGHT+colored("      [6] Quit          ","green")+colored("         |","red"))
        print(colored("+","green")+colored("_________________________________","red")+colored("+","green"))
        print()


    def exportSerchMenu(self):
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))
        print(colored("|                                    |","red"))
        print(colored("|         ","red")+Style.BRIGHT+colored("< FILTER SEARCH >" , "red")+colored("          |","red"))
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [1] [ Search for id credential ]","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [2] [ Search for username ]     ","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [3] [ Search for email ]        ","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [4] [ Search for service ]      ","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [5] [ Quit ]                    ","green")+colored("  |","red"))
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))


    def exportManagerMenuCredentials(self):
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))
        print(colored("|                                    |","red"))
        print(colored("|         ","red")+Style.BRIGHT+colored("< MANAGE MENU >" , "red")+colored("          |","red"))
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [1] [ Delete credential ]       ","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [2] [ Modify credential ]       ","green")+colored("  |","red"))
        print(colored("|                                    |","red"))
        print(colored("| ","red")+Style.BRIGHT+colored(" [3] [ Quit ]                    ","green")+colored("  |","red"))
        print(colored("+","green")+colored("____________________________________","red")+colored("+","green"))
        