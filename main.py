from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Slithering Snake - A Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.increase_score(food.check_distance(predator=snake, prey=food))
    scoreboard.display_score()
    if snake.hit_wall() or snake.detect_collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
