""" Light program version of WindTurbines Inventory """
from datetime import datetime
import re
# import string
import colorama
from colorama import Fore, Back, Style

num_format = re.compile(r'^\-?[1-9][0-9]*$')

colorama.init(autoreset=True)


class Bcolors:
    """Class representing colors options"""
    GRE = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


the_date = datetime.now().date()
print(" ")
print(f'{Bcolors.GRE}✇  Second Hand Windturbines. Inventory Tool ✇ ')
print(the_date)
print('=======================================================')


class Windturbine:
    """Class representing Windturbine details as follows"""
    def __init__(self):
        self._uname = ''
        self._mfg = ''
        self._model = ''
        self._country = ''
        self._year = 0
        self._npow = 0

    def addTurbine(self):
        try:
            self._uname = self._is_valid_uname(input('Agent-Name:\n '))
            self._mfg = input('Enter Windturbine Manufacturer:\n ')
            self._model = input('Enter Windturbine Model:\n ')
            self._country = self._is_valid_country(input('Enter Country:\n '))
            self._year = self._is_valid_year(input('Enter WT year:\n '))
            self._npow = self._is_valid_npow(input('Power [kW]:\n '))
            return True
        except ValueError as err:
            print(f"{err}")
            return False

    def _is_valid_uname(self, _uname):
        print(Fore.GREEN + 'Validation')
#        print(_uname)
        if not _uname.isalpha():
            print(f'{Bcolors.RED}No completed')
#            print(type(_uname))
            raise ValueError(
                f"""
                {Fore.YELLOW}Please use only characters (a-z){Fore.RESET}
                You typed {Style.BRIGHT}{_uname}{Style.RESET_ALL}
                """
            )
        return _uname

    def _is_valid_country(self, _country):
        print(Fore.GREEN + 'Validation')
#        print(_country)
        if not _country.isalpha():
            print(f'{Bcolors.RED}No completed')
#            print(type(_country))
            raise ValueError(
                f"""
                {Fore.YELLOW}Please use only characters (a-z){Fore.RESET}
                You typed {Style.BRIGHT}{_country}{Style.RESET_ALL}
                """
            )
        return _country

    def _is_valid_year(self, _year):
        print(Fore.GREEN + 'Validation')
#        print(type(_year))
        if not _year.isnumeric():
            print(f'{Bcolors.RED}No completed')
#            print(type(_year))
            raise ValueError(
                f"""
                {Fore.YELLOW}Please use only numbers (0-9){Fore.RESET}
                You typed {Style.BRIGHT}{_year}{Style.RESET_ALL}
                """
            )
        return _year

    def _is_valid_npow(self, _npow):
        print(Fore.GREEN + 'Validation')
#       print(type(_npow))
        if not _npow.isnumeric():
            print(f'{Bcolors.RED}No completed')
#           print(type(_npow))
            raise ValueError(
                f"""
                {Fore.YELLOW}Please use only numbers (0-9){Fore.RESET}
                You typed {Style.BRIGHT}{_npow}{Style.RESET_ALL}
                """
            )
        return _npow

    def __str__(self):
        return '\t'.join(str(x) for x in [
            self._uname, self._mfg, self._model,
            self._country, self._year, self._npow
        ])


class Inventory:
    """Class representing Windturbine to be added"""
    def __init__(self):
        self.turbines = []

    def addTurbine(self):
        turbine = Windturbine()
        if turbine.addTurbine() is True:
            self.turbines.append(turbine)
            print()
            print('Fantastic!!! 😎, The Windturbine was added ✇')

    def viewInventory(self):
        print('====================================================')
        print('\t'.join(['', 'Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        print('====================================================')
        for idx, turbine in enumerate(self.turbines):
            print(idx + 1, end='\t')
            print(turbine)


inventory = Inventory()
while True:

    print("=======================================================")
    print(' ✔ Add Windturbine to Inventory                     [1]')
    print(' ✔ Delete Windturnine from Inventory                [2]')
    print(' ✔ List all Windturbines                            [3]')
    print(' ✔ Update Windturbine in Inventory                  [4]')
    print(' ✔ Export Current Inventory                         [5]')
    print(' ✔ Exit                                             [6]')
    print("=======================================================")
    userInput = input('Select 1-6:\n ')
    if userInput == "1":
        # Add a Windturbines
        inventory.addTurbine()
    elif userInput == '2':
        # Remove a Windturbine
        if len(inventory.turbines) < 1:
            print(Fore.RED + 'WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = int(input('Enter # of Windturbine to be deleted:\n '))
        if item - 1 > len(inventory.turbines):
            print(Fore.RED + 'Wrong number provided')
        else:
            inventory.turbines.remove(inventory.turbines[item - 1])
            print()
            print(Fore.RED + 'Windturbine deleted')
    elif userInput == '3':
        # list of the Windturbines recorded
        if len(inventory.turbines) < 1:
            print(Back.RED + 'WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        # Edit Windturbine recorded
        if len(inventory.turbines) < 1:
            print(Back.RED + 'WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = input(Fore.GREEN + 'Select # of Windturbine to be updated:\n ')
        if not str(item).isdigit():
            print(Fore.RED + 'Wrong input provided')
            continue
        if str(item) == 0:
            print('mal')
            continue
        item = int(item)
        if item - 1 > len(inventory.turbines):
            print(Fore.RED + 'Wrong number provided')
        else:
            windturbine = Windturbine()
            if windturbine.addTurbine() is True:
                inventory.turbines.remove(inventory.turbines[item - 1])
                inventory.turbines.insert(item - 1, windturbine)
                print()
                print(Back.CYAN + 'Fore.Great 😊, Windturbine was updated')
    elif userInput == '5':
        # Create a file txt to export it
        if len(inventory.turbines) < 1:
            print(Back.RED + 'WindTurbine(s) not found!!!')
            continue
        f = open('windturbine_inventory.txt', 'w', encoding='utf-8')
        f.write('\t'.join(['Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        f.write('\n')
        for turbile in inventory.turbines:
            f.write('%s\n' % turbile)
        f.close()
        print(Fore.CYAN + 'Cool!! 😎 info exported to the file')
    elif userInput == '6':
        # exit the loop
        print(Fore.BLUE + 'talk soon to you 😉')
        break
    else:
        # Wrong user input
        print(Fore.RED + 'Invalid Input. Please try again')
# This is a new line that ends the file
