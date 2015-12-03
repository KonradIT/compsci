#Copyright Konrad Iturbe (@KonradIT at GitHub) 12/3/15
 
import turtle
 
window=turtle.Screen()  
graphic=turtle.Turtle()
 
def thething():
    graphic.forward(50)
    graphic.left(90)
    graphic.forward(100)
    graphic.right(90)
    graphic.forward(100)
    graphic.left(90)
    graphic.forward(100)
 
graphic.color("yellow")
thething()
graphic.color("red")
thething()
graphic.color("green")
thething()
graphic.color("blue")
thething()
 
window.exitonclick()
