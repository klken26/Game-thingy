"""
This game is a modified version of snake, whose rules can be found at http://somewebsite.com. 
We took reference for the 
1. Logic of snake behaviour
2. Creation of the Game screen

We made changes to the design of the code by
1. Using Object Oriented Programming instead of Procedural style
"""

import turtle
import time
import random

class Snake:
    def __init__(self):
        #Snake Head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 100)
        self.head.direction = "stop"
    def move(self):
        """Moves the Snake"""
        if self.head.direction == "up":
            y = self.head.ycor() #y coordinate of the turtle
            self.head.sety(y + 20)
    
        if self.head.direction == "down":
            y = self.head.ycor() #y coordinate of the turtle
            self.head.sety(y - 20)
    
        if self.head.direction == "right":
            x = self.head.xcor() #y coordinate of the turtle
            self.head.setx(x + 20)
    
        if self.head.direction == "left":
            x = self.head.xcor() #y coordinate of the turtle
            self.head.setx(x - 20)

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
 
    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    
    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

class Food:
    def __init__(self):
        # Snake food
        self.position = turtle.Turtle()
        self.position.speed(0)
        self.position.shape("circle")
        self.position.color("red")
        self.position.penup()
        self.position.shapesize(0.50, 0.50)
        self.position.goto(0, 0)
    def move(self):
        # move the food to a random position on screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.position.goto(x, y)


def setup():
    """Set up the window and snake"""
    #set up the screen
    window = turtle.Screen()
    window.title("OMG A SNAKE IN SUTD?")
    window.bgcolor("lightblue")
    window.setup(width=500,height=500)
    window.tracer(0) # turns off the screen updates
    return window

"""
The code for this function was modified from the code found at
https://www.edureka.co/blog/python-turtle-module/
"""
def main_program():
    """Runs the game"""
    #set up the screen
    window = setup()

    # Create the objects in the game
    snake = Snake()
    food = Food()
    delay=0.1 # slow down the snake

    # Main game loop
    while True:
        window.update()
        snake.move()
        # keyboard bindings
        window.listen()
        window.onkey(snake.go_up, "w")
        window.onkey(snake.go_down, "s")
        window.onkey(snake.go_right, "d")
        window.onkey(snake.go_left, "a")

        if snake.head.distance(food.position) <15: # calculate the distance between the two objects 
            food.move()

        time.sleep(delay)

# Run the programme easily
if __name__ == '__main__':
    main_program()
    
