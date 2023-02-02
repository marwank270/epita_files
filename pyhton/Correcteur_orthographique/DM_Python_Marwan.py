### Marwan Kaouachi's Python homework

### Dependencies
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


### Functions

# Load and return as a list the argument file, now in utf-8
def load_lexicon(path: str):
    try:
        with open(path, encoding="utf-8") as lexi:
            lexi_list = lexi.read().splitlines()
        return lexi_list
    except:
        print(f"{cc.err}{cc.red}Could not load \"lexicon\" file.{cc.end}\n{cc.info}Please make sure the file is in the same folder as the program and correctly named {cc.red}\"lexicon\"{cc.end}.")
        return -1


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
    
    # If they're the same word we skip them
    if word_1 == word_2:
        return 1.0
    
    # Storing length of words
    w1_len = len(word_1)
    w2_len = len(word_2)
    
    # Maximum distance
    dist_max = math.floor(max(w1_len, w2_len) / 2) - 1
    
    # Other variables
    similar = 0
    transpositions = 0
    point = 0
    distance = 0
    
    # List for each words
    flagged_1 = [0] * w1_len
    flagged_2 = [0] * w2_len
    
    # Take the shortest in first
    """if w1_len > w2_len:
        tmp = word_1
        word_1 = word_2
        word_2 = tmp     """
    
    # Calculate similar char between words
    for char_i in range(w1_len):
        for char_j in range(max(0, char_i - dist_max), min(w2_len, char_i + dist_max + 1)):
            if word_1[char_i] == word_2[char_j] and flagged_2[char_j] == 0:
                flagged_1[char_i] = 1
                flagged_2[char_j] = 1
                similar += 1
                break
            
    # If no similar char at all we skip 
    if similar == 0:
        return 0.0
        
    # Calculate char transpositions between words
    for i in range(w1_len):
        if flagged_1[i]:
            while flagged_2[point] == 0:
                point += 1
            if word_1[i] != word_2[point]:
                transpositions += 1
            point += 1
    transpositions = transpositions//2
    distance = (similar/ w1_len + similar / w2_len + (similar - transpositions) / similar)/ 3.0
    
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

# Add words in lexicon file   
def add_lexicon():
    path = "./lexicon.txt"
    lexi = open(path, "a", encoding="utf-8")
    print(clear)
    word = input(f"{cc.ask}{cc.und}Saisissez un mot a entrer dans le lexique :{cc.end} ").lower()
    word.split(' ')
    lexi.write("\n" + word)
    lexi.close()
    print(f"\n{cc.greenTag} Le mot \"{word}\" a été ajouté au lexique.")
    input(f"{cc.info}Appuyez sur une touche pour continuer ...")

    edit_lexicon()

# Delete words in lexicon file
def del_lexicon():
    path = "./lexicon.txt"
    print(clear)
    
    notin = False
    word = input(f"{cc.ask}{cc.und}Saisissez un mot a supprimer dans le lexique :{cc.end} ").lower() 
    with open(path, "r", encoding="utf-8") as lexi:
        all_lines = lexi.readlines()
        for line in all_lines:
            if word in line:
                with open(path, "w", encoding="utf-8") as lexi:
                    for line in all_lines:
                        if line.strip("\n") != word:
                            lexi.write(line)
                        else:
                            print(f"\n{cc.redTag} Le mot \"{word}\" a été supprimé au lexique.")
                            break
                            
            else:
                notin = True
                
        if notin == True:
            print(f"\n{cc.greenTag} Le mot \"{word}\" n'était pas dans le lexique.")
                
                
    input(f"{cc.info}Appuyez sur une touche pour continuer ...")
    
    edit_lexicon()
 
    
### Running stuff

# False 'clear' command because i'm not authorized to import 'os'
clear = "\n" * 100
print(clear)


