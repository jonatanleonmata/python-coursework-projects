# Restaurant Ordering Program

Academic project from CSE 1321L, Kennesaw State University, Fall 2026. Original file: `Assignment4.py`.

A Python program that takes a restaurant order through text menus and calculates the subtotal, tip, tax, and total.

## Features

- Separate menus for burgers, sides, and drinks.
- Multiple items can be added before checkout.
- Preset percentage tips, a custom tip, or no tip.
- A fixed 6% tax calculation and money formatted to two decimal places.
- Functions separate menu input, ordering, and calculations.

## Python concepts

Functions, parameters and return values, loops, conditional statements, numeric input, and formatted output.

## Run

From this folder, run:

```sh
python3 Assignment4.py
```

Uses Python 3 and its built-in features. No extra packages are required.

## Example

[Recorded example run](example-output.txt): a single burger, fries, a small drink, and a 20% tip produce a $11.97 subtotal and a $15.08 total.

## Current scope

This is a terminal-based academic exercise. Numeric menu choices outside the allowed range and negative custom tips are retried. Text entered at a numeric prompt raises an error. Orders last for the current run. The tax rate and prices are fixed exercise values.
