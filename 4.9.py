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

t = turtle.Turtle()
t.pensize(4)
t.pencolor(pink)
t.speed(10)

size = 20
for i in range(5):
  for j in range(4):
    t.forward(size)
    t.left(90)
  size += 20
  t.penup()
  t.goto(-size/2, -size/2)
  t.pendown()

turtle.done()
