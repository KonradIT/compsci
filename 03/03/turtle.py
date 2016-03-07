import turtle
import time

green = turtle.Turtle()
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()

green.color("green")
green.forward(100) 
green.left(270) 
green.forward(100)

red.color("red")
red.left(90)  
red.forward(100)
red.left(270)
red.forward(100)

blue.color("blue")
blue.backward(100)
blue.right(270)
blue.forward(100)

yellow.color("yellow")
yellow.left(270)
yellow.forward(100)
yellow.right(90)
yellow.forward(100)

time.sleep(5)
green.left(270) 
green.forward(100)
red.left(270)
red.forward(100)
blue.left(270)
blue.forward(100)
yellow.right(90)
yellow.forward(100)

time.sleep(5)
turtle.write("WE DON'T TRACK YOU /s",align="center", font=("Arial", 16, "normal"))
time.sleep(5)
