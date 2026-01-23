# Orange Circle — Reaction & Precision Game

Orange Circle is a fast‑paced arcade-style game built in Python using Pygame. The goal is simple: test the player’s reaction time and precision by requiring quick, accurate responses under increasing pressure.

This project was built as a complete, self-contained game loop to demonstrate interactive programming, real-time event handling, and game-state management.

---

## Overview

In Orange Circle, the player interacts with a dynamic on-screen target. As the game progresses, timing windows and difficulty increase, forcing the player to react faster and more precisely. The game ends when the player fails to meet the required accuracy or timing constraints.

The project emphasizes:

- Real-time input handling
- Frame-based game loops
- State transitions between gameplay phases
- Clean separation of game logic and execution flow

---

## Core Features

- **Real-Time Gameplay**  
  Continuous frame updates and event polling using Pygame’s main loop.

- **Reaction & Precision Mechanics**  
  Player performance is evaluated based on timing and positional accuracy.

- **Clear Game Loop Structure**  
  Distinct start, run, and end phases ensure predictable and maintainable control flow.

- **Minimal Setup**  
  Designed to run immediately after cloning, with no external services or configuration required.

- **Resizable Window Support**  
  The game window can be resized at runtime, with rendering and gameplay adapting dynamically to the new window dimensions.

---

## Tech Stack

- Python
- Pygame
- JSON (for lightweight data persistence)

---

## Running the Game

To run the game locally:

```bash
git clone https://github.com/your-username/OrangeCircle
cd OrangeCircle
pip install pygame
python main.py
```

---

## What This Project Demonstrates

- Ability to design and implement a complete interactive application
- Understanding of real-time systems and event-driven programming
- Experience managing game state and user input
- Clean, readable Python code suitable for extension or refactoring

---

## Future Improvements

- Difficulty scaling based on player performance
- Score history tracking
- Visual effects and animation polish

---
