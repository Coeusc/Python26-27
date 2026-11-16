import turtle
bob = turtle. Turtle()
bob.speed(0)
turtle.bgcolor("black")
bob.color("blue")
bob.width(1)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def spiral2 (x, y):
    jump(x, y)
    bob.color("red")
    bob.width(0.5)
    for times in range(150):
        bob.circle(times*2)
        bob.forward(times*4)
        bob.left(95)
        
def spiral (x, y):
    jump(x, y)
    bob.color("lightblue")
    for times in range(250):
        bob.circle(times*2)
        bob.forward(times*7)
        bob.left(91)

        
def pento (x, y):
    jump(x, y)
    bob.color("purple")
    for times in range(200):
         bob.circle(100)
         bob.forward(times * 7)
         bob.left(75)

