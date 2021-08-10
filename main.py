from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# STEP_1: Create the Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

# STEP_2: Move the Snake
# STEP_3: Control the Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# STEP_4: Detect Food Collision
# STEP_5: Create a scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# STEP_6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        snake.reset()
        scoreboard.game_over()

# STEP_7: Detect collision with tail
# if head collide with any segment in the tail, trigger game over
    for segment in snake.segments[1:]:  # Using python slicing
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            snake.reset()

screen.exitonclick()
