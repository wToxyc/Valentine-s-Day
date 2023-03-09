from turtle import *

title("Valentine's Day")

hideturtle()

color("red")
bgcolor("black")
fillcolor("red")

begin_fill()

def curve():
    for i in range(200):
        right(1)
        forward(1)

left(140)
forward(133)

curve()
left(120)
curve()

end_fill()

done()