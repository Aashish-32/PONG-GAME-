import turtle

# Set up the screen
turtle.Screen()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Ping Pong game by Aaryan")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)

paddle_aspeed = 20
paddle_bspeed = 20

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.dy = 0.5
ball.dx = 0.5


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_aspeed
    paddle_a.sety(y)

turtle.listen()
turtle.onkey(paddle_a_up, "Up")


def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_aspeed
    paddle_a.sety(y)

turtle.listen()
turtle.onkey(paddle_a_down, "Down")

def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_bspeed
    paddle_b.sety(y)

turtle.listen()
turtle.onkey(paddle_b_up, "w")

def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_bspeed
    paddle_b.sety(y)

turtle.listen()
turtle.onkey(paddle_b_down, "s")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.penup()
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > -290:
        y = ball.ycor()
        y *= -1
        ball.sety(y)