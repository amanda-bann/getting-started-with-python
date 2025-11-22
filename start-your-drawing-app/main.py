# Import the turtle module and random module
import turtle
from turtle import *
import random

screen = turtle.Screen()

screen.bgcolor("lightyellow")
screen.title("My Turtle Drawing App")
screen.setup(width=1200, height=1200)

print("Welcome to your drawing app! Let our cute little tortuga draw shapes for you. Select a shape you want to draw. After typing the number and hitting enter, the drawing app will draw the shape on the canvas.")

# Create a turtle object
tortuga_turtle = turtle.Turtle()
tortuga_turtle.shape("turtle")
tortuga_turtle.shapesize(2, 2, 2)
tortuga_turtle.speed(2)
tortuga_turtle.color("lightgreen")
tortuga_turtle.pencolor("darkgreen")
tortuga_turtle.pensize(4)

tortuga_turtle.penup()
# tortuga_turtle.left(45)
# tortuga_turtle.forward(100)
tortuga_turtle.left(180)
tortuga_turtle.forward(400)
tortuga_turtle.right(90)
tortuga_turtle.forward(400)

tortuga_turtle.pendown()

tortuga_turtle.write("Tortuga's Drawing App", font=("Arial", 24, "bold", "italic"))

tortuga_turtle.penup()
tortuga_turtle.right(180)
tortuga_turtle.forward(50)
tortuga_turtle.pendown()

tortuga_turtle.write("To draw a shape, go to the console and choose an option!", font=("Arial", 20, "bold"))

tortuga_turtle.penup()
tortuga_turtle.forward(50)
tortuga_turtle.left(60)
tortuga_turtle.forward(450)
tortuga_turtle.pendown()

# Draw a hexagon
def hexagon():
    # hexagon
    for i in range(0,6):
        tortuga_turtle.pencolor("blue")
        tortuga_turtle.forward(100)
        tortuga_turtle.right(60)


#Bonus: Draw a square
def square():
    # square
    for i in range(0,4):
        tortuga_turtle.pencolor("magenta")
        tortuga_turtle.forward(200)
        tortuga_turtle.right(90)
# Clear the drawing
# tortuga_turtle.clear()

#Bonus: Draw a star
def star():
    # star
    for i in range(0,5):
        tortuga_turtle.pencolor("cyan")
        tortuga_turtle.forward(110)
        tortuga_turtle.right(216)

# Bonus: Draw a circle
def circle():
    # circle
    tortuga_turtle.pencolor("violet")
    tortuga_turtle.circle(100)

# Bonus: Draw a triangle
def triangle():
    # triangle
    for i in range(0,3):
        tortuga_turtle.pencolor("hotpink")
        tortuga_turtle.forward(150)
        tortuga_turtle.right(120)

# Draw a fancy star
def fancy_star():
    # fancy star
    tortuga_turtle.penup()
    tortuga_turtle.home()
    tortuga_turtle.pendown()
    tortuga_turtle.pensize(2)
    tortuga_turtle.speed(5)
    tortuga_turtle.color('magenta', "lavender")
    tortuga_turtle.begin_fill()
    while True:
        tortuga_turtle.forward(200)
        tortuga_turtle.left(170)
        if abs(tortuga_turtle.pos()) < 1:
            break
    tortuga_turtle.end_fill()
    # tortuga_turtle.done()

Selection = input("1: Hexagon, 2: Square, 3: Star, 4: Circle, 5: Triangle, 6: Fancy Star. Please enter the number of the shape you want to draw: ")
if Selection == "1":
    print("Hexagon! Go, Tortuga, go!")
    hexagon()
    
    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(400)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user

elif Selection == "2":
    print("Square! Get it, Tortuga, go!")
    square()
    
    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(450)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user

elif Selection == "3":
    print("Star! Shine bright, Tortuga, go!")
    star()

    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(300)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user

elif Selection == "4":
    print("Circle! Round 'em up, Tortuga, go!")
    circle()
    
    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(300)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user

elif Selection == "5":
    print("Triangle! Point 'em out, Tortuga, go!")
    triangle()

    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(300)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user

elif Selection == "6":
    print("Fancy Star! Show your stuff, Tortuga, go!")
    fancy_star()
    # screen.exitonclick() # Leave the canvas open until closed by the user
    tortuga_turtle.penup()
    tortuga_turtle.right(180)
    tortuga_turtle.forward(150)
    tortuga_turtle.left(90)
    tortuga_turtle.forward(300)
    tortuga_turtle.pendown()

    tortuga_turtle.write("      Muchas gracias, Tortuga! To close the screen, click on it!", font=("Arial", 20, "bold", "italic"))
    screen.exitonclick() # Leave the canvas open until closed by the user
