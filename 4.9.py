#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjfalcon-argot
#
# Created:     09/09/2025
# Copyright:   (c) cjfalcon-argot 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")
pen.color("hotpink")
pen.pensize(5)

t = turtle.Turtle()
t.speed(5)

for i in range(5):
  for j in range(4):
    t.forward(50 + i + 20)
    t.left(90)
  t.penup()
  t.goto(-10 * (i+1), -10 * (i+1))
  t.pendown()

turtle.done()
