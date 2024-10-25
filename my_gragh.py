import turtle
def p30(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def p31(x, y, radius, color):
    turtle.penup()        
    turtle.goto(x, y - radius) 
    turtle.fillcolor(color)    
    turtle.pendown()           
    turtle.begin_fill()        
    turtle.circle(radius)      
    turtle.end_fill()          

def p32(startX, startY, endX, endY, color):
    turtle.penup()              
    turtle.goto(startX, startY) 
    turtle.pendown()            
    turtle.pencolor(color)      
    turtle.goto(endX, endY)