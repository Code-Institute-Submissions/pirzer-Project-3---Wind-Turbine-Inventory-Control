""" Light program version of WindTurbines Inventory """
import string
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class Bcolors:
    """Class representing colors options"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'


the_date = datetime.now().date()
print(" ")
print(f'{Bcolors.YELLOW}✇  Second Hand Windturbines. Inventory Tool ✇ ')
print(the_date)
print("=======================================================")


class Windturbine:
    """Class representing Windturbine details as follows"""
    def __init__(self):
        self._uname = ''
        self._mfg = ''
        self._model = ''
        self._country = ''
        self._year = 0
        self._npower = 0

    def addTurbine(self):
        try:
            self._uname = self._is_valid_uname(input('Agent-Name:\n '))
            self._mfg = input('Enter Windturbine Manufacturer:\n ')
            self._model = input('Enter Windturbine Model:\n ')
            self._country = input('Enter Country Location:\n ')
            self._year = int(input('Enter Windturbine year:\n '))
            self._npower = int(input('Enter Nominal Power [kW]:\n '))
            return True
        except ValueError as err:
            print(f"{err}")
            return False

    def _is_valid_uname(self, _uname):
        if not _uname.isalpha():
            raise ValueError(
                f"""
                Please use only characters (a-z)
                You typed {Style.BRIGHT}{_uname}{Style.RESET_ALL}
                """
            )
        return self._uname

    def __str__(self):
        return '\t'.join(str(x) for x in [
            self._uname, self._mfg, self._model,
            self._country, self._year, self._npower
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
        print("=====================================================")
        print('\t'.join(['', 'Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        print("=====================================================")
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
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = int(input('Enter # of Windturbine to be deleted:\n '))
        if item - 1 > len(inventory.turbines):
            print('Wrong number provided')
        else:
            inventory.turbines.remove(inventory.turbines[item - 1])
            print()
            print('Windturbine deleted')
    elif userInput == '3':
        # list of the Windturbines recorded
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        # Edit Windturbine recorded
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = int(input('Select # of Windturbine to be updated:\n '))
        if item - 1 > len(inventory.turbines):
            print('Wrong number provided')
        else:
            windturbine = Windturbine()
            if windturbine.addTurbine() is True:
                inventory.turbines.remove(inventory.turbines[item - 1])
                inventory.turbines.insert(item - 1, windturbine)
                print()
                print('Great 😊, Windturbine was updated')
    elif userInput == '5':
        # Create a file txt to export it
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        f = open('windturbine_inventory.txt', 'w', encoding='utf-8')
        f.write('\t'.join(['Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        f.write('\n')
        for turbile in inventory.turbines:
            f.write('%s\n' % turbile)
        f.close()
        print('Cool!! 😎 info exported to the file')
    elif userInput == '6':
        # exit the loop
        print('talk soon to you 😉')
        break
    else:
        # Wrong user input
        print('Invalid Input. Please try again')


def validate_user(letter):
    """
    Validate agents name field. Letters (a-z)
    """
    try:
        # if letter not in alphabet:
        if letter.isalpha():
            return True
            
    except ValueError as err:
        # raise ValueError(
        #         f"Single letters (a-z) "
        #         f"You typed {Style.BRIGHT}{letter}{Style.RESET_ALL}"
        #     )
        print(f"{Fore.RED}Wrong data:{Fore.RESET} {err}.\n")
        return False
    


def get_user_letter():
    """
    Asking user for agent-name input
    """
    while True:
        user_letter = input('Agent-Name:\n ')

        if validate_user(user_letter):
            break
    return user_letter
# This is a new line that ends the file
