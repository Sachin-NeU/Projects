# import turtle
#
# windows = turtle.Screen()
# windows.title("Spider Web")
# windows.bgcolor("light blue")
# tur = turtle.Turtle()
# tur.shape("turtle")
# tur.speed(2)
#
# size = 200
#
# tur.setheading(90)
# for i in range(0,6):
#     tur.forward(size)
#     tur.penup()
#     tur.forward(-size)
#     tur.pendown()
#     tur.left(60)
#
#
# windows.exitonclick()

import turtle

colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
my_pen.speed(10)
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(61)


turtle.done()



