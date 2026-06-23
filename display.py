"""
The Display File (Module) That Handles Many Classes That Will Be Inserted To Main File (Tic_Tac_Toe.py) and Menus File (menu.py).
The Display File That Imports Turtle Class Responsible For Drawing Border And Buttons Along turtle.screen.

******CLASSES******
1- Border Class : It Inerits From Turtle Class From turtle Module.
                  It Contains Built In Methods That Creates Border And Hides It.
                  
2- Button Class : It Inherits From Turtle Class From turtle Module.
`                 It Contains Built In Methods That Draws Buttons And Displays Prompts.
"""

#IMPORTS.
from turtle import Turtle

#CLASSES.
class Border(Turtle):
    """
    Class Of Borders That Inherits From Turtle Class From turtle Module.
    """
    
    def __init__(self):
        """
        Initialize Magic Method.
        """
        
        super().__init__()
        self.hideturtle()
        self.turtles = []
        self.positions = ( (40, 0),(-40, 0),(0, -40),(0, 40),)
    
    def create(self):
        """
        The Create Method That Creates A Border.
        """
        
        #CREATING.......
        for i in range(4):
            block = Turtle("square")
            block.color('white')
            block.penup()
            if i > 1:
                block.shapesize(0.25, 12)
            else :
                block.shapesize(12, 0.25)
                
            block.goto(self.positions[i])
            self.turtles.append(block)
            
    def hide(self):
        """
        The Hide Method That Clears Border (Hides Border).
        """
        
        for i in self.turtles:
            i.hideturtle()
            
class Button(Turtle):
    """
    Class Of Buttons That Inherits From Turtle Class From turtle Module.
    """
    
    def __init__(self, x, y, prompt, color="white",pencolor= "grey", textcolor="black", texttype="arial", textsize=16, x_space=100, y_space=40):
        """
        Initialize Magic Method.

        Args:
            x (_type_): _description_
            y (_type_): _description_
            prompt (_type_): _description_
            color (str, optional): _description_. Defaults to "white".
            pencolor (str, optional): _description_. Defaults to "grey".
            textcolor (str, optional): _description_. Defaults to "black".
            texttype (str, optional): _description_. Defaults to "arial".
            textsize (int, optional): _description_. Defaults to 16.
            x_space (int, optional): _description_. Defaults to 100.
            y_space (int, optional): _description_. Defaults to 40.
        """
        
        super().__init__()
        #ATTRIBUTES
        
        #SPACES
        self.x_space = x_space
        self.y_space = y_space
        #PROMPT
        self.prompt = prompt
        #POSITIONS
        self.x = x
        self.y = y
        #COLORS
        self.colour = color
        self.pencolour = pencolor
        self.textcolor = textcolor
        #TEXT SETTINGS
        self.textsize = textsize
        self.texttype = texttype
        #USEFUL INFORMATION
        self.area = self.x_space*self.y_space
        self.perimeter = 2*(self.x_space+self.y_space)
        #DIRECTIONS
        self.min_x = self.x - (self.x_space/2)
        self.max_x = self.x + (self.x_space/2)
        self.min_y = self.y - (self.y_space/2)
        self.max_y = self.y + (self.y_space/2)
        #RANGES
        self.x_range = (self.min_x, self.max_x)
        self.y_range = (self.min_y, self.max_y)
        
        self.hideturtle()
        self.penup()
        self.color(self.pencolour, self.colour)
        self.fillcolor(self.colour)
        self.goto(self.x-(self.x_space/2),
                  self.y-(self.y_space/2))
        
    def draw(self):
        """
        The Draw Method That Draws Buttons Using All Of Its Data.
        """
        
        #DRAWING....
        self.fillcolor(self.colour)
        self.begin_fill()
        for _ in range(2):
            self.forward(self.x_space)
            self.left(90)
            self.forward(self.y_space)
            self.left(90)
        self.end_fill()
        self.display()
            
    def display(self):
        """
        The Display Method That Displays Prompts.
        """
        
        self.goto(self.x, self.y-(self.y_space/4))
        self.color(self.textcolor)
        self.write(self.prompt, align='center', font=(self.texttype, self.textsize, 'bold'))
        self.goto(self.x-(self.x_space/2),
                  self.y-(self.y_space/2))
        