# Import the turtle module
# import turtle

# screen = turtle.Screen()

# screen.bgcolor("lightyellow")
# screen.title("My Turtle Drawing App")
# screen.setup(width=600, height=600)


from turtle import *
color('magenta', 'lightgreen')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()