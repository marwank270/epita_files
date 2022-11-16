### Marwan Kaouachi's Python homework

### Dependencies
import math
import random


### Functions

# Load and return as a list the argument file, now in utf-8
def load_lexicon(path: str):
    lexicon = open(path, encoding="utf-8")
    lexi_list = lexicon.read()
    lexicon.close()
    lexi_list = lexi_list.split('\n')
    return lexi_list


# Check whether the input is in the lexicon
def check_word(word: str, lexicon):
    if len(word) == 0:
        print("Please enter a word")
        return False
    elif word in lexicon:
        return True
    else:
        return False

# Calculate "Jaro distance"
def jaro_distance(word_1: str, word_2:str):
    w1_len = len(word_1)
    w2_len = len(word_2)
    case = []
    nbr = 0
    distance = 0
    similar = 0
    
    # Take the shortest in first
    if w1_len > w2_len:
        tmp = word_1
        word_1 = word_2
        word_2 = tmp 
    
    # Calculate similar char between words
    for char_1 in word_1:
        for char_2 in word_2:
            if char_1 == char_2:
                case.append(char_1)
    case = list(set(case))
    similar = len(case)
    
    if similar == 0:
        similar += 1
        
    if w1_len == w2_len:
        for char in range(w1_len - 1):
            if word_1[char] != word_2[char] and word_1[char] == word_2[char+1] or word_1[char-1] == word_2[char]:
                nbr += 1
    else:
        nbr = 0
    nbr = nbr//2
    distance = (1/3)*(similar/w1_len + similar/w2_len + ((similar - nbr)/similar))
    return distance

# Find and return closest words in the lexicon
def closest_words(word: str, lexicon: list):
    closest = []
    temporary_word = ""
    temporary_jaro = 0
    for element in lexicon: 
        if jaro_distance(word, element) > temporary_jaro:
            temporary_word = element
            temporary_jaro = jaro_distance(word, element)
            closest.append(element)
        if len(closest) > 5:
            while len(closest) > 5:
                closest.remove(closest[0])
    return closest
   
        
    
### Actual Program

# False 'clear' command because i'm not authorized to import 'os'
clear = "\n" * 100
print(clear)

# My Own Console Color class (Use ANSI escape codes) to make my program look fancy
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
    
    ### Example Usage for anyone who wants to understand it
    #
    # Use f"" inside a print() to allow variables in it, and call the class with cc.[option]
    # Since my class use ANSI Escpe code we need to stop modifications by adding the "end" flag
    # Example could be : $ print(f"test {cc.red}test, but in red{cc.end}")

ascii_art = """
  _              _                 
 | |    _____  _(_) ___ ___  _ __  
 | |   / _ \ \/ / |/ __/ _ \| '_ \ 
 | |__|  __/>  <| | (_| (_) | | | |
 |_____\___/_/\_\_|\___\___/|_| |_|
                                   """
                               
# Load lexicon before starting the core code                                
lexicon = load_lexicon("./lexicon.txt")

def menu():
    print(f"{cc.yellow}{ascii_art}{cc.end}\n\n{cc.base} 1 : {cc.green}Démarrer le programme{cc.end}\n{cc.base} 0 : {cc.red}Quitter le programme{cc.end}\n\n")
    choix_menu = 0
    quit = False
    while choix_menu != 1 or choix_menu != 0 or quit == True:
        choix_menu = input(f"{cc.ask}{cc.und}Choisissez une option pour commencer :{cc.end}  ")
        if choix_menu.isdecimal() == False:
            print(f"{cc.warn}Vous devez choisir une option étant un {cc.red}chiffre{cc.end} entre {cc.red}[0;1]{cc.end}.")
        else:
            choix_menu = int(choix_menu)
            if choix_menu > 1 or choix_menu < 0 or quit == True:
                print(f"{cc.warn} Vous devez choisir une option entre [0;1].")
            else:   
                if choix_menu == 1:
                    program()
                else:
                    print(f"{cc.heart} Au revoir.")
                    quit == True
                    break
                
def program():
    print(clear)
    
    sentence = input(f"{cc.ask}{cc.und}Tapez une phrase à corriger :{cc.end} ")
    sentence = sentence.split()
    
    for word in sentence:
        closest = closest_words(word, lexicon)
        if word not in lexicon:
            correct = word
            while correct not in closest:
                correct = input(f"{cc.und}{cc.red}{word}{cc.end}{cc.und} n'est pas un mot français, vous vouliez dire ?{cc.end}\n{closest} \n{cc.ask}")
                if correct not in closest and check_word(correct, lexicon) == False:
                    print(f"{cc.warn}Ce mot ne fais pas parti de la liste des suggestion.")
                else: 
                    sentence = sentence.replace(word, correct)
                    print(f"{cc.base} {sentence}")
                    break
    
    input("Press \"Enter\" to go back")
    menu()

# First function to be runned  
menu()
#print(jaro_distance("veup", "veux"))
#print(jaro_distance("veup", "peu"))
