import turtle

def setup():
    #set up the screen
    window = turtle.Screen()
    window.title("OMG A SNAKE IN SUTD?")
    window.bgcolor("lightblue")
    window.setup(width=500,height=500)
    window.tracer(0) # turns off the screen updates

    #Snake Head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 100)
    head.direction = "stop"

if __name__ == '__main__':
    setup()