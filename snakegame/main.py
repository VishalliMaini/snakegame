from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen=Screen()

screen.setup(width=600,height=600)
screen.title("My snake game")
screen.bgcolor("black")
#alag alag turtles naa dekhe move karte puri as single unit move kare
screen.tracer(0)
is_game = True
snake = Snake()
food = Food()
scoreboard=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #check for collision
    if snake.head.distance(food)<15:
        food.refresh()
        #increasing snakes body
        snake.extend()
        scoreboard.increment_score()
    #wall collision
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300 :
        is_game=False
        scoreboard.gameover()
    for segment in snake.segments:
       if segment==snake.head:
           pass
       elif snake.head.distance(segment)<10:
           is_game = False
           scoreboard.gameover()


screen.exitonclick()