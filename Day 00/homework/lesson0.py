
from turtle import *


#we want to paint a house 

#step 1: draw a square
width(7)
colormode("black")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("white")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200  )
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
right(60)
end_fill()

#window
penup()
goto(60,180)
pendown()
color("pink")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()
penup()
goto(180,180)
pendown()
color("pink")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()
exitonclick()