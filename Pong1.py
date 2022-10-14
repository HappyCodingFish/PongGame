# Part 1: Getting start
import turtle
import time
from Equipments import Paddle, Ball

width, height = 1024, 768

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


# Main game loop
while True:
    window.update()
    
    # Move the Ball
    ball_1.move()
    time.sleep(.001)

    # Border checking
    # ball_1.bounce_paddle() <--------------- Stopped here
    ball_1.touch_border(width, height)
    ball_1.bounce_paddle(paddle_a)
    ball_1.bounce_paddle(paddle_b)

    # Paddles touching