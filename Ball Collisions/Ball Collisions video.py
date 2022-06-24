import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer()

balls = []

for _ in range(25):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5,  5)

gravity = 0.1

while True:
    time.sleep(0.01)

    turtle.tracer(0, 0)
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        # check for wall collisions
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1

        # check for a bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1

    # check for collisions between balls
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):
            # check for a collision
            if balls[i].distance(balls[j]) < 20:
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy

    wn.update()

