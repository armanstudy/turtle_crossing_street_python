# 🐢 Turtle Crossing - Learn OOP in Python by Building a Game

Welcome to **Turtle Crossing**, a beginner-friendly game built with Python's built-in `turtle` graphics library. This project is designed as an **educational guide** to teach you how to use:

- Python **classes** and **functions**
- Basic **object-oriented programming (OOP)**
- Real-time game logic with graphics

---

## 🎯 Project Goal

The main goal of this project is to **teach you OOP in Python step-by-step** through a fun game where the player (a turtle) tries to cross a road full of cars.

---

## 🧰 Requirements

- Python 3.7 or later
- No external packages — the `turtle` module is included with Python

---

📚 Full Code Walkthrough with Explanations
🧠 main.py - The Game Controller

'''python
 from turtle import Screen  # Imports the graphics screen from turtle
import time                # Used to pause the game loop
from player import Player  # Imports the Player class from player.py
from car_manager import CarManager  # Imports CarManager class
from scoreboard import Scoreboard   # Imports Scoreboard class



