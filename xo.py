"""
The XO File That Handles Two Classes That Will Be Inserted To Main Projects File (Tic_Tac_Toe.py).
The XO File That Imports Turtle Class From Turtle Module To Create Drawings Along turtle.screen.

******CLASSES******
1-O Class: It Draws In a Certain Position Using .draw(position) Method And Deletes All Drawings Using .delete() Method.
2-X Class: It Draws In a Certain Position Using .draw(position) Method And Deletes All Drawings Using .delete() Method.
"""

#IMPORTS.
from turtle import Turtle

#CLASSES.
class O:
    """
    Class Of Whole O's.
    """
    
    def __init__(self):
        """
        Initialize Magic Method.
        """
        
        self.turtles = []
    
    def draw(self, position):
        """
        Drawing Method To Draw The O In Different Positions.

        Args:
            position (_type_): _description_
        """
        
        #SETTING UP....
        block = Turtle()
        block.hideturtle()
        block.color('white')
        block.penup()
        block.goto(position)
        block.goto(block.xcor(), block.ycor()-20)
        block.pendown()
        block.pensize(3.5)
        #DRAWING....
        block.circle(20)
        self.turtles.append(block)
        
    def delete(self):
        """
        Deleting Method That Deletes Whole O Draws.
        """
        
        for i in self.turtles:
            i.clear()
            
class X:
    """
    Class Of Whole X's.
    """
    
    def __init__(self):
        """
        Initialize Magic Method.
        """
        
        self.turtles = []
    
    def draw(self, position):
        """
        Drawing Method To Draw The X In Different Positions.

        Args:
            position (_type_): _description_
        """
        
        #SETTING UP......
        block = Turtle()
        block.hideturtle()
        block.color('white')
        block.penup()
        block.goto(position)
        block.pensize(3.5)
        
        #DRAWING....
        block.goto(block.xcor()+20, block.ycor()+20)
        block.pendown()
        block.goto(block.xcor()-40, block.ycor()-40)
        block.penup()
        block.goto(block.xcor(), block.ycor()+40)
        block.pendown()
        block.goto(block.xcor()+40, block.ycor()-40)
        self.turtles.append(block)
        
    def delete(self):
        """
        Deleting Method That Deletes Whole X Draws.
        """
        
        for i in self.turtles:
            i.clear()
            