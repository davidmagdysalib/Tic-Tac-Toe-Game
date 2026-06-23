"""
The write File (Module) That Handles A Class Which Will Be Inserted To Main File (Tic_Tac_Toe.py).
The write File Imports Turtle Class From turtle Module To Display Prompts Along turtle.screen.

******CLASSES******
1- Writer Class : It Inherits From Turtle Class And Its Responsible For Displaying Prompts.
                  It Also Have Built in Methods For Winning, Losing and Draw.
                  It Also Have a Built In Method For Reseting Game (again()).
"""

#IMPORTS.
from turtle import Turtle

#CLASSES.
class Writer(Turtle):
    """
    The Writer Turtle That Inehert from Turtle Class inside turtle Module.
    """
    
    def __init__(self):
        """
        The Initialize Magic Method.
        """
        
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.display('Tic Tac Toe Game !', 'white', 25)
        
    def display(self, prompt, color='white', size=16, pos=(0, 200)):
        """
        The Display Method That Displays Prompts.

        Args:
            message (_type_): _description_
            color (str, optional): _description_. Defaults to 'white'.
            size (int, optional): _description_. Defaults to 16.
            pos (tuple, optional): _description_. Defaults to (0, 200).
        """
        
        self.goto(pos)
        self.color(color)
        self.clear()
        self.write(prompt, align='center', font=("arial", size, 'bold'))
        
    def lost(self):
        """
        The Losing Method.
        """
        
        self.display('You Lost !')
        self.screen.bgcolor('darkred')
        
    def draw(self):
        """
        The Draw Method.
        """
        
        self.display('Draw !')
        self.screen.bgcolor('darkgrey')
        
    def won(self):
        """
        The Win Method.
        """
        
        self.display('You Won !')
        self.screen.bgcolor('darkgreen')
        
    def again(self):
        """
        The Method That Returns Game To Normal Screen.
        """
        
        self.display('Tic Tac Toe Game !')
        self.screen.bgcolor('black')
        