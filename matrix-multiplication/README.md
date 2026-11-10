# Matrix Multiplication Tool

Academic project from CSE 1321L, Kennesaw State University, Fall 2026. Original file: `Assignment5C.py`.

A Python program that multiplies two compatible matrices using nested lists and loops.

## Features

- Accepts the number of rows and columns for each matrix.
- Checks that Matrix A's column count equals Matrix B's row count.
- Reads comma-separated integer values in row order.
- Uses nested loops to calculate each entry of the product.
- Prints both input matrices and the result.

## Python concepts

Two-dimensional lists, nested loops, integer conversion, functions, and implementing a mathematical algorithm.

## Run

From this folder, run:

```sh
python3 Assignment5C.py
```

Uses Python 3 and its built-in features. No extra packages are required.

## Example

[Recorded example run](example-output.txt): a 2 by 3 matrix multiplied by a 3 by 2 matrix produces:

```text
58  64
139 154
```

Enter positive dimensions and exactly rows-times-columns integer values for each matrix. For example, a 2 by 3 matrix needs six values.

## Current scope

The program checks dimension compatibility. It assumes positive dimensions, integer values, and the correct number of values. Too few values raise an error, and extra values are ignored. Stronger input validation would be a useful future improvement. This is an academic matrix algorithm exercise.
