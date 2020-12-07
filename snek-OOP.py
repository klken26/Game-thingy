import turtle
import time            #needed for adding delays in code later
import random          #needed for randomizing numbers later, for position of food
import os


class Snake:
    def __init__(self):
        #Snake Head
        self.head = turtle.Turtle()
        self.head.speed(0) #initialisation does not require movement of head. This will later change via manipulation of coordinates.
        self.head.shape("square")
        self.head.color("black")
        self.head.penup() #removes tracers from being visible
        self.head.goto(0, 100) #absolute position of turtle (centre). Default position of turtle is (0,0) and this is important to know when you're
                               #adding in the segments later; good to know how the turtle objects work.
        self.head.direction = "stop"
        self.segments = []
        self.delay = 0.075 #sets delay, if not update will be continuous at almost infinite speed

#the following function sets the motion of the turtle object 
#when head.direction is set to a specific value. (take note that these methods are object methods)

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

#this set of functions helps to restrict the movement of the snake.
#meaning to say, that it is not able to move in the opposite direction it is currently in. 

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
 
 #if the head is already facing down, you cannot make it go up. this applies to all other directions 

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    
    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def segment_creator(self):
        new_segment = turtle.Turtle()  #creates new object to be pushed into snake.segment
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        self.segments.append(new_segment) #pushes segment into segments array 

#checks for collision. Details are within this function. Take note that this is a static method, which is different from what a object method is.
#it basically is just a function within a class which allows it to be called with multiple methods being used. I used a staticmethod here to demonstrate the different methods available
#but actually you don't have to use a static method. 

    @staticmethod
    def check_collision(obj,otherobj):
        
    # Check for boundary collision
        if obj.head.xcor() > 240 or obj.head.xcor() < -240 or obj.head.ycor() > 250 or obj.head.ycor() < -250: #if it is out of gridbox 
            time.sleep(1)
            obj.head.goto(0, 0)
            obj.head.direction = "stop"
            obj.delay = 0.075  
            # Hide the segments
            for segment in obj.segments:
                #teleports existing blocks to another random space and removes the segment to clear list
                segment.goto(10000, 10000)
            #bug free way to clear array (other methods cause bugs)
            obj.segments.clear()
            # reset score
            otherobj.score = 0
            # update score and updates the score presented in turtle 
            otherobj.newpen.clear()
            otherobj.newpen.color("red")
            otherobj.newpen.goto(0, 180)
            otherobj.newpen.penup()
            otherobj.newpen.hideturtle()
            otherobj.newpen.write("You died! restarting game...", align="center", font=("Courier", 15, "normal"))
            time.sleep(2)
            otherobj.newpen.clear()
            otherobj.pen.clear()
            otherobj.pen.write("score: {} High Score: {}".format(otherobj.score, otherobj.high_score), align="center", font=("Courier", 22, "normal"))

    #Check for head collision
        for segment in obj.segments:
         if segment.distance(obj.head) < 20: #collision requirement: if head is 20 units close to a segment
            time.sleep(1)
            obj.head.goto(0, 0) #resets the block position to the centre 
            obj.head.direction = "stop"
            obj.delay = 0.075 
            
            # Hide the segments
            for segment in obj.segments:
            #teleports existing blocks to another random space and removes the segment to clear list 
                segment.goto(10000, 10000)

            obj.segments.clear()
            # reset score
            otherobj.score = 0
            # update score and updates the score presented in turtle 
            otherobj.newpen.clear()
            otherobj.newpen.color("red")
            otherobj.newpen.goto(0, 180)
            otherobj.newpen.penup()
            otherobj.newpen.hideturtle()
            otherobj.newpen.write("You died! restarting game...", align="center", font=("Courier", 15, "normal"))
            time.sleep(2)
            otherobj.newpen.clear()
            otherobj.pen.clear()
            otherobj.pen.write("score: {} High Score: {}".format(otherobj.score, otherobj.high_score), align="center", font=("Courier", 22, "normal"))


class Score:
    def __init__(self):
        #score sheet
        self.score = 0
        self.high_score = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 200) #tells it to go to x=0, y=200 coordinate on screen 
        self.pen.write("Score: {} High Score: {}".format(self.score, self.high_score), align="center", font=("Courier", 22, "normal"))

        self.newpen = turtle.Turtle()
        self.newpen.speed(0)
        self.newpen.shape("square")
        self.newpen.color("red")
        self.newpen.penup()
        self.newpen.hideturtle()
        self.newpen.goto(0, 180) #tells it to go to x=0, y=180 coordinate on screen 
        self.newpen.write("The snake is malnourished :(", align="center", font=("Courier", 15, "normal"))
        #quotes to be output when game is played
        with open ("wordlist.txt") as file:
            data = file.readlines()
            file.close()
        self.quotes = []
        for line in data:
            self.quotes.append(line.replace("\\n","\n"))
  