ascii_art = """
  _              _                 
 | |    _____  _(_) ___ ___  _ __  
 | |   / _ \ \/ / |/ __/ _ \| '_ \ 
 | |__|  __/>  <| | (_| (_) | | | |
 |_____\___/_/\_\_|\___\___/|_| |_|
                                   """
                               
# Load lexicon before starting the core code                                
lexicon = load_lexicon("./lexicon.txt")

# Program main menu
def menu():
    print(clear)
    print(f"{cc.yellow}{ascii_art}{cc.end}\n\n{cc.base}1 : {cc.green}Démarrer le programme{cc.end}\n{cc.base}2 : {cc.green}Modifier le lexique{cc.end}\n{cc.base}0 : {cc.red}Quitter le programme{cc.end}\n\n")
    choix_menu = 0
    quit = False
    while choix_menu != 1 or choix_menu != 2 or choix_menu != 0 or quit == True:
        choix_menu = input(f"{cc.ask}{cc.und}Choisissez une option pour commencer :{cc.end}  ")
        if choix_menu.isdecimal() == False:
            print(f"{cc.warn}Vous devez choisir une option étant un {cc.red}chiffre{cc.end} entre {cc.red}[0;2]{cc.end}.")
        else:
            choix_menu = int(choix_menu)
            if choix_menu > 2 or choix_menu < 0 or quit == True:
                print(f"{cc.warn} Vous devez choisir une option entre {cc.red}[0;2]{cc.end}.")
            else:   
                if choix_menu == 1:
                    program()
                elif choix_menu == 2:
                    edit_lexicon()
                else:
                    print(f"{cc.heart} Au revoir.")
                    quit == True
                    break

# Core of the excercise                
def program():
    print(clear)
    
    sentence = input(f"{cc.ask}{cc.und}Tapez une phrase à corriger :{cc.end} ").lower()
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
                    sentence = [elem.replace(word, correct) for elem in sentence]
        else:
            pass
        
    sentence = ' '.join(sentence)
    print(f"{cc.info}Votre phrase corrigée : {cc.und}{sentence}{cc.end}")
    restart = input(f"\n\n{cc.base}1 : {cc.green}Recommencer{cc.end}\n{cc.base}0 : {cc.red}Retourner au menu{cc.end}\n\n{cc.ask}{cc.und}Choisissez une option ci-dessus :{cc.end} ")
            
    if restart == 1 or restart == '1':
        program()
    elif restart == 0 or restart == '0':
        menu()
    else:
        print(f"{cc.warn}Votre saisie ne correspond a aucune options. Vous allez être rediriger vers le menu principal.")
        input(f"{cc.info}Appuyez sur une touche pour continuer ...")
        menu()

# Lexicon edition menu
def edit_lexicon():
    print(clear)
    print(f"{cc.base}1 : {cc.green}Ajouter un mot dans le lexique{cc.end}\n{cc.base}2 : {cc.red}Supprimer un mot dans le lexique{cc.end}\n{cc.base}0 : {cc.red}Retourner au menu{cc.end}")
    choix_edit = ""
    
    while choix_edit != 1 or choix_edit != 2 or choix_edit != 0 or quit == True:
        choix_edit = input(f"\n\n{cc.ask}{cc.und}Choisissez une option pour modifier le lexique :{cc.end} ")
        if choix_edit.isdecimal() == False:
            print(f"{cc.warn}Vous devez choisir une option étant un {cc.red}chiffre{cc.end} entre {cc.red}[0;2]{cc.end}.")
        else:
            choix_edit = int(choix_edit)
            if choix_edit > 2 or choix_edit < 0 or quit == True:
                print(f"{cc.warn} Vous devez choisir une option entre {cc.red}[0;2]{cc.end}.")
            else:   
                if choix_edit == 1:
                    add_lexicon()
                elif choix_edit == 2:
                    del_lexicon()
                else:
                    menu()
                    quit == True
                    break   
                

# First function to be runned  
# after checkin that lexicon is
# correctly loaded
if lexicon != -1:
    menu()
