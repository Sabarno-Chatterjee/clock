from turtle import Turtle


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.face = Turtle()
        self.hand = Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

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
        self.face.penup()
        self.face.goto(0, 0)
        self.face.dot(10)
        self.face.pensize(2)
        for angle in range(0, 360, 6):
            self.face.setheading(90)
            self.face.forward(620)
            self.face.pendown()
            self.face.forward(30)
        self.face.pensize(4)

        for angle in range(0, 360, 60):
            self.face.penup()
            self.face.goto(0, 0)
            self.face.setheading(90)
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
        self.hand.goto(0,0)
        self.hand.setheading(90-self.minute*6)
        self.hand.pendown()
        self.hand.color("black")
        self.hand.pensize(4)
        self.hand.forward(400)

        # Second hand:
        self.hand.penup()
        self.hand.goto(0,0)
        self.hand.color("red")
        self.hand.dot(5)
        self.hand.setheading(90-self.second*6)
        self.hand.pendown()
        self.hand.pensize(2)
        self.hand.forward(600)


