# python-beginner-projects

My first Python projects, built while learning fundamentals.

## Projects

### guess.py — Number Guessing Game
Guess a randomly generated number between 1-100 within limited attempts.
Learned: while loops, break, try/except for input validation, nested loops for replay logic.

### calculator.py — Calculator
Basic calculator supporting +, −, ×, ÷ with error handling.
Learned: if/elif/else chains, handling divide-by-zero, input validation, catching invalid operations. Later refactored to use functions (add, subtract, multiply, divide).

### unit_converter.py — Unit Converter
Converts between km/miles, kg/lbs, and meters/feet, with a menu of options.
Learned: menu-driven input, rounding output with round(), structuring multiple conversion branches, moving constants outside a loop.

### rock_paper_scissors.py — Rock Paper Scissors
Play rock-paper-scissors against the computer, with score tracking across rounds.
Learned: random.choice() for random selection from a list, nested if/elif for win logic, .lower() for case-insensitive comparison, tracking multiple counters (wins/losses/ties), and writing my own functions (def, parameters, return) instead of one long script.

### contact_book.py — Contact Book
Menu-driven contact manager: add, view, delete, and quit. Contacts stored as dictionaries inside a list.
Now saves contacts to a file and loads them back on startup, so data persists between runs instead of disappearing when the program closes.
Learned: lists of dictionaries, looping with .items(), building dictionaries from user input, searching and removing items from a list, for...else for "not found" handling, and file reading/writing — open(), read/write/append modes, the with statement, and reconstructing dictionaries from saved text using string methods (.strip(), .split()).

## What I'm learning next
Tuples, sets, and the concept of Big-O notation.
