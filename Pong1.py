# Part 1: Getting start
import turtle
import time

width, height = 1024, 768
screenEdge_w, screenEdge_h = width/2 - 10, height/2 - 10

# Paddles and Balls Classes
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(*position)

    # Function For Paddle
    def paddle_up(self):
        self.sety(self.ycor() + 20)

    def paddle_down(self):
        self.sety(self.ycor() - 20)

class Ball(turtle.Turtle):
    def __init__(self, position, speed=2):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(*position)
        self.dx = speed
        self.dy = speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_border(self):
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
    def bounce_padder(self):
        pass

# Create paddle and ball objects
paddle_a = Paddle((-width/2*7/8, 0))
paddle_b = Paddle((width/2*7/8, 0))
ball_1 = Ball((0, 0), 4)

# Set up window
window = turtle.Screen()
window.title("Pong by Frank")
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
    time.sleep(.01)

    # Border checking
    # ball_1.bounce_paddle() <--------------- Stopped here
    ball_1.bounce_border()
    

    # Paddles touching