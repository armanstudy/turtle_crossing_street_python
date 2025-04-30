from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Instantiate objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Key binding
screen.onkey(player.move_up, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False  

    # Check if player reaches the finish line              
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
