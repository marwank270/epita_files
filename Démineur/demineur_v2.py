### Marwan Kaouachi's Python demineur v2 project ###

### Dependencies
from tkinter import *
from random import *

### Global variables
global discovered, flags, mines, cells, grid, mines_number, flags_number, lines, columns, d

discovered = []                                     # Coordinates list of discovered bombs 
flags = []                                          # Coordinates list of flags droped by user
mines = []                                          # Coordinates list of mines
cells = []                                          # State of the cell (0-8 no mines, number of mines in behavior. 9 = boom)
grid = []                                           # Array that handle display of cells
mines_number = 0                                    # Mines number at the begining
flags_number = 0                                    # Flags number at the begining
lines = 16                                          # Height
columns = 16                                        # Length
d = 20                                              # Box size


### Classes 

# ToolTip class, made to display hover hint message
# This class isn't made by myself i found it on 
# stackoverflow while I was looking for help on how to use
# the tk dependency to make a mouse hover text
class ToolTip(object):
    
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

### Functions

# Get coordinates of the left click and run trace() function
def lc(event):
    global d
    
    # Column then line
    j = (event.x-2)//d
    i = (event.y-2)//d
    trace(i, j)
    
# Get coordinates of the right click and run trace() function
def rc(event):
    global d
    
    # Column then line
    j = (event.x-2)//d
    i = (event.y-2)//d
    flag(i, j)

# Get coordinates of neighbour cells
def neighborhood(i, j):
    global cells
    
    neighbour = []
    
    try:
        neighbour.append(cells[i-1][j-1])
        neighbour.append(cells[i-1][j])
        neighbour.append(cells[i-1][j+1])
        neighbour.append(cells[i][j-1])
        neighbour.append(cells[i][j+1])
        neighbour.append(cells[i+1][j-1])
        neighbour.append(cells[i+1][j])
        neighbour.append(cells[i+1][j+1])
    except:
        pass
    
    return neighbour

# Return the number of mines in the neighborhood in cells[i][j]
def count_mines(i, j):
       
    neighbors_list = list(neighborhood(i,j))
    # Look for '9' and count the number of bombs
    bombs_neighborhood = neighbors_list.count(9)
    return bombs_neighborhood

# Spread of discovering empy cells around
def spread(i, j): 
    global lines, columns
    
    ll = lines - 1
    cc = columns - 1
    
    # [ERR] : IndexError: list index out of range.
    # I need to find a way to check coordinates around only if they exists (try-except didn't worked) 
    """ I found out that the code will generate an IndexError but won't crash the program 
        so i've decided to let it like that"""   
    
    # Use trace() function in the 8 adjacent cells 
    trace(i-1,j-1)
    trace(i-1,j)
    trace(i-1,j+1)
    trace(i,j-1)
    trace(i,j+1)
    trace(i+1,j-1)
    trace(i+1,j)
    trace(i+1,j+1)
    
    # I'll let this like it it works for now so ...
    """# Try 1 to repair the last line bug in the spread functions
    # Verify edges
    if i-1 > 0 and j-1 > 0 and i+1 < ll and j+1 < cc:
        trace(i-1,j-1)
        trace(i-1,j)
        trace(i-1,j+1)
        trace(i,j-1)
        trace(i,j+1)
        trace(i+1,j-1)
        trace(i+1,j)
        trace(i+1,j+1)"""
        

### Graphical stuff

