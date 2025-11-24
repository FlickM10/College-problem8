# 🎲 High-Tie-Low Dice Game

A simple command-line game implemented in **Python 3** that tests the user's prediction skills against a random dice roll. The core logic hinges on a comparison against a fixed, initial reference roll.

---

## 💻 Technical Details

### Architecture and Design

The game follows a **sequential, procedural** structure. It operates in two main phases: **Setup** and **Game Loop**, followed by **Result Calculation**.

* **Language:** Python 3.x
* **Dependencies:** None (uses only the standard built-in `random` module).

### Code Breakdown

The following details explain the key components and logic flow of the `high_tie_low.py` script:

#### 1. Initialization and Setup

The script begins by importing the necessary module and gathering initial parameters from the user.

| Variable | Type | Purpose |
| :---: | :---: | :--- |
| `N` | `int` | Stores the **total number of rounds** the user wishes to play, parsed from command-line input. |
| `Initial_roll` | `int` | The **fixed reference value** (1-6) generated using `random.randint(1, 6)`. All subsequent predictions are based on this value. |
| `Wins` | `int` | A counter initialized to `0` to track the user's successful predictions. |

#### 2. The Game Loop

The game uses a **`for` loop** that iterates `N` times, handling one round of the game in each iteration.

* **User Input:** Inside the loop, `input()` is used to capture the user's prediction (`Pred`), which is expected to be one of the strings: `"High"`, `"Tie"`, or `"Low"`.
* **Dice Roll:** A new random integer `Roll` (1-6) is generated for the current round.

      Roll = random.randint(1, 6)

#### 3. Prediction Logic

The core comparison and logic are handled using a series of **`if-elif-else`** blocks that determine the true outcome (`Pred_real`) by comparing `Roll` to the fixed `Initial_roll`.

| Condition | `Pred_real` Value |
| :--- | :--- |
| `Roll > Initial_roll` | `'High'` |
| `Roll == Initial_roll` | `'Tie'` |
| `Roll < Initial_roll` | `'Low'` |

A final conditional check compares the user's input (`Pred`) directly against the determined `Pred_real`. If they match, the `Wins` counter is incremented.

#### 4. Final Output and Calculation

After the loop completes, the script calculates and prints the final statistics.

* **Win Percentage Calculation:**
    The final win rate is calculated using floating-point arithmetic to ensure accuracy:
   <img width="437" height="90" alt="image" src="https://github.com/user-attachments/assets/d32d4e81-a50a-47ff-9435-e889c046d497" />


---

## 🛠️ Potential Improvements

* **Input Validation:** Add error handling (e.g., using a `try-except` block or a validation loop) to ensure `N` is a positive integer and `Pred` is one of the allowed strings (`"High"`, `"Tie"`, `"Low"`).
* **Case Insensitivity:** Implement a `.lower()` or `.upper()` transformation on the user's prediction (`Pred`) to make the game more robust to user input (e.g., accepting `"high"` or `"HIGH"`).
* **Variable Scoping:** While simple, ensure all variables are appropriately scoped for future expansion.

---
