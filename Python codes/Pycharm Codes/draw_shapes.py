import turtle


def draw_square(turtle1):
    for j in range (1,361):
        for i in range(1,5):
            turtle1.forward(100)
            turtle1.right(90)
            #print("Square completed.")
        turtle1.right(1)



def draw_circle(turtle2):
    turtle2.circle(100)


def draw_shape():
    windows = turtle.Screen()
    windows.bgcolor("red")
    windows.title("Shapes")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.fillcolor("yellow")

    brad.speed(50)
    draw_square(brad)

    angie = turtle.Turtle()
    angie.color("white")
    draw_circle(angie)

    windows.exitonclick()


draw_shape()
