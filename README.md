# python-beginner-projects

My first Python projects, built while learning programming fundamentals and building a strong foundation in CS. 

---

## 🛠️ Projects

### 1. guess.py — Number Guessing Game
* **What this does:** A game where the user guesses a randomly generated number between 1-100 within a limited number of attempts.
* **Why I built it:** To learn `while` loops, the `break` statement, `try/except` for input validation, and nested loops for replay logic.
* **What I'd do differently:** Next time, I would add a difficulty selector at the beginning to let the user choose the range of numbers (e.g., 1-50 vs 1-500).

### 2. calculator.py — Calculator
* **What this does:** A basic calculator supporting addition, subtraction, multiplication, and division with error handling.
* **Why I built it:** To practice `if/elif/else` chains, handling divide-by-zero errors, catching invalid operations, and refactoring a long script into reusable custom functions.
* **What I'd do differently:** I'd restructure the main loop to allow the user to chain calculations together (e.g., taking the previous answer and adding to it) instead of starting fresh every time.

### 3. unit_converter.py — Unit Converter
* **What this does:** Converts values between km/miles, kg/lbs, and meters/feet using a menu-driven interface.
* **Why I built it:** To learn how to build menu-driven user inputs, round outputs using `round()`, structure multiple conversion branches, and keep constants outside of loops.
* **What I'd do differently:** I would try storing the conversion rates in a dictionary to make the code shorter and avoid long `if/elif` chains.

### 4. rock_paper_scissors.py — Rock Paper Scissors
* **What this does:** A game against the computer with score tracking (wins/losses/ties) across multiple rounds.
* **Why I built it:** To understand `random.choice()` for list selection, nested `if/elif` for game logic, case-insensitive string comparison (`.lower()`), and passing parameters/return values in functions.
* **What I'd do differently:** I'd add a "Best out of 3" or "Best out of 5" tournament mode instead of just an infinite loop.

### 5. contact_book.py — Contact Book
* **What this does:** A menu-driven contact manager (add, view, delete, quit) that saves contacts to a text file so data persists between sessions.
* **Why I built it:** To master dictionaries inside lists, looping with `.items()`, `for...else` logic, and file I/O operations (`open()`, `read/write/append`, the `with` statement, and string methods like `.strip()` and `.split()`).
* **What I'd do differently:** Now that I know how complex manual string splitting can get, I would use Python's built-in `json` module to save and load the dictionary data more cleanly.

### 6. quiz_app.py — Interactive Quiz
* **What this does:** A multiple-choice quiz that takes user input, evaluates the answers, tracks the score, and outputs a final result.
* **Why I built it:** To practice iterating through nested data structures (lists of dictionaries), using `.lower()` for robust input validation, and formatting dynamic output with f-strings.
* **What I'd do differently:** Currently, the questions are hardcoded into the script. Next time, I will use Python file handling to read the questions dynamically from an external `.txt` or `.json` file.

---

## 🚀 What I'm Learning Next
* Tuples and Sets
* The concept of Big-O notation
