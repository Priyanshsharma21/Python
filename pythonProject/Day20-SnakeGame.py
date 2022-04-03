from turtle import  Screen
from snake import Snake
from food import Food
from scorboard import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
# score.showScore()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    if snake.head.distance(food) < 50:
        food.refresh()
        score.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over()
        game_is_on = False

    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment)< 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

# slice function
# List = [1,2,3,4,5,6]
# List.slice[1,4] // 4 not included
# List.slice[1,4,2] //increament
# List.slice[::-1] // Use to reverse