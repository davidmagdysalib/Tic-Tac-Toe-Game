"""
Main File Of Tic Tac Toe Game.
It Imports all Data From Other Files :
1- Classes (display.py), (write.py), (xo.py).
2- Menus (menu.py)
3- time, random For Ai Uses.

It Contains Many Functions That Work Together To Make This Great Game !
"""

#IMPORTS.
from turtle import Screen
from display import Border
from xo import O, X
from write import Writer
from data import data
from menu import main_menu, main_menu_buttons, play_menu, play_menu_buttons, level_menu, level_menu_buttons, credits_menu, credits_menu_buttons, menu, remove
import time, random

#MAIN WINDOW.
window = Screen()
window.tracer(0)
window.setup(600, 600)
window.bgcolor('black')
window.title('Tic Tac Toe')
window.update()

#POSITIONS OF DRAW AND CHECK CLICK OF EACH CELL.
positions = data.POSITIONS

#WINS.
wins = data.WINS

#POSITIONS OF O AND X.
o_pos = []
x_pos = []

#EMPTY CELLS.
empty_cells = [1,2,3,4,5,6,7,8,9]

#GAME STATE.
game_state = "main_menu"

#OBJECTS
O = O()
X = X()
border = Border()
writer = Writer()

#CLICK FUNCTION THAT CHECKS X AND Y OF A CLICK.
x = 600
y = 600
def click(x_pos,y_pos):
    """
    It Returns X Position and Y Position of Click.

    Args:
        x_pos (_type_): _description_
        y_pos (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    global x,y
    x = x_pos
    y = y_pos
    return (x,y)

def check_click(list_buttons):
    """
    Checking The Click Of Mouse To Display New Menu.

    Args:
        list_buttons (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state, drawn
    
    window.onscreenclick(click)
    window.update()
    for button in list_buttons:
        if (x >= button.min_x and x <= button.max_x) and (y >= button.min_y and y <= button.max_y):
            
            #MAIN MENU BUTTONS.
            if button.prompt == "Play": game_state = "play_menu"; drawn = False
            if button.prompt == "Exit": game_state = "exit"
            if button.prompt == "Credits": game_state = "credits"; drawn = False
            
            #PLAY MENU BUTTONS.
            if button.prompt == "SinglePlayer": game_state = "level_menu"; drawn = False
            if button.prompt == "MultiPlayer" : game_state = "multiplayer"
            if button.prompt == "Back" : game_state = "main_menu"; drawn = False
            
            #LEVEL MENU BUTTONS.
            if button.prompt == "Easy" : game_state = "easy_mode"
            if button.prompt == "Medium" : game_state = "medium_mode"
            if button.prompt == "Hard" : game_state = "hard_mode"
            if button.prompt == "Impossible" : game_state = "impossible_mode"

#USER TURN FUNCTION.
def user_turn(name="User", shape=O, list=o_pos):
    """
    The Function That Handles The User Turn And Returns True Or False To Know Either To Start Computer Turn Or No.

    Args:
        name (str, optional): _description_. Defaults to "User".
        shape (_type_, optional): _description_. Defaults to O.
        list (_type_, optional): _description_. Defaults to o_pos.

    Returns:
        _type_: _description_
    """
    
    #DISPLAYING TEXT USING WRITER.
    writer.display(f"{name} Turn : ")
    window.onscreenclick(click)
    window.update()
    
    #CHECKING POSITION OF MOUSE CLICK USING A MAIN LOGIC FROM POSITIONS DICTIONARY FROM DATA HANDLERS.
    for position in positions:
        key = positions[position]
        if (x >= key["x_range"][0] and x <= key["x_range"][1]) and (y >= key["y_range"][0] and y <= key["y_range"][1]):
            if (position not in x_pos) and (position in empty_cells):
                shape.draw(key["draw"])
                list.append(position)
                empty_cells.remove(position)
                window.update()
                return True 
    return False
            
#COMPUTER TURN FUNCTION.
def computer_turn(level):
    """
    The Function That Handles The Computer Turn And Returns True Or False To Know Either To Start User Turn Or No.

    Args:
        level (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    #DISPLAYING TEXT.
    writer.display("Computer Turn : ")
    window.update()
    time.sleep(1.5)
                
    for win in wins:
        a, b, c = win[0], win[1], win[2]
        
        #CHECK IF X CAN WIN.
        if ((a in x_pos) and (b in x_pos) and (c in empty_cells) and (random.randint(1,level) == 1)) :
            X.draw(positions[c]["draw"])
            x_pos.append(c)
            empty_cells.remove(c)
            window.update()
            return True
        
        elif ((a in x_pos) and (b in empty_cells) and (c in x_pos) and (random.randint(1,level) == 1)) :
            X.draw(positions[b]["draw"])
            x_pos.append(b)
            empty_cells.remove(b)
            window.update()
            return True
        
        elif ((a in empty_cells) and (b in x_pos) and (c in x_pos) and (random.randint(1,level) == 1)) :
            X.draw(positions[a]["draw"])
            x_pos.append(a)
            empty_cells.remove(a)
            window.update()
            return True
        
        #CHECK IF X CAN BLOCK.
        elif ((a in o_pos) and (b in o_pos) and (c in empty_cells) and (random.randint(1,level) == 1)) :
            X.draw(positions[c]["draw"])
            x_pos.append(c)
            empty_cells.remove(c)
            window.update()
            return True
        
        elif ((a in o_pos) and (b in empty_cells) and (c in o_pos) and (random.randint(1,level) == 1)) :
            X.draw(positions[b]["draw"])
            x_pos.append(b)
            empty_cells.remove(b)
            window.update()
            return True
        
        elif ((a in empty_cells) and (b in o_pos) and (c in o_pos) and (random.randint(1,level) == 1)) :
            X.draw(positions[a]["draw"])
            x_pos.append(a)
            empty_cells.remove(a)
            window.update()
            return True
            
    corner = random.choice([1,3,7,9])
    #CHECK IF CENTER IS EMPTY.
    if (5 in empty_cells) and (random.randint(1,level) == 1):
        X.draw(positions[5]["draw"])
        x_pos.append(5)
        empty_cells.remove(5)
        window.update()
        return True
    
    #CHECK IF CORNER IS EMPTY.
    elif (corner in empty_cells) and (random.randint(1,level) == 1):
        X.draw(positions[corner]["draw"])
        x_pos.append(corner)
        empty_cells.remove(corner)
        window.update()
        return True
        
    #DO A RANDOM MOVE.
    else:
        if empty_cells:
            block = random.choice(empty_cells)
            
            X.draw(positions[block]["draw"])
            x_pos.append(block)
            empty_cells.remove(block)
            window.update()
            return True
    
#CHECK WINNING FUNCTION.    
def check_winning(who):
    """
    Checking Who Won.

    Args:
        who (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    #CHECKING......
    for win in wins:
        if (win[0] in who) and (win[1] in who) and (win[2] in who):
            return True
        

#SINGLEPLAYER FUNCTION.
def singleplayer(level):
    """
    The Function That Creates Singleplayer Game.

    Args:
        level (_type_): _description_
    """
    
    global game_state, drawn, o_pos, x_pos, empty_cells
    
    #REMOVE ALL MENUS.
    remove(main_menu_buttons)
    remove(play_menu_buttons)
    remove(level_menu_buttons)
    remove(credits_menu_buttons)
     
    user = True   
    computer = False             
    game = True
    border.create()
    #MAIN LOOP.
    while game:
        window.update()
        
        #USER TURN.
        if user:
            #IF ITS A DRAW.
            if empty_cells == []:
                writer.draw()
                window.update()
                game = False
                
            if user_turn(name="User", shape=O, list=o_pos):
                user = False
                computer = True
                
        #IF WON.
        if check_winning(o_pos):
            writer.won()
            window.update()
            user = False
            computer = False
            game = False
                
        #IF LOST.
        elif check_winning(x_pos):
            writer.lost()
            window.update()
            user = False
            computer = False
            game = False
        
        #IF ITS A DRAW.
        elif empty_cells == []:
            writer.draw()
            window.update()
            game = False
            
        #COMPUTER TURN.
        if computer:
            #IF ITS A DRAW.
            if empty_cells == []:
                writer.draw()
                window.update()
                game = False
                
            elif computer_turn(level):
                user = True
                computer = False
         
    #RESETING EVERYTHING.       
    time.sleep(2)
    border.hide()
    O.delete()
    X.delete()
    writer.again()
    game_state = "main_menu"
    drawn = False
    o_pos = []
    x_pos = []
    empty_cells = [1,2,3,4,5,6,7,8,9]
      
#MULTIPLAYER FUNCTION.
def multiplayer():
    """
    Function That Creates Multiplayer Game
    """
    
    global game_state, drawn, x_pos, o_pos, empty_cells
    
    #REMOVE ALL MENUS.
    remove(main_menu_buttons)
    remove(play_menu_buttons)
    remove(level_menu_buttons)
    remove(credits_menu_buttons)
    
    game = True
    user1 = True
    user2 = False
    border.create()
    #MAIN LOOP.
    while game:
        window.update()
        
        #USER TURN.
        if user1:
            #IF ITS A DRAW.
            if empty_cells == []:
                writer.draw()
                window.update()
                game = False
                
            if user_turn(name="User1", shape=O, list=o_pos):
                user1 = False
                user2 = True
                
        #IF WON.
        if check_winning(o_pos):
            window.bgcolor("darkgreen")
            writer.display("User1 Won")
            window.update()
            user1 = False
            user2 = False
            game = False
                
        #IF LOST.
        elif check_winning(x_pos):
            window.bgcolor("darkgreen")
            writer.display("User2 Won")
            window.update()
            user1 = False
            user2 = False
            game = False
        
        #IF ITS A DRAW.
        elif empty_cells == []:
            writer.draw()
            window.update()
            game = False
            
        #COMPUTER TURN.
        if user2:
            #IF ITS A DRAW.
            if empty_cells == []:
                writer.draw()
                window.update()
                game = False
                
            elif user_turn(name="User2", shape=X, list=x_pos):
                user1 = True
                user2 = False
        
    #RESITING EVERYTHING.
    time.sleep(2)
    border.hide()
    O.delete()
    X.delete()
    writer.again()
    game_state = "main_menu"
    drawn = False
    o_pos = []
    x_pos = []
    empty_cells = [1,2,3,4,5,6,7,8,9]
          
          
#MAIN LOOP.
game = True
drawn = False
game_state = "main_menu"
while game:
    time.sleep(0.01)
    window.update()
    
    #MAIN MENU.
    if game_state == "main_menu":
        if not drawn:
            remove(main_menu_buttons)
            remove(play_menu_buttons)
            remove(level_menu_buttons)
            remove(credits_menu_buttons)
            writer.clear()
            menu(main_menu, main_menu_buttons)
            drawn = True
        
        if check_click(main_menu_buttons):
            x, y = 600, 600
    
    #EXIT.
    elif game_state == "exit":
        game = False
        
    #CREDITES.
    elif game_state == "credits":
        if not drawn:
            remove(main_menu_buttons)
            remove(play_menu_buttons)
            remove(level_menu_buttons)
            menu(credits_menu, credits_menu_buttons)
            drawn = True
        
        if check_click(credits_menu_buttons):
            x, y = 600, 600
            
        writer.display("""
                       Developer : David Magdy
                       Version : 1.0
                       """, pos=(-50,0))
        
        
    #PLAY MENU.
    elif game_state == "play_menu":
        if not drawn:
            remove(main_menu_buttons)
            remove(play_menu_buttons)
            remove(level_menu_buttons)
            menu(play_menu, play_menu_buttons)
            drawn = True
        
        if check_click(play_menu_buttons):
            x, y = 600, 600
            
    #MULTIPLAYER.
    elif game_state == "multiplayer":
        x, y = 600, 600
        multiplayer()
        
    #LEVEL MENU.
    elif game_state == "level_menu":
        if not drawn:
            remove(main_menu_buttons)
            remove(level_menu_buttons)
            menu(level_menu, level_menu_buttons)
            drawn = True
        
        if check_click(level_menu_buttons):
            x, y = 600, 600
            
    #EASY MODE.
    elif game_state == "easy_mode":
        x, y = 600, 600
        singleplayer(16)
        
    #MEDIUM MODE.
    elif game_state == "medium_mode":
        x, y = 600, 600
        singleplayer(8)
        
    #HARD MODE.
    elif game_state == "hard_mode":
        x, y = 600, 600
        singleplayer(4)
        
    #IMPOSSIBLE MODE.
    elif game_state == "impossible_mode":
        x, y = 600, 600
        singleplayer(1)
          
window.exitonclick()