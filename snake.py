from turtle import Turtle

snake_positions = positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_POS = 20


class Snake:
    def __init__(self):

        self.snake_body = []
        self.start_game()

    def start_game(self):
        for pos in snake_positions:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.snake_body.append(snake)

    def extend(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snake_body[-1].position())
        self.snake_body.append(snake)

    def move(self):

        for part in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[part - 1].pos()
            self.snake_body[part].goto(self.snake_body[part - 1].pos())

        self.snake_body[0].forward(MOVE_POS)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
