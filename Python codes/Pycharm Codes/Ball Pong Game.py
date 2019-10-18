import turtle
import winsound

windows = turtle.Screen()
windows.title("Practice ball pong")
windows.bgcolor('black')
windows.setup(width=800, height=600)
windows.tracer(0)

# Paddle A
pad_a = turtle.Turtle()
pad_a.color("white")
pad_a.shape("square")
pad_a.speed(0)
pad_a.penup()
pad_a.goto(-350, 0)
pad_a.shapesize(stretch_len=1, stretch_wid=5)

# Paddle B
pad_b = turtle.Turtle()
pad_b.color("white")
pad_b.shape("square")
pad_b.speed(0)
pad_b.penup()
pad_b.goto(350, 0)
pad_b.shapesize(stretch_len=1, stretch_wid=5)

# Ball
ball = turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Scores
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.color("light blue")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1 : {} Player2: {}".format(score_a, score_b),align="center",font=("Arial",20,"normal"))


# Function to move Paddle A up
def pad_a_up():
    y = pad_a.ycor()
    if pad_a.ycor() < 250:
        y += 20
    pad_a.sety(y)


# Function to move Paddle B down
def pad_a_down():
    y = pad_a.ycor()
    if pad_a.ycor() > -250:
        y -= 20
    pad_a.sety(y)


# Function to move Paddle B up
def pad_b_up():
    y = pad_b.ycor()
    if pad_b.ycor() < 250:
        y += 20
    pad_b.sety(y)


# Function to move Paddle B down
def pad_b_down():
    y = pad_b.ycor()
    if pad_b.ycor() > -250:
        y-=20
    pad_b.sety(y)


# Keyboard binding
windows.listen()
windows.onkeypress(pad_a_up, "w")
windows.onkeypress(pad_a_down, "s")
windows.onkeypress(pad_b_up, "Up")
windows.onkeypress(pad_b_down, "Down")


# Main game loop
while True:
    windows.update()

    # Function to move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.dy *= -1
        winsound.PlaySound("Ping-pong-ball-bounce-sound-effect.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.dy *= -1
        winsound.PlaySound("Ping-pong-ball-bounce-sound-effect.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player1 : {} Player2: {}".format(score_a, score_b),align="center",font=("Arial",20,"normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player1 : {} Player2: {}".format(score_a, score_b),align="center",font=("Arial",20,"normal"))

    # Paddle and Ball collision
    if ball.xcor() > 340 and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Ping-pong-ball-bounce-sound-effect.wav",winsound.SND_ASYNC)

    if ball.xcor() < -340 and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Ping-pong-ball-bounce-sound-effect.wav",winsound.SND_ASYNC)

    # if score_b == 2:
    #     windows.bye()
    #     win = turtle.Screen()
    #     win.bgcolor("White")
    #     win.title("Game Over - Result")
    #     win.tracer(0)




