# 🧭 Recursion · Stack · Backtracking — Base Course

10 basic problems, each solved **4 ways**, so that LeetCode recursion / backtracking problems become easy to start.
Open [`index.html`](index.html) in a browser: every problem has its own page where you **step through the real code line by line** and watch the variables, Python's call stack and **our own stack** change.

---

## 🤔 The idea

Recursion is just **a stack of pending work**. Python keeps that stack for you (the *call stack*). If you can build the same thing with **your own stack**, you can solve any recursion / backtracking problem in a single loop — with no recursion limit.

### The 4 ways (same answer every time)

| # | Way | What happens |
|---|-----|--------------|
| 1 | 🔁 **Loop** | `for` / `while` with variables |
| 2 | 🔂 **Recursion** | the function calls itself; Python's call stack holds the pending work |
| 3 | 📚 **Recursion + our own stack** | going **down** we `push` pending work, coming **up** we `pop` and finish it |
| 4 | 🧭 **Own stack + backtracking** | one loop, items are `(state, "go" / "back")`. `go` = enter / choose, `back` = leave / undo |

### 📦 Our own stack (base code — written ONCE)

File: [`code/stack_base.py`](code/stack_base.py). Whenever a problem uses *our own stack*, **refer back to this file**:

```python
from stack_base import Stack

stack = Stack()
stack.push(x)          # put x on top
x = stack.pop()        # remove and return the top
stack.is_empty()       # True when nothing is inside
```

---

## 🧩 Templates

**Method 3 — recursion with our own stack**
```python
stack = Stack()
while <going DOWN>:            # push every pending piece of work
    stack.push(piece)
result = <base case>
while not stack.is_empty():    # coming UP: pop and finish the work
    result = combine(result, stack.pop())
```

**Method 4 — own stack + backtracking (the LeetCode template)**
```python
stack = Stack()
stack.push((start, "go"))
while not stack.is_empty():
    state, phase = stack.pop()
    if phase == "go":                      # ENTER  (choose)
        if <base case>:
            <record the answer>
        else:
            stack.push((state, "back"))    # UNDO / combine later
            for child in <children>:       # push so the first child comes out first
                stack.push((child, "go"))
    else:                                  # "back": LEAVE (undo / combine)
        <undo the choice or combine the answers>
```

| Recursion says… | Our own stack says… |
|---|---|
| call a function | `stack.push(state)` |
| base case reached | record the answer |
| the call returns | `stack.pop()` (the `"back"` frame) |
| undo after the recursive call | the work in the `"back"` phase |
| RecursionError (depth ≈ 1000) | no limit |

---

## 🗺️ The 10 problems

| # | Problem | Pattern | LeetCode | Page | Notes | Code |
|---|---------|---------|----------|------|-------|------|
| 01 | Factorial | linear recursion | warm-up (LC 172 related) | [page](pages/01_factorial.html) | [md](notes/01_factorial.md) | [py](code/01_factorial.py) |
| 02 | Fibonacci | tree recursion | LC 509 | [page](pages/02_fibonacci.html) | [md](notes/02_fibonacci.md) | [py](code/02_fibonacci.py) |
| 03 | Sum of Digits | linear recursion | LC 1281 / 258 related | [page](pages/03_sum_of_digits.html) | [md](notes/03_sum_of_digits.md) | [py](code/03_sum_of_digits.py) |
| 04 | Reverse a Number | linear recursion | LC 7 | [page](pages/04_reverse_number.html) | [md](notes/04_reverse_number.md) | [py](code/04_reverse_number.py) |
| 05 | Palindrome Number | two-ended check | LC 9 (LC 125 related) | [page](pages/05_palindrome_number.html) | [md](notes/05_palindrome_number.md) | [py](code/05_palindrome_number.py) |
| 06 | Power x ^ n | linear recursion | LC 50 | [page](pages/06_power.html) | [md](notes/06_power.md) | [py](code/06_power.py) |
| 07 | Reverse a String | linear recursion | LC 344 | [page](pages/07_reverse_string.html) | [md](notes/07_reverse_string.md) | [py](code/07_reverse_string.py) |
| 08 | Numbers 1 to N | work before vs after the call | warm-up | [page](pages/08_numbers_1_to_n.html) | [md](notes/08_numbers_1_to_n.md) | [py](code/08_numbers_1_to_n.py) |
| 09 | Binary Strings of length n | backtracking: choose / explore / undo | LC 17, 22 related | [page](pages/09_binary_strings.html) | [md](notes/09_binary_strings.md) | [py](code/09_binary_strings.py) |
| 10 | Subsets | backtracking | **LC 78** | [page](pages/10_subsets.html) | [md](notes/10_subsets.md) | [py](code/10_subsets.py) |

---

## 🚀 Then jump to LeetCode

Order: **509 Fibonacci → 70 Climbing Stairs → 344 Reverse String → 7 Reverse Integer → 9 Palindrome Number → 50 Pow(x, n) → 78 Subsets → 46 Permutations → 17 Letter Combinations → 22 Generate Parentheses → 39 Combination Sum**.
For each: write method 2 (recursion) first, then convert it to method 4 with the template above.

---

## ⚠️ Common mistakes

- Forgetting the **base case** (infinite recursion / an empty-stack loop that never ends).
- Pushing the children in the wrong order: the stack is LIFO, so the child you push **last** is explored **first**.
- Forgetting the `"back"` frame, so the **undo** (`path.pop()`) never happens in backtracking.
- Using one shared `path` list but saving it without copying: save `path[:]`, not `path`.
- Calling `pop()` on an empty stack: always test `not stack.is_empty()` first.

---

## ▶️ How to run

```bash
cd code
python3 stack_base.py            # try our stack
python3 01_factorial.py          # all 4 methods + tests
```

Each `.py` file runs all four methods on the same tests and checks that they agree. The web pages replay real runs of exactly this code.
