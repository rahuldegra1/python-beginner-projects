# Python Beginner Projects

My first Python projects, built while learning programming fundamentals and building a strong foundation in computer science. Started August 2026, as part of a self-directed roadmap toward becoming an AI/ML engineer, alongside an Online BCA at Manipal University Jaipur.

Each project below follows the same reflection format: **what it does, why I built it, what I'd do differently.**

---

## 🚀 Projects

### Tic-Tac-Toe
**What it does:** A command-line two-player game. Maps a 3x3 grid to a single flat list (index 0-8), prints the board after every move, and checks all 8 win combinations (3 rows, 3 columns, 2 diagonals) after each turn.

**Why I built it:** To practice mapping 2D coordinates onto a 1D data structure, and to work with nested win-condition logic.

**What I'd do differently:** I originally had the draw-check run *before* the win-check, which meant a winning final move on the last empty square got misreported as a draw — Python hit the draw condition and broke out of the loop before ever calling `check_win()`. Fixed it by reordering the checks so a win is always tested first. Next time, I'd refactor the board into a `Board` class from the start instead of a plain list, and add a replay loop like my other games have.

---

### Dynamic Quiz App
**What it does:** A command-line trivia game that reads questions, four options, and the correct answer from an external `questions.csv` file using `csv.DictReader`, then tracks and reports a final score.

**Why I built it:** To practice reading structured external data instead of hardcoding everything into the script.

**What I'd do differently:** Shuffle the question order and the answer options on each run so the quiz isn't identical every time. Also add input validation so a typo doesn't silently count as a wrong answer.

---

### Contact Book
**What it does:** Stores contacts (name, phone, email) as dictionaries in a list, with add, view, and delete options. Persists data to a text file (`contact.txt`) so contacts survive between runs.

**Why I built it:** To practice file persistence and using a `for...else` loop for the delete-by-name search.

**What I'd do differently:** Switch from manually parsing comma-separated lines to using Python's `json` module for storage — it would be far more robust than string-splitting, especially once names or emails contain commas. I'd also add an "edit contact" option.

---

### Number Guessing Game
**What it does:** The computer picks a random number between 1 and 100; the player has 7 attempts to guess it, with "too high / too low" hints after each try.

**Why I built it:** To practice `while` loops, attempt counting, and handling invalid (non-numeric) input without crashing.

**What I'd do differently:** Track and display the player's best (fewest-attempts) score across rounds, and let the player choose a difficulty level that changes the number range and attempt limit.

---

### Rock, Paper, Scissors
**What it does:** Plays rounds of rock-paper-scissors against the computer using Python's `random` module, tracking wins, losses, and ties across the session.

**Why I built it:** To practice conditional logic across three possible player choices and three possible outcomes.

**What I'd do differently:** Replace the long `if/elif` chain with a lookup dictionary (e.g., mapping each choice to what it beats) — it would cut the logic down significantly and make it easier to extend to variants like rock-paper-scissors-lizard-spock.

---

### Unit Converter
**What it does:** Converts between km/miles, kg/lbs, and meters/feet based on a menu choice, using fixed conversion constants.

**Why I built it:** To practice building a simple menu-driven program with multiple independent operations.

**What I'd do differently:** Store the conversions in a dictionary keyed by choice, and split each conversion into its own small function, instead of one long `if/elif` block.

---

### Calculator
**What it does:** Performs addition, subtraction, multiplication, and division on two user-entered numbers in a loop, with error handling for invalid (non-numeric) input and division by zero.

**Why I built it:** My first real project — to practice `try/except` for input validation and basic control flow.

**What I'd do differently:** Add a visible prompt for the operator (right now it's a bare `input()` with no text), support for more operations (like exponents), and split the arithmetic into separate functions.

---

## 🧠 Core Skills Demonstrated

*   **File Handling (I/O):** Reading and writing external data using Python's `csv` module and plain text files.
*   **Data Structures:** Lists, nested dictionaries, and 1D-to-2D grid mapping.
*   **Control Flow:** Game loops built with `for` loops, `while` loops, `if/elif/else`, and a `for...else` search pattern.
*   **Input Validation:** `try/except` blocks to catch invalid input across every project rather than letting the program crash.
*   **Debugging:** Found and fixed a real logic bug in Tic-Tac-Toe (draw-check running before win-check), by tracing execution order and constructing a specific test case to confirm the fix.
*   **Version Control:** Managing a multi-file project via Git and GitHub.

## 🔜 Coming Next

*   **Object-Oriented Programming:** A bank account simulation and a to-do list manager, moving from function-based scripts to classes.
*   **Binary Search:** Implementing it from scratch and reasoning about why it runs in O(log n).
