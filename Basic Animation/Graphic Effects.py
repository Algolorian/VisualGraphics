# Basic Animation in Python 3
# Part 6: Using Classes
# by Christian Thompson AKA @TokyoEdTech
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")
turtle.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("green")
        self.frame = 0
        self.frames = ["circle", "square"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])
        # Set timer
        wn.ontimer(self.animate, 500)


for h in range(7):
    turtle.tracer(0, 0)
    for i in range(7):
        player = Player()
        player.animate()
        player.goto(-100 * h + 300, -100 * i + 300)
    time.sleep(0.15)
    turtle.update()

while True:
    wn.update()
    print("Main Loop")
