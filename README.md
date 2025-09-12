# Sudoku Solver (Python)

A tiny, dependency‑free Sudoku solver written in pure Python. It checks whether a given 9×9 puzzle is solvable and, if so, fills the grid using recursive backtracking.

> **Input convention**: empty cells are represented by the `'#'` character (not `0`).

---

## ✨ Features

* ✅ Determines if a puzzle is solvable
* 🧠 Produces a fully solved grid when solvable
* 🧩 Standard Sudoku rules (rows, columns, 3×3 boxes)
* 🧪 Minimal, readable code—great for learning backtracking
* 📦 No third‑party dependencies

---

## 🧰 How it works

This solver uses classic **depth‑first search with backtracking**:

1. **Find an empty cell** (`find_next_empty_cell`).
2. **Try digits 1–9** and check validity (`is_valid_number`) against:

   * the row
   * the column
   * the 3×3 sub‑grid
3. **Recurse** to continue with the next empty cell. If a guess leads to a dead end, **backtrack** and try the next digit.

### Core functions

```python
find_next_empty_cell(puzzle) -> tuple[int|None, int|None]
# Returns the (row, col) of the next empty cell, or (None, None) if full.

is_valid_number(puzzle, guess, row, col) -> bool
# Checks if `guess` can be placed at (row, col) under Sudoku constraints.

solve_sudoku(puzzle) -> bool
# Mutates the puzzle in-place. Returns True if solved, else False.
```

---

## 🚀 Quick start

### Requirements

* Python **3.8+** (any modern Python should work)

### Run

```bash
python sudoku_solver.py
```

> Replace `sudoku_solver.py` with your file name if different.

---

## 📝 Usage (with example)

The script expects a **list of lists** with `'#'` for empties.

```python
puzzle = [
    [3, 9, '#', '#', 5, '#', '#', '#', '#'],
    ['#', '#', '#', 2, '#', '#', '#', '#', 5],
    ['#', '#', '#', 7, 1, 9, '#', 8, '#'],
    ['#', 5, '#', '#', 6, 8, '#', '#', '#'],
    [2, '#', 6, '#', '#', 3, '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 4],
    [5, '#', '#', '#', '#', '#', '#', '#', '#'],
    [6, 7, '#', 1, '#', 5, '#', 4, '#'],
    [1, '#', 9, '#', '#', '#', 2, '#', '#'],
]

if solve_sudoku(puzzle):
    print("Solved!\n")
    for row in puzzle:
        print(row)
else:
    print("No solution exists.")
```

### Example output

```
Solved!
[3, 9, 8, 4, 5, 2, 1, 6, 7]
[7, 1, 4, 2, 8, 6, 9, 3, 5]
[5, 6, 2, 7, 1, 9, 4, 8, 3]
[9, 5, 1, 3, 6, 8, 7, 2, 0]
...
```

> Your output may differ depending on the starting grid. The solver mutates the `puzzle` in place.

> **Note**: The above is illustrative; run the script to see the full solved grid.

---

## 📦 Project layout

```
.
├─ sudoku_solver.py        # Contains find_next_empty_cell, is_valid_number, solve_sudoku
├─ README.md               # You are here
└─ (optional) tests/
```

---

## 🧪 Testing (optional)

You can quickly sanity‑check with Python’s REPL:

```python
from sudoku_solver import solve_sudoku
p = [["#"]*9 for _ in range(9)]
print(solve_sudoku(p))  # True — empty grid has solutions
```

For repeatable verification, consider adding `pytest` tests that assert:

* valid solutions return `True`
* unsatisfiable grids return `False`
* the solver respects given clues (doesn’t overwrite non‑empty cells)

---

## ⚙️ Complexity & notes

* **Time**: Exponential in the worst case (backtracking), but fast for typical puzzles due to constraint pruning.
* **Space**: O(1) extra (in‑place), plus recursion depth up to the number of empty cells.
* **Determinism**: Tries digits **1 → 9** in order; different orders can change performance.

### Limitations

* Assumes a valid 9×9 Sudoku shape and clue set (no explicit input validation).
* If a puzzle has **multiple solutions**, it will return the **first** one found.
* Uses `'#'` for empty cells—change to `0` or `None` if preferred (update checks accordingly).

---

## 🛠️ Extending the solver (ideas)

* Add **input parsing** from text/CSV/JSON files
* Add a **pretty printer** for the board
* Implement **MRV/forward checking** heuristics for speed
* Turn it into a **CLI** (e.g., `python sudoku_solver.py --file puzzle.txt`)
* Provide a **web UI** (Flask/FastAPI + simple frontend)

---

## 🔗 API reference (mini)

```python
def solve_sudoku(puzzle: list[list[int|str]]) -> bool:
    """Solve puzzle in-place using backtracking.

    Args:
        puzzle: 9×9 grid; digits 1–9 or '#' for empty.
    Returns:
        True if solved (and puzzle is mutated with a solution), else False.
    """
```

---

## 🧑‍💻 Contributing

Issues and PRs are welcome! If you’d like to contribute, consider adding tests, input parsers, or speed‑ups. Please keep code readable and well‑commented.

---


## 🙌 Acknowledgments

Built with ❤️ using classic backtracking. Perfect for learning recursion and constraint checking.
