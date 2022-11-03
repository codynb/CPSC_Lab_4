#theauthorsaremaggiedunnandcodybrown
import turtle
jack = turtle.Turtle()
jack.color('yellow')
for side in range(4):
    if side == 2:
        jack.color('blue')
    jack.forward(100)
    jack.right(90)
