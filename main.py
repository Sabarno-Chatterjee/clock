from turtle import Turtle, Screen
from clock import Clock
import datetime

screen = Screen()
screen.title("Clock")
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
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
    screen.ontimer(animate, 1000)


d = datetime.datetime.now()
clock = Clock(d.hour, d.minute, d.second)
clock.draw_face()
screen.update()
animate()

screen.exitonclick()
