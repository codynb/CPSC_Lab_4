#the theauthorsaremaggiedunnandcodybrown L2
import turtle
amy = turtle.Turtle()
amy.color('yellow')
for side in range(4):
    if side == 1:
        amy.color('blue')
    if side == 2:
        amy.color('green')
    if side == 3:
        amy.color("magenta")
    amy.forward(100)
    amy.right(90)
