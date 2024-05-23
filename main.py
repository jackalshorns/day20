from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

WALL_BOUNDARY = 295

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 30:
        food.refresh()
        snake.extend()
        score.increase()

    #Detect Collisioen w/ Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    #Detect Collision w/ Wall
    if (snake.head.xcor() > WALL_BOUNDARY or snake.head.xcor() < 0 - WALL_BOUNDARY or snake.head.ycor() > WALL_BOUNDARY
            or snake.head.ycor() < 0 - WALL_BOUNDARY):
        score.game_over()
        game_is_on = False

    # #Detect collision w/ Tail
    #
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 5:
    #         snake.extend()

screen.exitonclick()
