### Marwan Kaouachi's Python demineur project

### Dependencies:
import os
import numpy as np
import random as rnd

### Classes:
class Game:
    def __init__(self, matrix, ghost_matrix):
        self.matrix = matrix
        self.gm = ghost_matrix
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
    heart = f"{bgwhite}{red}[ ❤ ]{end} > "
    greenTag = f"[{green}+{end}] > "
    redTag = f"[{red}+{end}] > "
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
            user_input = input(display)
            if user_input == 'quit':
                return -1
            user_input = int(user_input)
        except:
            isnum = False
            print(f"{cc.warn}Votre saisie n'est pas un nombre entier. Vous devez saisir un chiffre.")  
            
        # All conditions needed for the input check, we return      
        if user_input <= val_max and user_input >= val_min and type(user_input) == int:
            return user_input
        
        # Input out of range, print error message and restart in the loop
        elif user_input > val_max or user_input < val_min and isnum == True:
            print(f"{cc.warn}Votre saisie ne correspond à aucune option disponible. Vous devez saisir une valeur comprise entre {cc.red}[{val_min}, {val_max}]{cc.end}.")
            
# Return list only  if user input is a char
def char_input(i_min: int, i_max: int, display: str):
    user_input = - 1
    uii = - 1 # user input index
    ischar = True
    
    # Loop to restart if the input is not correct
    while uii > i_max or uii < i_min:
        
        # Try catch to avoid crash while converting input
        try:    
            user_input = str(input(display))
            uii = alpha.rfind(user_input.upper())
        except:
            ischar = False
            print(f"{cc.warn}Votre saisie n'est pas un caractère. Vous devez saisir un caractère ici.")  
            
        # All conditions needed for the input check, we return      
        if uii <= i_max and uii >= i_min and type(user_input) == str and len(user_input) == 1:
            return [user_input, uii]
        
        # Input out of range, print error message and restart in the loop
        elif uii > i_max or uii < i_min or len(user_input) != 1 and ischar == True:
            min_range = alpha[i_min]
            max_range = alpha[i_max]
            print(f"{cc.warn}Votre saisie ne correspond à aucune option disponible. Vous devez saisir un caractère compris entre {cc.red}[{min_range}, {max_range}]{cc.end}.")

# Return list where user intend to play            
def game_input():
    line = -1
    column = -1
    target_position = []
    
    line = int_input(1, 16, f"\n{cc.base}{cc.und}Selectionnez une ligne {cc.green}[1, 16]{cc.end}{cc.und} (ou tapez \'quit\' pour retourner au menu) :{cc.end} ") - 1
    # If command quit is used
    if line <= -1:
        print(f"\n{cc.base}0 : Annuler et continuer la partie\n{cc.base}1 : Quitter la partie et revenir au menu principal\n")
        quit = int_input(0, 1, f"{cc.ask}Voulez vous quitter la partie ?")
        if quit == 1:
            menu()
        else:
            line = int_input(1, 16, f"\n{cc.base}{cc.und}Selectionnez une ligne {cc.green}[1, 16]{cc.end}{cc.und} :{cc.end} ") - 1
            target_position.append(line)
    else:
        target_position.append(line)
    
    column = char_input(0, 15, f"\n{cc.base}{cc.und}Selectionnez une colone {cc.green}[A, P]{cc.end}{cc.und} :{cc.end} ")
    target_position.append(column[1])
    
    return target_position      

# Display matrix in terminal (Debug version)
def disp_matrix(matrix):
    # Print matrix and references
    for i in range(len(matrix) + 1):
        ii = i + 1
        print(f"\n")
        
        # Print letters down the matrix aligned with it
        if ii == len(matrix) + 1:
            print("     ", end = "")
            for l in range(16):
                print(f"{cc.red}{alpha[l]}{cc.end}", end = "   ")
        else:
            # Print the inside of the matrix        
            for j in range(len(matrix[0])):
                if j == 0:
                    print(f"{cc.red}{ii:02}{cc.end} |", end = "")
                print(f" %s" % matrix[i,j], end= " |")    # f"{matrix[i,j]}"" don't work ?
                # Cheat mode
                # print(f" %s" % g.gm[i, j], end= " |")

