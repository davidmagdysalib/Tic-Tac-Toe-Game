#POSITION OF DRAWING AND CHECKING THE MAIN POSITION OF CLICK.
POSITIONS = {
    1 : {
        "draw" : (-80, -80),
        "x_range" : (-120, -40),
        "y_range" : (-120, -40)
    }, 
    
    2 : {
        "draw" : (0, -80),
        "x_range" : (-40, 40),
        "y_range" : (-120, -40)
    }, 
    
    3 : {
        "draw" : (80, -80),
        "x_range" : (40, 120),
        "y_range" : (-120, -40)
    }, 
    
    4 : {
        "draw" : (-80, 0),
        "x_range" : (-120, -40),
        "y_range" : (-40, 40),
    }, 
    
    5 : {
        "draw" : (0, 0),
        "x_range" : (-40, 40),
        "y_range" : (-40, 40)
    }, 
    
    6 : {
        "draw" : (80, 0),
        "x_range" : (40, 120),
        "y_range" : (-40, 40)
    }, 
    
    7 : {
        "draw" : (-80, 80),
        "x_range" : (-120, -40),
        "y_range" : (40, 120)
    }, 
    
    8 : {
        "draw" : (0, 80),
        "x_range" : (-40, 40),
        "y_range" : (40, 120)
    }, 
    
    9 : {
        "draw" : (80, 80),
        "x_range" : (40, 120),
        "y_range" : (40, 120)
    }, 
}

#WINNING POSSIBLITIES.
WINS = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    
    [1,4,7],
    [2,5,8],
    [3,6,9],
    
    [1,5,9],
    [3,5,7]
]
