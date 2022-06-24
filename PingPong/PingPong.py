import turtle
import random
import keyboard
import time


while True:
    game = True
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Ping Pong")
    wn.tracer()

    global paddle_yL, paddle_yR
    paddle_yL = 0
    paddle_yR = 0

    """class Ball(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.shape("circle")
            self.color("white")
            self.xS = random.randint(-3, 3)
            self.yS = random.randint(-3, 3)"""

    speed = 0.01

    wn.tracer(0, 0)
    balls = []
    for _ in range(1):
        balls.append(turtle.Turtle())

    for ball in balls:
        ball.penup()
        ball.shape("circle")
        ball.color("white")
        ball.shapesize(1)
        ball.xS = random.choice([-500, 500])
        ball.yS = random.randint(-500, 500)


    def left_paddle(y):
        global paddle_yL
        paddle_yL = y
        l_paddle = turtle.Turtle()
        l_paddle.hideturtle()
        l_paddle.penup()
        l_paddle.color('black')
        l_paddle.goto(-300, 0)
        l_paddle.begin_fill()
        l_paddle.pendown()
        l_paddle.goto(-300, 350)
        l_paddle.goto(-295, 350)
        l_paddle.goto(-295, -350)
        l_paddle.goto(-300, -350)
        l_paddle.goto(-300, 0)
        l_paddle.end_fill()
        l_paddle.penup()
        l_paddle.color('red')
        l_paddle.goto(-300, y)
        l_paddle.begin_fill()
        l_paddle.pendown()
        l_paddle.goto(-300, 30 + y)
        l_paddle.goto(-295, 30 + y)
        l_paddle.goto(-295, -30 + y)
        l_paddle.goto(-300, -30 + y)
        l_paddle.goto(-300, y)
        l_paddle.end_fill()
        l_paddle.penup()


    def right_paddle(y):
        global paddle_yR
        paddle_yR = y
        r_paddle = turtle.Turtle()
        r_paddle.hideturtle()
        r_paddle.penup()
        r_paddle.color('black')
        r_paddle.goto(300, 0)
        r_paddle.begin_fill()
        r_paddle.pendown()
        r_paddle.goto(300, 350)
        r_paddle.goto(295, 350)
        r_paddle.goto(295, -350)
        r_paddle.goto(300, -350)
        r_paddle.goto(300, 0)
        r_paddle.end_fill()
        r_paddle.penup()
        r_paddle.color('blue')
        r_paddle.goto(300, y)
        r_paddle.begin_fill()
        r_paddle.pendown()
        r_paddle.goto(300, 30 + y)
        r_paddle.goto(295, 30 + y)
        r_paddle.goto(295, -30 + y)
        r_paddle.goto(300, -30 + y)
        r_paddle.goto(300, y)
        r_paddle.end_fill()
        r_paddle.penup()


    left_paddle(0)
    right_paddle(0)
    wn.update()
    time.sleep(3)

    while game:
        print("looped")
        time.sleep(0.01)
        wn.tracer(0, 0)
        if keyboard.is_pressed('7'):
            if paddle_yL <= 270:
                left_paddle(paddle_yL + 15)
        elif keyboard.is_pressed('1'):
            if -270 <= paddle_yL:
                left_paddle(paddle_yL - 15)
        if keyboard.is_pressed('9'):
            if paddle_yR <= 270:
                right_paddle(paddle_yR + 15)
        elif keyboard.is_pressed('3'):
            if -270 <= paddle_yR:
                right_paddle(paddle_yR - 15)
                
        for ball in balls:
            ball.goto(ball.xcor() + ball.xS * speed, ball.ycor() + ball.yS * speed)
            if (300 > ball.xcor() > 280) and ((paddle_yR + 30) > ball.ycor() > (paddle_yR - 30)):
                ball.xS = -ball.xS
            elif (-300 > ball.xcor() > -280) and ((paddle_yL + 30) > ball.ycor() > (paddle_yL - 30)):
                ball.xS = -ball.xS
            elif ball.xcor() < -280:
                ball.xS = -ball.xS
            if ball.xcor() > 400:
                game = False
            elif ball.xcor() < -400:
                game = False
            if ball.ycor() > 300:
                ball.yS = -ball.yS
            elif ball.ycor() < -300:
                ball.yS = -ball.yS
        wn.update()
