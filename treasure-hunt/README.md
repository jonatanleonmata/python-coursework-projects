# Treasure Hunt Game

Academic project from CSE 1321L, Kennesaw State University, Fall 2026. Original file: `Assignment5B.py`.

A Python game that creates a random grid of treasures, traps, and empty locations. A player selects coordinates to collect all the treasures.

## Features

- User-selected map dimensions and random cell contents.
- A two-dimensional list stores and updates the map.
- Treasures add points and traps subtract points.
- Consecutive treasure finds receive a scoring bonus.
- Visited locations are tracked to prevent scoring them twice.
- Final statistics report the score, traps, and locations explored.

## Python concepts

Nested lists, nested loops, tuples, conditional statements, functions, random number generation, and tracking state during a game.

## Run

From this folder, run:

```sh
python3 Assignment5B.py
```

Uses Python 3 and the standard-library `random` module. No extra packages are required.

## Example

[Recorded example run](example-output.txt): a 3 by 3 map is completed with a final score of 50. The example includes a trap, a repeated selection, an empty location, and consecutive treasure finds. A seed was set by the verification runner to make this example repeatable; ordinary runs generate a new map.

## Current scope

The complete map is visible to the player. Input assumes positive integer map dimensions and valid, nonnegative coordinates within the map. Out-of-range coordinates raise an error; negative coordinates follow Python's list-indexing behavior. Input validation and a hidden map would be useful future improvements.
