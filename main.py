from turtle import Turtle, Screen
from snake import  Snake
import time
from food import Food
from score import  Score
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600 , width=600)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
food = Food()
score = Score()

while game_on:
    snake.move()
    screen.update()
    time.sleep(0.09)
    #eat food done
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_edit()
    #collide with walls
    if snake.snake_body[0].xcor() > 280 or  snake.snake_body[0].xcor() < -280 or  snake.snake_body[0].ycor() > 280 or  snake.snake_body[0].ycor() < -280:
        game_on = False
        score.end_game()
    #hit tail
    for part in snake.snake_body[1:]:
        if snake.snake_body[0].distance(part) < 10:
            game_on = False
            score.end_game()



screen.exitonclick()