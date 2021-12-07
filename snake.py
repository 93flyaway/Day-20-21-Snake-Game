from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for starting_position in STARTING_POSITIONS:
            self.create_segment(starting_position)

    def create_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def extend_segment(self):
        new_position = self.snake_body[-1].pos()
        self.create_segment(new_position)

    def move(self):
        for snake_index in range(-1, -len(self.snake_body), -1):
            target_position = self.snake_body[snake_index - 1].pos()
            self.snake_body[snake_index].goto(target_position)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.towards(self.snake_body[1]) != UP:
            self.head.setheading(UP)

    def right(self):
        if self.head.towards(self.snake_body[1]) != RIGHT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.towards(self.snake_body[1]) != LEFT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.towards(self.snake_body[1]) != DOWN:
            self.head.setheading(DOWN)

    def is_looped(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
