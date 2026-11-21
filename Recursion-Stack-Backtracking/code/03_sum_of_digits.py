"""
============================================================
 03. SUM OF DIGITS   (Linear recursion (1 branch))
============================================================

PROBLEM
-------
Return the sum of the digits of a non-negative integer n.

Examples:
    sum_digits(123) = 6
    sum_digits(4506) = 15
    sum_digits(0) = 0


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      n % 10 is the last digit, n // 10 removes it. Repeat until n is 0,
      adding each digit.
 2. RECURSION
      sum(n) = last digit + sum(n // 10). Base case: n == 0 gives 0.
 3. RECURSION + OUR OWN STACK
      DOWN: push each digit while chopping n. UP: pop the digits and add
      them.
 4. OUR OWN STACK + BACKTRACKING
      (n, phase) frames. 'go' dives to n // 10 and leaves a 'back'. On
      'back', add this level's digit n % 10.


💡 TAKEAWAY
-----------
Same shape as factorial. Only the work changes (add instead of
multiply). n % 10 = last digit, n // 10 = the rest.

LEETCODE
--------
LC 1281 · Subtract the Product and Sum of Digits -> https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
also: LC 258 · Add Digits -> https://leetcode.com/problems/add-digits/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def sum_digits_loop(n):
    total = 0
    while n > 0:
        total = total + n % 10         # add the last digit
        n = n // 10                    # drop the last digit
    return total


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def sum_digits_recursion(n):
    if n == 0:                         # base case: no digits left
        return 0
    return n % 10 + sum_digits_recursion(n // 10)


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def sum_digits_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push every digit
        stack.push(n % 10)
        n = n // 10
    total = 0
    while not stack.is_empty():        # coming UP: pop and add
        total = total + stack.pop()
    return total


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def sum_digits_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    total = 0
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n // 10, "go"))
        else:                          # "back": LEAVE -> do the work
            total = total + n % 10
    return total


# ----------------------------------------------------------
# Test cases   (python3 03_sum_of_digits.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [sum_digits_loop, sum_digits_recursion, sum_digits_stack, sum_digits_backtrack]
    tests = [
        ((0,), 0),
        ((7,), 7),
        ((123,), 6),
        ((4506,), 15),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
