from turtle import Turtle
import random

COLORS = ["green", "blue", "red", "purple", "pink", "orange", "yellow", "magenta"]


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.face = Turtle()
        self.hand = Turtle()
        self.draw_pattern = Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()
        self.draw_pattern.hideturtle()

    def draw(self):
        self.draw_face()
        self.draw_hand()

    def draw_face(self):
        self.face.clear()
        self.face.penup()
        self.face.goto(0, -700)
        self.face.pensize(5)
        self.face.pendown()
        self.face.fillcolor("white")
        self.face.begin_fill()
        self.face.circle(700)
        self.face.end_fill()
        self.face.penup()
        self.face.goto(0, 0)
        self.face.dot(10)
        self.face.pensize(2)
        for angle in range(0, 360, 6):
            self.face.penup()
            self.face.goto(0, 0)
            self.face.setheading(90 - angle)
            self.face.forward(620)
            self.face.pendown()
            self.face.forward(30)
        self.face.pensize(4)

        for angle in range(0, 360, 60):
            self.face.penup()
            self.face.goto(0, 0)
            self.face.setheading(90 - angle)
            self.face.forward(600)
            self.face.pendown()
            self.face.forward(50)

    def draw_hand(self):
        # Hour hand
        self.hand.clear()
        self.hand.penup()
        self.hand.goto(0, 0)
        self.hand.setheading(90 - self.hour % 12 * 360 // 12)
        self.hand.pendown()
        self.hand.color("black")
        self.hand.pensize(6)
        self.hand.forward(300)

        # Minute hand:
        self.hand.penup()
        self.hand.goto(0, 0)
        self.hand.setheading(90 - self.minute * 6)
        self.hand.pendown()
        self.hand.color("black")
        self.hand.pensize(4)
        self.hand.forward(400)

        # Second hand:
        self.hand.penup()
        self.hand.goto(0, 0)
        self.hand.color("red")
        self.hand.dot(5)
        self.hand.setheading(90 - self.second * 6)
        self.hand.pendown()
        self.hand.pensize(2)
        self.hand.forward(600)

    def draw_pattern(self):
        self.draw_pattern.penup()
        self.draw_pattern.goto(0, 0)
        self.draw_pattern.pensize(3)
        self.draw_pattern.pendown()
        for pattern in range(100):
            self.draw_pattern.color(random.choice(COLORS))
            self.draw_pattern.forward(100)
            if random.randint(0, 2) == 1:
                self.draw_pattern.right(90)
            else:
                self.draw_pattern.left(90)
