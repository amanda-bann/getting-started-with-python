# Import the turtle module
import turtle

screen = turtle.Screen()

screen.bgcolor("lightyellow")
screen.title("My Turtle Drawing App")
screen.setup(width=600, height=600)

# Create a turtle object
tortuga_turtle = turtle.Turtle()

tortuga_turtle.shape("turtle")
tortuga_turtle.speed(2)
tortuga_turtle.color("purple")
tortuga_turtle.pensize(5)
# Set pen color to blue
tortuga_turtle.pencolor("blue")

# Move the pen forward by 100 pixels
#tortuga_turtle.forward(100)
# Rotate the pen right by 60 degrees
#tortuga_turtle.right(60)

# Draw a hexagon
for _ in range(6):
    tortuga_turtle.forward(100)
    tortuga_turtle.right(60)

# Clear the drawing
tortuga_turtle.clear()

#Bonus: Draw a square
tortuga_turtle.pencolor("green")
for _ in range(4):
    tortuga_turtle.forward(100)
    tortuga_turtle.right(90)

# Clear the drawing
tortuga_turtle.clear()

#Bonus: Draw a star
tortuga_turtle.pencolor("lavender")
for _ in range(5):
    tortuga_turtle.forward(110)
    tortuga_turtle.right(216)

# Leave the canvas open until closed by the user
screen.exitonclick()