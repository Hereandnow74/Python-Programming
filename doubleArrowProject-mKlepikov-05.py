# -*- coding: utf-8 -*-
"""
Program: Turtle Project: Double Arrow
Author: Mikhail Klepikov
Description: This program create a double arrow figure with the help of Turtle graphics module.
Revisions:
    00 - create Turtle tom
    01 - change coordinates from where to draw
    02 - draw the right part of double arrow
    03 - draw the left part of double arrow
    04 - move turtle to origin place (0, 0)
"""

import turtle #access the turtle module
# there are no literal constants
# there are no class definitions
# there are no function definitions

# announcement on the next line
print("Turtle Project: Double Arrow")
# main program begins on the next line
canvas = turtle.Screen() # establish a drawing window
tom = turtle.Turtle() # create a turtle object
tom.penup() # not draw when moving untill we put "pen" down
tom.goto(0, 50) # change coordinates from where to draw
tom.pendown() # put "pen" down to start drawing
'''
tom.forward(№) - draw a line forward to № distance
tom.right(№) - turn right by № units
tom.left(№) - turn left by № units
'''
tom.forward(100) 
tom.right(270) 
tom.forward(50)
tom.right(135) 
tom.forward(141.421) 
tom.right(90) 
tom.forward(141.421) 
tom.right(135) 
tom.forward(50) 
tom.left(90) 
tom.forward(200)
tom.left(90)
tom.forward(50)
tom.right(135)
tom.forward(141.421)
tom.right(90)
tom.forward(141.421)
tom.right(135)
tom.forward(50)
tom.left(90)
tom.forward(100)
tom.right(90)

tom.penup()
tom.home() # move turtle to origin place (0, 0), facing the default direction
tom.pendown()

