"""
============================================================
 06. POWER  X ^ N   (Linear recursion (1 branch))
============================================================

PROBLEM
-------
Return x raised to the power n (n ≥ 0). Here x^n = x × x × … (n times).  LC 50 also needs the halving trick: x^n = (x^(n/2))².

Examples:
    power(2, 3) = 8
    power(3, 4) = 81
    power(5, 0) = 1


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Multiply x into the result n times.
 2. RECURSION
      x^n = x × x^(n−1). Base case: x^0 = 1.
 3. RECURSION + OUR OWN STACK
      DOWN: push one x for every pending multiplication. UP: pop and
      multiply into the result.
 4. OUR OWN STACK + BACKTRACKING
      (n, phase) frames. Each 'back' multiplies the result by x.


💡 TAKEAWAY
-----------
The count n drives the depth. Once this is easy, the halving trick (n
// 2) is a one-line change for LC 50.

LEETCODE
--------
LC 50 · Pow(x, n) -> https://leetcode.com/problems/powx-n/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def power_loop(x, n):
    result = 1
    for _ in range(n):
        result = result * x
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def power_recursion(x, n):
    if n == 0:                         # base case
        return 1
    return x * power_recursion(x, n - 1)


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def power_stack(x, n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: one pending multiply per step
        stack.push(x)
        n = n - 1
    result = 1                         # base case
    while not stack.is_empty():        # coming UP
        result = result * stack.pop()
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def power_backtrack(x, n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n - 1, "go"))
        else:                          # "back": LEAVE -> do the work
            result = result * x
    return result


# ----------------------------------------------------------
# Test cases   (python3 06_power.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [power_loop, power_recursion, power_stack, power_backtrack]
    tests = [
        ((2, 0), 1),
        ((2, 3), 8),
        ((3, 4), 81),
        ((5, 1), 5),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
