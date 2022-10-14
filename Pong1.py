# Part 1: Getting start
import turtle
import time
from Equipments import *

width, height = 1024, 768
score_l, score_r = 0, 0

# Create paddle and ball objectss
paddle_a = Paddle((-width/2*7/8, 0))
paddle_b = Paddle((width/2*7/8, 0))
ball_1 = Ball(size=10, speed=4)
pen = Pen((0, height/2*4/5))

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


# Main game loop
while True:
    window.update()
    
    # Move the Ball
    ball_1.move()
    time.sleep(.001)

    # Border checking
    ball_1.touch_border_y(height)
    score = ball_1.touch_border_x(width)
    if score:
        if score > 0:
            score_r += 1
            pen.updateScore(score_l, score_r)
        else:
            score_l += 1
            pen.updateScore(score_l, score_r)
    ball_1.bounce_paddle(paddle_a)
    ball_1.bounce_paddle(paddle_b)

    # Paddles touching