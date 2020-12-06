# Team 4 - Snake in SUTD?!
Members: Yong Kang Chia, Kushagra Jain, Liu Nanhan, Chong Shuting, Lawrence Kevin Sagaya Anthony

# Description 
This game is a adapted version of the snake game. The description can be found here:

https://en.wikipedia.org/wiki/Snake_(video_game_genre)


# Documentation
It is required for this game to use the random,turtle and time library. 

The game is coded based on Object Oriented Paradigm (OOP) and it contains the following objects:
1. Snake Object
2. Food Object
3. Score Object



## 1. Snake Object


```Class Snake: 
__init__(self). Formation of the ‘SNEK’ including its shape, colour and size,speed. Making the default position (0,100), the centre of the play area.
move(self). Sets the motion of the turtle object.
go_up(self). go_down(self). go_right(self). go_left(self). Restricts the movement of the ‘SNEK’ so it is not able to move in the opposite direction it is currently in.
segment_creator(self).: This allows the ‘SNEK’ to grow in length by 1 box when it consumes a fruit. 
	check_collision(obj,otherobj): This checks for any collision occurring (boundary and snake itself). It is a function within a class which allows it to be called with multiple methods being used.
```
## 2. Food Object
```Class Score: The score will be located at top of the screen, at (0, 200).```
## 3. Score Object
```
Class Food:
	__init__(self). Formation of the Snake food including the shape, colour and size. The shape of the food is turtle and its color is red.
	move(self). The food will move to a random position on screen. The x is from -200 to 200, the y is from -230 to 230, based on the size of the screen.
setup(). Set up the screen, window and snake.
```
## 3. Main Program
This is the function that runs the game. The speed of the snake and the text displayed will be dependent on the length of the snake
```
main_program(). 
```
