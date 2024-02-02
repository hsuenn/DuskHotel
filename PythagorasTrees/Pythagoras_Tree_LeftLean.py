# Name: Choo Tze Hsuen
# Admin No.: 220926F
# Tutorial Group: AA2301

import turtle
import math
'''
    :param t: turtle object
    :param size: side length of square
    :param level: recursive parameter
    :param angle: left-side angle for Pythagoras tree, range in (0, 90)
                  angle < 45: left-leaning Pythagoras tree
                  angle = 45: balanced Pythagoras tree
                  angle > 45: right-leaning Pythagoras tree
    '''

# define color list
Color_list = ['plum','plum3','PapayaWhip','PeachPuff','pink','PaleVioletRed3','PaleVioletRed4',
                  'firebrick4']
num_color = len(Color_list)

screen = turtle.Screen()
screen.bgcolor("skyblue4")
# This turns off screen updates
screen.tracer(0)

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("black")
myTurtle.fillcolor("green")
myTurtle.speed(3)

# Draw a single square of the given size, and fill it in
def drawBranch(t, size, color):
  myTurtle.pencolor(color)
  t.pendown()
  t.width(size/10)
  t.forward(size)
  t.penup()

# Draw a node at the given level, recursively drawing all
# the smaller nodes
def drawNode(t, size, level, angle=30):
  if (level < 1):
    return
  else:
    drawBranch(t, size, Color_list[(level-1)%num_color])

    # re-computed using Pythagoras formula
    leftSize = size * math.cos(angle*math.pi/180)
    rightSize = size * math.sin(angle*math.pi/180)

    # Draw the left branch
    t.left(angle) # if left-side angle is 45 degrees, this angle is 180-45=135
    t.forward(rightSize/2)
    drawNode(t, leftSize, level - 1, angle)

    # Draw the right branch
    t.right(90+angle)
    t.forward(size/2)
    t.left(angle)
    drawNode(t, rightSize, level - 1, angle)
    t.back(leftSize/2)
    t.left(90-angle)
    t.back(size)

# Position the turtle, and start drawing!
myTurtle.penup()
myTurtle.goto(0, -150)
myTurtle.left(90)

# Note: 14 levels will take a while to draw!  You can try
# a smaller number, but then the tree won't be as detailed.
drawNode(myTurtle, 80, 14)

myTurtle.hideturtle()

# Update the screen to see the changes
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()