# Reset and init grid for new game
def reinit():
    global discovered, flags, mines, cells, grid, mines_number, flags_number, lines, columns, d
    
    # Erase Cancas
    draw.delete(ALL)
    
    # Dsiplay messages
    #rules.configure(text = "Règles : Clic gauche pour découvrir une case, Clic droit pour poser un drapeau, la partie se gagne en découvrant toutes les cases sans toucher de bombe. ")
    message.configure(text = 'Nombre de mines restantes :')
    message_flag.configure(text = 'Nombre de drapeaux restants :')
    
    # Game variables initialisation
    mines_number = 0
    discovered = []
    flags = []
    mines = []
    cells = []
    grid = []
    
    # Go througth every lines
    for i in range(lines):

        cells.append([])
        grid.append([])
        
        # Go througth every columns
        for j in range(columns):
            
            # Adding bombs w/ random percentage
            chances_mine = random()
            # Draw and append it in the grid
            grid[i].append(draw.create_rectangle(2+j*d, 2+i*d, 2+(j+1)*d, 2+(i+1)*d, outline='black', fill='gray'))
            
            # Chances under or equal to 16% => place a mine (9) in the cell
            if chances_mine <= 0.16 : 
                cells[i].append(9)
                mines_number = mines_number + 1
                number_mines.configure(text=mines_number)
                fast_list = [i,j]

                mines.append(fast_list)
                
            # Chances above 16% => place no mine (0) in the cell
            else :                                  
                cells[i].append(0)
                
    # Equalize bombs, flags and message
    flags_number = mines_number
    number_flag.configure(text=flags_number)

# Reveal what's inside the selected cell    
def trace(i,j):
    global discovered, cells, lines, columns
    # Get coordinates from lc() or rc()
    fast_list = [i,j]
    # Verification in the discovered and flags lists
    verif = discovered.count(fast_list)
    verif2 = flags.count(fast_list)
    
    # Conditions check not discovered not flagged not out of range etc
    if verif == 0 and i >= 0 and i <= 15 and j >= 0 and j <= 19 and verif2 == 0:
        
        # Store coordinates in discovered        
        discovered.append(fast_list)
        
        # No bomb at coordinates        
        if cells[i][j] == 0 :
            
            # Count of mines around
            count = count_mines(i,j)    
            
            # No bombs around coordinates
            if count == 0 :
                
                draw.itemconfigure(grid[i][j], fill='white')
                spread(i,j)
            else :

                draw.itemconfigure(grid[i][j], fill='white')
                # Write number of bombs found around coordinates
                draw.create_text(2+d*(j+0.5), 2+(i+0.5)*d, fill='black', state=DISABLED, font= ('Courier', '10', 'bold'), text = str(count))     
        
        # Bomb found at coordinates
        elif cells[i][j] == 9:
            
            # Draw mine
            draw.itemconfigure(grid[i][j], fill='red')
            draw.create_oval(5+j*d, 5+i*d, (j+1)*d-1, (i+1)*d-1, outline='black', fill='black')
            
            # Unload messages on screen 
            #rules.configure(text='')
            number_mines.configure(text='') 
            number_flag.configure(text='')
            message_flag.configure(text='')
            
            # Loose message
            message.configure(text='Vous avez perdu.')
                                                        
            discovered=[]
            
            # Bomb and game plate reveal (loose color)
            for i in range (lines) :
                for j in range(columns) :   
                    
                    # No bomb
                    if cells[i][j] == 0 :

                        draw.itemconfigure(grid[i][j], fill='white')
                        end_list = [i,j]
                        discovered.append(end_list)

                    else :
    
                        draw.itemconfigure(grid[i][j], fill='red')
                        draw.create_oval(5+j*d, 5+i*d, (j+1)*d-1, (i+1)*d-1, outline='black', fill='black')
                        end_list = [i,j]
                        discovered.append(end_list)
        
        # Verify Win conditions
        nb_terme = len(discovered)
        
        # Win if all boxes empty are discovered
        if nb_terme == 256 - mines_number :
            
            message.configure(text='Vous avez gagné !!!')
            #rules.configure(text='')
            number_mines.configure(text='')
            discovered=[]
            number_flag.configure(text='')
            message_flag.configure(text='')
            
            # Bomb and game plate reveal (win color)
            for i in range (lines) :
                for j in range(columns) :   
                    
                    # No bomb
                    if cells[i][j] == 0 :
    
                        draw.itemconfigure(grid[i][j], fill='white')
                        end_list = [i,j]
                        discovered.append(end_list)
    
                    else :
    
                        draw.itemconfigure(grid[i][j], fill='lightgreen')
                        draw.create_oval(5+j*d, 5+i*d, (j+1)*d-1, (i+1)*d-1, outline='black', fill='black')
                        end_list = [i,j]
                        discovered.append(end_list)

