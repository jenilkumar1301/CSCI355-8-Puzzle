
# CSCI 355 - 8 Puzzle Solver

This is our 8-puzzle project for CSCI 355. We are using the A* algorithm to solve the puzzle and find the shortest path to the goal state.

## Group Members

- Jenil - Backend, A* solver and testing
- Jerry - Report
- Jashkiran - HTML and CSS
- Sid - JavaScript and animation

## Project Files

- app.py - Flask application
- solver.py - A* algorithm
- test_solver.py - Tests for the solver
- templates/index.html - Webpage
- static/style.css - CSS
- static/script.js - Puzzle animation

## Running the Project

First install Flask:

    pip install -r requirements.txt

Then run:

    python3 app.py

Open http://127.0.0.1:5000 in your browser.

## How It Works

The puzzle has 8 numbered tiles and one empty space. We use 0 for the empty space.

Our solver uses A* search with Manhattan distance to find the solution.

The goal is:

    1 2 3
    4 5 6
    7 8 0

The webpage will have two buttons:
- Randomize - Shuffles the puzzle
- Solve - Shows the moves to solve it

## Testing

To test the solver, run:

    python3 -m unittest test_solver.py

We have 6 basic tests for the solver, including solved, one-move, two-move and unsolvable boards.

## Current Progress



## Current Progress

The backend, A* solver, HTML, CSS and JavaScript are completed.

All 6 solver tests passed.

We tested the project in the browser. Both Randomize and Solve buttons are working, and the puzzle shows the solution step by step.

We are now working on the report and video demonstration.
