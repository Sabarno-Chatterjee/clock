from turtle import Turtle, Screen
from clock import Clock
import datetime

screen = Screen()
screen.title("Clock")
screen.setup(800, 800)
screen.setworldcoordinates(-800, -800, 800, 800)
screen.tracer(0, 0)
screen.bgcolor("yellow green")


def animate():
    global clock
    d = datetime.datetime.now()
    clock.hour = d.hour
    clock.minute = d.minute
    clock.second = d.second
    clock.draw_hand()
    screen.update()
    screen.ontimer(animate, 800)


d = datetime.datetime.now()
clock = Clock(d.hour, d.minute, d.second)
clock.draw_face()
screen.update()
animate()

screen.exitonclick()
