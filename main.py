from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extent_snake()
        scoreboard.increase_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        game = False
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            game = False
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
