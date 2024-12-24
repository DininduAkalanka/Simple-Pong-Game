import turtle
import time

# Screen setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Increase initial speed
ball.dy = -0.2  # Increase initial speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# Instructions
pen.goto(0, 0)
pen.write(
    "How to Play:\nPlayer A: Use 'W' to move up, 'S' to move down.\nPlayer B: Use 'Up Arrow' to move up, 'Down Arrow' to move down.\nPress any key to start!",
    align="center",
    font=("Courier", 16, "normal"),
)
wn.update()
time.sleep(3)  # Display instructions for 3 seconds
pen.clear()

# Display initial scores
pen.goto(0, 260)
pen.write("Player A: 0     Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Keep paddle within the screen
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:  # Keep paddle within the screen
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Keep paddle within the screen
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:  # Keep paddle within the screen
        y -= 20
        paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    time.sleep(0.01)  # Control frame rate for smoother movement

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}     Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}     Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle collisions with faster speed increment
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 9.2  # Speed up after each collision
        ball.dy *= 9.2  # Speed up after each collision

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 9.2  # Speed up after each collision
        ball.dy *=9.2  # Speed up after each collision
