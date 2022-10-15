import turtle
import winsound

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
        self.size = size
        self.hits = 0
        self.h_b, self.l_b, _ = (p * 10 for p in self.shapesize())

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def touch_border_y(self, window_height):
        if  self.ycor() + self.h_b > window_height/2:
            self.dy *= -1
            self.sety(window_height/2 - self.h_b)
            
        elif self.ycor() - self.h_b< -window_height/2:
            self.dy *= -1
            self.sety(-window_height/2 + self.h_b)
            
    def touch_border_x(self, window_width):
        if  self.xcor() + self.l_b > window_width/2:
            self.dx *= -1
            self.goto(0, 0)
            self.hits = 0

            return -1
        elif self.xcor() - self.l_b < -window_width/2:
            self.dx *= -1
            self.goto(0, 0)
            self.hits = 0
            return 1

    def bounce_paddle(self, paddle):
        x = paddle.xcor()
        y = paddle.ycor()
        h_p, l_p, _ = (p * 10 for p in paddle.shapesize())
        
        if x < 0:
            if (x < self.xcor() - self.l_b < x + l_p) and \
                y - h_p - self.h_b < self.ycor() < y + h_p + self.h_b:
                self.dx *= -1
                self.hits += 1
                self.enlarge()
                winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)
                self.setx(x + l_p + self.l_b)
                return 1

            elif self.xcor() - self.l_b < x:
                if y < self.ycor() - self.h_b < y + h_p:
                    self.dy *= -1
                    self.sety(y + h_p + self.h_b)
                    winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)

                elif y > self.ycor() + self.h_b > y - h_p:
                    self.dy *= -1
                    self.sety(y - h_p - self.h_b)
                    winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)
                   
        else:
            if (x > self.xcor() + self.l_b > x - l_p) and \
            y - h_p - self.h_b < self.ycor() < y + h_p + self.h_b:
                self.dx *= -1
                self.hits += 1
                self.enlarge()
                winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)
                self.setx(x - l_p - self.l_b)
                return 1

            elif self.xcor() + self.l_b > x:
                if y < self.ycor() - self.h_b < y + h_p:
                    self.dy *= -1
                    self.sety(y + h_p + self.h_b)
                    winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)
                    
                elif y > self.ycor() + self.h_b > y - h_p:
                    self.dy *= -1
                    self.sety(y - h_p - self.h_b)
                    winsound.PlaySound("bounce_table.wav", winsound.SND_ASYNC)
    def enlarge(self):
        if self.hits > 9:
            self.shapesize(stretch_wid=self.size + self.hits // 10, stretch_len=self.size + self.hits // 10)
            self.h_b, self.l_b, _ = (p * 10 for p in self.shapesize())

class Pen(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(*position)
        self.write("Player A: 0 \t Player B: 0", 
                    align="center", font=("Courier", 24, "normal"))

    def updateBoard(self, p1_score, p2_score, hits):
        self.clear()
        self.write("Player A: {} \t Player B: {} \t Hits: {}".format(p1_score, p2_score, hits), 
                    align="center", font=("Courier", 24, "normal"))

