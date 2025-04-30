from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """Manages the player turtle (user-controlled character)."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """Moves the player turtle upward by MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Resets the player's position to the starting point."""
        self.goto(STARTING_POSITION)

    def reset_position(self):
        """Resets the player when they reach the finish line."""
        self.go_to_start()
