from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    """Displays the current level and game over message."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard with the current level."""
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        """Increases the level and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays the game over message in the center of the screen."""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
