from turtle import Turtle, Screen

screen = Screen()
AXIS_POSITIONS = [(-20, 0),(0, 0) , (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for pos in AXIS_POSITIONS:
            self.add_segment(pos)


    def add_segment(self,position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_segments.append(new_snake)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            newX = self.all_segments[seg_num - 1].xcor()
            newY = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(newX, newY)
            self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

