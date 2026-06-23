"""
The Menu File (Module) Used In Tic Tac Toe Project.
This File Handles Many Variables And Functions That Will Inserted To The Main File (Tic_Tac_Toe.py).
This File Imports Data Handlers And Imports Button From Display File (Module).

******VARIABLES******
-main_menu Is a Menu That Stores Data From Main File (main.py).
-main_menu_buttons Is a List That Stores Buttons And Their Information Inside Button Class (Attributes).

-play_menu Is a Menu That Stores Data From Play File (play.py).
-play_menu_buttons Is a List That Stores Buttons And Their Information Inside Button Class (Attributes).

-level_menu Is a Menu That Stores Data From Level File (level.py).
-level_menu_buttons Is a List That Stores Buttons And Their Information Inside Button Class (Attributes).

-credits_menu Is a Menu That Stores Data From Credits File (credits.py).
-credits_menu_buttons Is a List That Stores Buttons And Their Information Inside Button Class (Attributes).
"""

from data import main, play, level, credits
from display import Button

#MENUS.
main_menu = main.MAIN_MENU
main_menu_buttons = []

play_menu = play.PLAY_MENU
play_menu_buttons = []

level_menu = level.LEVEL_MENU
level_menu_buttons = []

credits_menu = credits.CREDITS_MENU
credits_menu_buttons = []
    
#CREATE MENUS.
def create(list, list_buttons):
    """
    The Function That Creates Buttons.

    Args:
        list (_type_): _description_
        list_buttons (_type_): _description_
    """
    for buttons in list:
        button = list[buttons]
        list_buttons.append(Button(x=button["x"], y=button["y"], prompt=button["prompt"], color=button["color"], pencolor=button["pencolor"], textcolor=button["textcolor"], textsize=button["textsize"], texttype=button["texttype"], x_space=button["x_space"], y_space=button["y_space"]))

#DRAW LIST.
def draw(list_buttons):
    """
    The Function That Draws Buttons (Shows Buttons).

    Args:
        list_buttons (_type_): _description_
    """
    for button in list_buttons:
        button.draw()
        
#REMOVE BUTTONS.
def remove(list_buttons):
    """
    The Function That Removes Buttons.

    Args:
        list_buttons (_type_): _description_
    """
    
    for button in list_buttons:
        button.clear()
        
#MENU FUNCTION.
def menu(list, list_buttons):
    """
    The Function That Creates Menu If Not Created Before and Draws Them.

    Args:
        list_buttons (_type_): _description_
    """
    
    if not list_buttons:
        create(list, list_buttons)
    draw(list_buttons)
    