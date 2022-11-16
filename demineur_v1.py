### Marwan Kaouachi's Python demineur project

### Dependencies:
import os
import math
import random

# My Own Console Color class (Use ANSI escape codes) to make my program look a bit more fancy
class cc:
    end = "\x1b[0m"

    # Mise en forme
    bold = "\x1b[1m"
    ita = "\x1b[3m"
    unav = "\x1b[2m"
    und = "\x1b[4m"
    blink = "\x1b[5m]"
    inv = "\x1b[7m"
    stri = "\x1b[9m"

    # Couleur Front
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    magenta = "\x1b[35m"
    cyan = "\x1b[36m"
    white = "\x1b[37m"

    # Couleur Back
    bgblack = "\x1b[40m"
    bgred = "\x1b[41m"
    bggreen = "\x1b[42m"
    bgyellow = "\x1b[43m"
    bgblue = "\x1b[44m"
    bgmagenta = "\x1b[45m"
    bgcyan = "\x1b[46m"
    bgwhite = "\x1b[47m"

    # Flags
    base = f"[ {green}#{end} ] > "
    ask = f"[ {blue}?{end} ] > "
    warn = f"{bgred}{white}[ ! ]{end} > "
    info = f"{bgcyan}{white}[ i ]{end} > "
    heart = f"{bgwhite}{red}[ ❤ ]{end} >"
    greenTag = f"[{green}+{end}]"
    redTag = f"[{red}+{end}]"
    err = f"{bgred}[/!\]{end} : "
    
    ### Example Usage for anyone who wants to understand it
    #
    # Use f"" inside a print() to allow variables in it, and call the class with cc.[option]
    # Since my class use ANSI Escpe code we need to stop modifications by adding the "end" flag
    # Example could be : $ print(f"test {cc.red}test, but in red{cc.end}")
    

### Functions:

# Take min max and let user input an integer
# only between these values
def int_input(val_min: int, val_max: int, display: str):
    user_input = -1
    isnum = True
    
    # Loop to restart if the input is not correct
    while user_input > val_max or user_input < val_min:
        
        # Try catch to avoid crash while converting input
        try:    
            user_input = int(input(display))
        except:
            isnum = False
            print(f"{cc.warn}Votre saisie n'est pas un nombre entier. Vous devez séléctionner une option par son chiffre.")  
        # All conditions needed for the input check, we return      
        if user_input <= val_max and user_input >= val_min and type(user_input) == int:
            return user_input
        # Input out of range, print error message and restart in the loop
        elif user_input > val_max or user_input < val_min and isnum == True:
            print(f"{cc.warn}Votre saisie ne correspond à aucune option. Vous devez saisir une valeur comprise entre {cc.red}[{val_min}, {val_max}]{cc.end}.")
def menu():
    ascii_art = """
  ____                 _                       
 |  _ \  ___ _ __ ___ (_)_ __   ___ _   _ _ __ 
 | | | |/ _ \ '_ ` _ \| | '_ \ / _ \ | | | '__|
 | |_| |  __/ | | | | | | | | |  __/ |_| | |   
 |____/ \___|_| |_| |_|_|_| |_|\___|\__,_|_|   
                                               
"""
print(int_input(0, 4, f"{cc.info}Test saisie nombre: {cc.green}[0, 4]{cc.end}"))