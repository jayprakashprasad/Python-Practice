#Python program to draw spiral square in turtle programming

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


import turtle
 
t = turtle.Turtle()
side = 200
for i in range(100):
   t.forward(side)
   t.right(90) #Exterior angle of a square is 90 degree
   side = side - 2

#Python program to draw spiral star in turtle programming
import turtle
 
t = turtle.Turtle()
side = 200
for i in range(100):
   t.forward(side)
   t.right(144) #Exterior angle of a star is 144 degree
   side = side - 2

#Python program to draw spiral triangle in turtle programming
import turtle
 
t = turtle.Turtle()
side = 200
for i in range(70):
   t.forward(side)
   t.right(120) #Exterior angle of a triangle is 120 degree
   side = side - 3

#Python program to draw spiral pentagon in turtle programming
import turtle
 
t = turtle.Turtle()
side = 200
for i in range(104):
   t.forward(side)
   t.right(72) #Exterior angle of a pentagon is 72 degree
   side = side - 2

#Python program to draw spiral polygon in turtle programming
import turtle
  
t = turtle.Turtle()
numberOfSides = int(input('Enter the number of sides of a polygon: '))
lengthOfSide = int(input('Enter the length of a side of a polygon: '))
exteriorAngle = 360/numberOfSides
for i in range(200):
   t.forward(lengthOfSide)
   t.right(exteriorAngle)
   lengthOfSide = lengthOfSide - 0.5



