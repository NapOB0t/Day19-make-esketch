from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def moveforward():# move tim forward by 100
    tim.forward(100)

def movebackward(): # move tim backward by 100
    tim.backward(100)

def anticlock():# turn the heading of tim or direction by 45 degrees anticlockwise.
    tim.right(45)

def clockw():# turn tim's heading or deirection 45 degrees clockwise.
    tim.left(45)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
#These commands set the screen listener to respond to specific key strokes in order to activate specific events
screen.onkey(key='w', fun=moveforward)
screen.onkey(key='s', fun=movebackward)
screen.onkey(key='a', fun=anticlock)
screen.onkey(key='d', fun=clockw)
screen.onkey(key='c', fun=clear)
screen.exitonclick()