# Display the matrix for the player
def display(matrix):
    # Print matrix and references
    for i in range(len(matrix) + 1):
        ii = i + 1
        print(f"\n")
        
        # Print letters down the matrix aligned with it
        if ii == len(matrix) + 1:
            print("     ", end = "")
            for l in range(16):
                print(f"{cc.red}{alpha[l]}{cc.end}", end = "   ")
        else:
            # Print the inside of the matrix        
            for j in range(len(matrix[0])):
                if j == 0:
                    print(f"{cc.red}{ii:02}{cc.end} |", end = "")
                print(f" %s" % matrix[i, j], end= " |")
                # Cheat mode
                # print(f" %s" % g.gm[i, j], end= " |")
                


# Check the bomb count around            
def check_around(line: int, column: int, matrix):
    bomb_count = 0
    
    # Obviously check first if the coordinates have any bomb
    if matrix[line, column] == 1:
        # -1 means game over
        return -1
    # Search for bomb around the coordinates
    else:
        line_cp = line - 1
        column_cp = column - 1
        
        # Research loop
        for i in range(3):
            column_cp = column - 1
            for j in range(3):
                try:
                    # Find bomb around
                    if matrix[line_cp, column_cp] == 1:
                        bomb_count += 1
                    column_cp += 1
                # If coordinates are near edges
                except:
                    pass
        line_cp += 1
        
    return bomb_count
            

def menu():
    # Clear the terminal from previous stuff
    os.system('cls||clear')
    ascii_art = f"""{cc.blue}
  ____                 _                       
 |  _ \  ___ _ __ ___ (_)_ __   ___ _   _ _ __ 
 | | | |/ _ \ '_ ` _ \| | '_ \ / _ \ | | | '__|
 | |_| |  __/ | | | | | | | | |  __/ |_| | |   
 |____/ \___|_| |_| |_|_|_| |_|\___|\__,_|_|   {cc.end}
                                               
""" 
    print(ascii_art)
    print(f"{cc.info}{cc.und}Rappel des règles du jeu :{cc.end}\n\t- Le but du jeu est de découvrir toutes les cases sans toucher la moindre bombe !\n\t- Après chaque coup vous aurez le nombre de bombe dispatché dans les 8 cases tout autour de votre dernière sélection.\n\t- Pour déplacer le repère vous utiliserez les flèches directionnelles.\n")
    print(f"{cc.greenTag}1 : Commencer une partie.\n{cc.redTag}0 : Quitter le jeu.\n\n")
    choice = int_input(0, 1, f"{cc.ask}{cc.und}Choisissez une option :{cc.end} ")
    
    if choice == 1:
        play()
    elif choice == 0:
        print(f"{cc.heart}Au revoir.")
        exit()
def play():   
    score = 0
    # Matrix initialisation & bomb randomization
    matrix = np.full((16,16), " ")
    ghost_matrix = np.zeros((16,16), dtype=np.int32)
    g = Game(matrix, ghost_matrix)
    
    # Bomb placement loop
    for i in range(40):
        
        # Random coordinates
        rand_i = rnd.randint(0, 15)
        rand_j = rnd.randint(0, 15)
        
        # Ghost Matrix edition    
        g.gm[rand_i, rand_j] = 1    # I decided to use 0 & 1 instead of boolean
                                        # value because it's smaller to display
                                    
    loose = False
    while loose == False:
        # Clear the terminal from previous stuff
        os.system('cls||clear')
        
        # Display the matrix
        display(g.matrix)
        
        print(f"\n\n{cc.greenTag}Score: {cc.green}{score}{cc.end}")
        target = game_input()
        
        bomb_count = check_around(target[0], target[1], g.gm)
        
        if bomb_count == -1:
            loose = True
            break
        else:
            g.matrix[target[0], target[1]] = bomb_count
            score += 1
        """if g.matrix[target[0], target[1]] == 1:
            loose = True
            break
        else:
            pass"""
    
    os.system('cls||clear')
    disp_matrix(g.gm) 
    print(f"\n{cc.redTag}{cc.red}Vous avez touché une bombe en {cc.end}[{target[0]}, {target[1]}]{cc.red} vous avez perdu !{cc.end}\n{cc.greenTag}Score : {cc.green}{score}{cc.end}\n\n{cc.greenTag} 1 : Commencez une nouvelle partie.\n{cc.redTag} 0 : Retourner au menu principal\n\n")
    restart = int_input(0, 1, f"{cc.ask}{cc.und}Choisissez une option ci-dessus pour continuer :{cc.end} ")
    if restart == 1:
        play()
    else:
        menu()
    
    
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#print(alpha.rfind('p'.upper()))
#print(alpha[])
menu()