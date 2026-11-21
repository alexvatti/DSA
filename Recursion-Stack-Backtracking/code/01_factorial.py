"""
============================================================
 01. FACTORIAL   (Linear recursion (1 branch))
============================================================

PROBLEM
-------
Return n! = 1 × 2 × 3 × … × n  (and 0! = 1).

Examples:
    factorial(4) = 24
    factorial(5) = 120
    factorial(0) = 1


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Multiply 1 × 2 × … × n with a loop. Simple, fast, no extra memory.
 2. RECURSION
      n! = n × (n−1)!. Stop at the base case. Python keeps the pending
      multiplications on its own call stack.
 3. RECURSION + OUR OWN STACK
      Do what Python does, ourselves. Going DOWN: push every pending n.
      At the base case start with 1. Going UP: pop and multiply.
 4. OUR OWN STACK + BACKTRACKING
      One loop. Each stack item is (n, phase). 'go' = dive deeper and
      leave a 'back' note. 'back' = we are returning, do the work
      now. go / back = enter / leave: the template for
      backtracking.


💡 TAKEAWAY
-----------
Recursion is just a stack of pending work. Going DOWN pushes the
pending multiplications, coming UP pops and finishes them.

LEETCODE
--------
(no direct LeetCode problem: it is the warm-up)
also: LC 172 · Factorial Trailing Zeroes -> https://leetcode.com/problems/factorial-trailing-zeroes/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def factorial_recursion(n):
    if n <= 1:                         # base case
        return 1
    return n * factorial_recursion(n - 1)


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def factorial_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 1:                       # going DOWN: push the pending work
        stack.push(n)
        n = n - 1
    result = 1                         # base case
    while not stack.is_empty():        # coming UP: pop and finish the work
        result = result * stack.pop()
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def factorial_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER this level
            if n > 1:
                stack.push((n, "back"))    # remember to come back here
                stack.push((n - 1, "go"))  # dive deeper first
        else:                          # "back": LEAVE this level
            result = result * n
    return result


# ----------------------------------------------------------
# Test cases   (python3 01_factorial.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [factorial_loop, factorial_recursion, factorial_stack, factorial_backtrack]
    tests = [
        ((0,), 1),
        ((1,), 1),
        ((4,), 24),
        ((5,), 120),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