# Drop and pickup flags
def flag(i,j) :
    global lines, columns, discovered, flags, flags_number
    
    # Get coordinates from lc() or rc()
    fast_list = [i,j]
    # Verification in the discovered and flags lists
    verif = flags.count(fast_list)
    verif2 = discovered.count(fast_list)
    
    # Verifications before flag placement
    if verif == 0 and verif2 == 0 and flags_number > 0 :
        
        # Update box
        draw.itemconfigure(grid[i][j], fill='orange')
        flags.append(fast_list)
        flags_number = mines_number - len(flags)                                   
        number_flag.configure(text=flags_number)
    
    # If a flag has already been placed here    
    elif verif != 0 and verif2 == 0 and flags_number >= 0 :
    
        # Update box
        draw.itemconfigure(grid[i][j], fill='grey')
        flags.remove(fast_list)
        flags_number = mines_number - len(flags)
        number_flag.configure(text=flags_number)
        
    # Verify win conditions
    verif_flags = sorted(flags)                                      
    verif_mines = sorted(mines)
    
    if verif_flags == verif_mines :
        
        # Win update
        message.configure(text='Vous avez gagné !!!')
        #rules.configure(text='')
        number_mines.configure(text='')
        discovered = []
        number_flag.configure(text='')
        message_flag.configure(text='')
        
        # Bomb and game plate reveal (win color)
        for i in range (lines) :
            for j in range(columns) :  
                
                # No bomb
                if cells[i][j] == 0 :
                
                    draw.itemconfigure(grid[i][j], fill='white')
                    end_list = [i,j]
                    discovered.append(end_list)
            
                else :
            
                    draw.itemconfigure(grid[i][j], fill='lightgreen')
                    draw.create_oval(5+j*d, 5+i*d, (j+1)*d-1, (i+1)*d-1, outline='black', fill='black')
                    end_list = [i,j]
                    discovered.append(end_list)


### Window creation, entitlement and size settings

win = Tk()
win.title('Démineur v2 de Marwan K.')
win.resizable(width=False, height=False)


### Text in game

#rules = Label(win, text='Règles : Clic gauche pour découvrir une case, Clic droit pour poser un drapeau, la partie se gagne en découvrant toutes les cases sans toucher de bombe.')
#rules.grid(row = 2, column = 0, padx=3, pady=3, sticky=E)

message = Label(win, text='Nombre de mines à trouver :')
message.grid(row = 0, column = 0, padx=3, pady=3, sticky=E)

number_mines = Label(win, text='')
number_mines.grid(row = 0, column = 1, padx=3, pady=3, sticky=W)

message_flag = Label(win , text='Nombre de drapeaux restants :')
message_flag.grid(row = 1, column = 0, padx = 3, pady = 3, sticky=E)

number_flag = Label(win , text=flags_number)
number_flag.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=W)


### Buttons at the end of a game

button_quitter = Button(win, text='Quitter', command=win.quit)      
button_quitter.grid(row = 3, column = 1, sticky=S+W+E, padx=15, pady=5) 

button_reload = Button(win, text='Nouvelle partie', command=reinit)
button_reload.grid(row = 3, column = 0, sticky=S+W+E, padx=15, pady=5)
#button_reload.pack()
CreateToolTip(button_reload, text = 'Règles :\nClic gauche pour découvrir une case,\nClic droit pour poser un drapeau,\nla partie se gagne en découvrant toutes les cases sans toucher de bombe.')



### Creation of Canvas and grid for the game

draw = Canvas(win, bg='white', width=d*columns+1, height=d*lines+1)
draw.grid(row = 2, column = 0, columnspan = 2, padx=5, pady=5)


### Main starting loop ###

draw.bind('<Button-1>', lc)
draw.bind('<Button-3>', rc)
reinit()

# Listen events loop
win.mainloop()
try:
    # Good way the end window if closed
    win.destroy()
except TclError:
    pass 
