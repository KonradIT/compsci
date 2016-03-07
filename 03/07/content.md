##Fix python code

```
import turtle
import testerino
def run():
    turtle.shape("turtle")
    stepsForward = 0
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)

    while stepsForward < 3:
        turtle.forward(50)
        stepsForward = stepsForward + 1
        turtle.right(90)

        while stepsForward < 5:
            
            count=count+1
            turtle.forward(50)
            stepsForward = stepsForward + 1
            turtle.right(135)
            turtle.forward(50)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            if count == 5:
                run()
count=0
run()

```