class Food:
    def __init__(self):
        # Snake food
        self.position = turtle.Turtle()
        self.position.speed(0)
        self.position.shape("turtle")
        self.position.color("red")
        self.position.penup()
        self.position.shapesize(1, 1)
        self.position.goto(0, 0)

    def move(self):
        # move the food to a random position on screen
        xfood = random.randint(-200, 200)
        yfood = random.randint(-230, 230)
        self.position.goto(xfood, yfood)


def setup():
    """Set up the window and snake"""
    #set up the screen
    window = turtle.Screen()
    window.title("OMG A SNAKE IN SUTD?")
    window.bgcolor("lightblue")
    window.setup(width=500,height=500)
    window.tracer(0) # turns off the screen updates
    return window

def main_program():
    """Runs the game"""
    #set up the screen
    window = setup()

    #temporary turtle, this will display the opening screen and clear it before the game starts. 
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Welcome to SNEK! Have fun :)", align="center", font=("Courier", 18, "normal"))
    #sets a delay and cleans the pen away
    time.sleep(5)
    pen.clear()

    # Create the objects in the game
    snake = Snake()
    food = Food()
    text = Score()

    # Main game loop
    while True:
        window.update()
        snake.move() #continuously run this function and its effect if head_direction is not "stop"
        text.pen.clear()
        text.pen.write("Score: {} High Score: {}".format(text.score, text.high_score), align="center", font=("Courier", 22, "normal"))
        Snake.check_collision(snake,text)
        time.sleep(snake.delay)
        # keyboard bindings
        window.listen()
        window.onkey(snake.go_up, "w") #demonstration of class-based inheritance; if you're interested lemme know!
        window.onkey(snake.go_down, "s")
        window.onkey(snake.go_right, "d")
        window.onkey(snake.go_left, "a")
      
        if text.score == 0:
            text.newpen.clear()
            snake.delay = 0.075
            text.newpen.color("red")
            text.newpen.goto(0, 180)
            text.newpen.penup()
            text.newpen.hideturtle()
            text.newpen.write("The Snake is malnourished :( ", align="center", font=("Courier", 15, "normal"))
           
           
        if len(snake.segments) == 1: #could be put into a function and called with different strings. But meh, let's lengthen the code alittle bit.
            text.newpen.clear()      #basically, if I have less than 3 segments, the text will be cleared and a new one will be printed. 
            snake.delay = 0.09
            text.newpen.color("white")
            text.newpen.goto(0, 180)
            text.newpen.penup()
            text.newpen.hideturtle()
            text.newpen.write("The snake's feeling much better!", align="center", font=("Courier", 15, "normal"))
    
        if len(snake.segments) == 2:
            text.newpen.clear()
            snake.delay = 0.075
            text.newpen.color("white")
            text.newpen.goto(0, 180)
            text.newpen.penup()
            text.newpen.hideturtle()
            text.newpen.write("Only happy, well-fed snakes can grow :)", align="center", font=("Courier", 15, "normal"))

        if len(snake.segments) == 3:
            text.newpen.clear()
            snake.delay = 0.075
            text.newpen.color("white")
            text.newpen.goto(0, 180)
            text.newpen.penup()
            text.newpen.hideturtle()
            text.newpen.write("Now for some facts about SUTD!", align="center", font=("Courier", 15, "normal"))


        if snake.head.distance(food.position) < 15: # calculate the distance between the two objects 
            food.move()                             # invokes the move() function within food class
            snake.segment_creator()                 # adds a segment into array/list    
            snake.delay-=0.005                      # speeds up the snake 
            text.score = text.score + 10            # adds score 
            if text.score > text.high_score:
                text.high_score = text.score        # updates score 
            if len(snake.segments) > 3:             # if the length of snake is longer than 3:
                text.newpen.clear()
                a = random.randint(0, len(text.quotes)-1)
                if len(text.quotes[a]) > 80:
                    text.newpen.goto(0, 130) #adds spacing for the paragraph to fit
                    text.newpen.write(text.quotes[a], align="center", font=("Courier", 12, "normal"))
                elif len(text.quotes[a]) > 30:
                    #add code to make space for long text later 
                    text.newpen.goto(0, 150) #adds spacing for the paragraph to fit
                    text.newpen.write(text.quotes[a], align="center", font=("Courier", 12, "normal"))
                else:
                    text.newpen.goto(0, 160)
                    text.newpen.write(text.quotes[a], align="center", font=("Courier", 14, "normal"))
            

# move the end segment in reverse order. Reverse order is MUCH better than forward order as this reduces "one-off" errors caused due to appendation of values to the end of the array/list. 
# starting from the back allows the segments to systematically be assigned the coordinates of the segment ahead of it
        if len(snake.segments) > 0:
            for index in range(len(snake.segments)-1, -1, -1):
                if index != 0:
                    x = snake.segments[index-1].xcor()
                    y = snake.segments[index-1].ycor()
                else: 
                    x = snake.head.xcor()
                    y = snake.head.ycor()
                snake.segments[index].goto(x, y)

# Run the programme easily, forces the code to be run directly instead of it being imported. 
if __name__ == '__main__':
    # Add music (only works on windows for now)
    try:
        os.system("start ./music.mp3")
        main_program()
        turtle.mainloop()
        print("hi")
    except:
        main_program()