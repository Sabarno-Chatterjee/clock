from turtle import Turtle, Screen
from clock import Clock
import datetime

screen = Screen()
screen.title("Clock")
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)
screen.bgcolor("yellow green")

clock = Clock(12,1,1)
clock.draw_face()

screen.exitonclick()
