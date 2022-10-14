# Part 1: Getting start
import turtle
import time

width, height = 1024, 768
screenEdge_w, screenEdge_h = width/2 - 10, height/2 - 10

# Paddles and Balls Classes
class Paddle(turtle.Turtle):
    def __init__(self, position, length=5):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=length, stretch_len=1)
        self.penup()
        self.goto(*position)

    # Function For Paddle
    def paddle_up(self):
        self.sety(self.ycor() + 20)

    def paddle_down(self):
        self.sety(self.ycor() - 20)

class Ball(turtle.Turtle):
    def __init__(self, position=(0, 0), size=1, speed=2):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.penup()
        self.goto(*position)
        self.dx = speed
        self.dy = speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def touch_border(self):
        global screenEdge_h, screenEdge_w
        
        if  self.ycor() > screenEdge_h:
            self.sety(screenEdge_h)
            self.dy *= -1
        elif self.ycor() < -screenEdge_h:
            self.sety(-screenEdge_h)
            self.dy *= -1

        if  self.xcor() > screenEdge_w:
            self.goto(0, 0)
            self.dx *= -1
        elif self.xcor() < -screenEdge_w:
            self.goto(0, 0)
            self.dx *= -1

    def bounce_paddle(self, paddle):
        x = paddle.xcor()
        y = paddle.ycor()
        h_p, l_p, _ = (p * 10 for p in paddle.shapesize())
        h_b, l_b, _ = (p * 10 for p in self.shapesize())

        if x < 0:
            if (x < self.xcor() - l_b < x + l_p) and \
                y - h_p - h_b < self.ycor() < y + h_p + h_b:
                self.dx *= -1
                self.setx(x + l_p + l_b)
            elif self.xcor() - l_b < x:
                if y + h_p - l_p < self.ycor() - h_b < y + h_p:
                    self.dy *= -1
                    self.sety(y + h_p + h_b)
                elif y - h_p + l_p > self.ycor() + h_b > y - h_p:
                    self.dy *= -1
                    self.sety(y - h_p - h_b)
        else:
            if (x > self.xcor() + l_b > x - l_p) and \
            y - h_p - h_b < self.ycor() < y + h_p + h_b:
                self.dx *= -1
                self.setx(x - l_p - l_b)
            elif self.xcor() + l_b > x:
                if y + h_p - l_p < self.ycor() - h_b < y + h_p:
                    self.dy *= -1
                    self.sety(y + h_p + h_b)
                elif y - h_p + l_p > self.ycor() + h_b > y - h_p:
                    self.dy *= -1
                    self.sety(y - h_p - h_b)

# Create paddle and ball objectss
paddle_a = Paddle((-width/2*7/8, 0))
paddle_b = Paddle((width/2*7/8, 0))
ball_1 = Ball(size=10, speed=4)

# Set up window
window = turtle.Screen()
window.title("Pong by HappyCodingFish")
window.bgcolor("black")
window.setup(width=width, height=height)
window.tracer(0)

# KeyBoard Binding
window.listen()
window.onkeypress(paddle_a.paddle_up, "w")
window.onkeypress(paddle_a.paddle_down, "s")
window.onkeypress(paddle_b.paddle_up, "Up")
window.onkeypress(paddle_b.paddle_down, "Down")
window.ontimer(ball_1.move, 100)

# Main game loop
while True:
    window.update()
    
    # Move the Ball
    ball_1.move()
    time.sleep(.001)

    # Border checking
    # ball_1.bounce_paddle() <--------------- Stopped here
    ball_1.touch_border()
    ball_1.bounce_paddle(paddle_a)
    ball_1.bounce_paddle(paddle_b)

    # Paddles touching