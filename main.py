from turtle import Screen
from snake import Snake
from food import Food
import time

# STEP_1: Create the Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()

# STEP_2: Move the Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# STEP_3: Control the Snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

# STEP_4: Detect Food Collision

screen.exitonclick()
