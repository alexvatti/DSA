"""
============================================================
 04. REVERSE A NUMBER   (Linear recursion (1 branch))
============================================================

PROBLEM
-------
Reverse the digits of a non-negative integer n.  (LC 7 adds a sign and an overflow check.)

Examples:
    reverse(123) = 321
    reverse(1200) = 21
    reverse(7) = 7


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Peel off the last digit and append it to rev: rev = rev × 10 +
      digit.
 2. RECURSION
      Carry the answer in a parameter. When n reaches 0 the answer is
      ready: no work is needed on the way back.
 3. RECURSION + OUR OWN STACK
      DOWN: push the digits (the last digit goes in first). UP: the
      first digit pops first, so it gets place value 1, the next
      gets 10, and so on.
 4. OUR OWN STACK + BACKTRACKING
      On 'back' the most significant digit returns first, so give it
      place 1, then 10, then 100 …


💡 TAKEAWAY
-----------
A stack reverses order by nature (last in, first out), so reversing is
its natural job.

LEETCODE
--------
LC 7 · Reverse Integer -> https://leetcode.com/problems/reverse-integer/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def reverse_number_loop(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10        # append the last digit
        n = n // 10
    return rev


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def reverse_number_recursion(n, rev=0):
    if n == 0:                         # base case: rev is complete
        return rev
    return reverse_number_recursion(n // 10, rev * 10 + n % 10)


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def reverse_number_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push every digit
        stack.push(n % 10)
        n = n // 10
    result = 0
    place = 1
    while not stack.is_empty():        # coming UP: the first digit comes out first
        result = result + stack.pop() * place
        place = place * 10
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def reverse_number_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 0
    place = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n // 10, "go"))
        else:                          # "back": LEAVE -> first digit returns first
            result = result + (n % 10) * place
            place = place * 10
    return result


# ----------------------------------------------------------
# Test cases   (python3 04_reverse_number.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [reverse_number_loop, reverse_number_recursion, reverse_number_stack, reverse_number_backtrack]
    tests = [
        ((0,), 0),
        ((7,), 7),
        ((123,), 321),
        ((1200,), 21),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
