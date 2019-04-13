#!/bin/python3

# From: https://projects.raspberrypi.org/en/projects/turtle-race

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
Mai = Turtle()
Mai.color('red')
Mai.shape('turtle')

Mai.penup()
Mai.goto(-160, 100)
Mai.right(360)
Mai.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.right(360)
bob.pendown

Malou = Turtle()
Malou.color('Green')
Malou.shape('turtle')

Malou.penup()
Malou.goto(-160, 40)
Malou.right(360)
Malou.pendown()

Pai = Turtle()
Pai.color('yellow')
Pai.shape('turtle')

Pai.penup()
Pai.goto(-160, 10)
Pai.right(360)
Pai.pendown()

for turn in range(100):
  Mai.forward(randint(1,5))
  bob.forward(randint(1,5))
  Malou.forward(randint(1,5))
  Pai.forward(randint(1,5))

