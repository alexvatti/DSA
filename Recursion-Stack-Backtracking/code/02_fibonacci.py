"""
============================================================
 02. FIBONACCI   (Tree recursion (2 branches))
============================================================

PROBLEM
-------
fib(0) = 0, fib(1) = 1, and fib(n) = fib(n−1) + fib(n−2). Return fib(n).

Examples:
    fib(4) = 3
    fib(5) = 5
    sequence: 0 1 1 2 3 5 8 13 …


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Keep only the last two numbers (a, b) and slide forward n times.
 2. RECURSION
      fib(n) = fib(n−1) + fib(n−2). Two calls per call, so the calls
      form a tree (slow for big n, but very clear).
 3. RECURSION + OUR OWN STACK
      A stack of pending sub-problems. Pop k: if k < 2 it is a base
      case, add k to the total; otherwise push the two smaller
      problems k−1 and k−2.
 4. OUR OWN STACK + BACKTRACKING
      Two stacks: 'work' holds (k, phase) frames, 'values' holds
      finished answers. 'go' with k ≥ 2 leaves a 'back' frame.
      When we come 'back', pop two answers and push their sum.


💡 TAKEAWAY
-----------
Two recursive calls make a TREE. With our own stack we walk the same
tree depth-first ourselves.

LEETCODE
--------
LC 509 · Fibonacci Number -> https://leetcode.com/problems/fibonacci-number/
also: LC 70 · Climbing Stairs -> https://leetcode.com/problems/climbing-stairs/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def fib_recursion(n):
    if n < 2:                          # base cases: fib(0)=0, fib(1)=1
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def fib_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push(n)
    total = 0
    while not stack.is_empty():
        k = stack.pop()
        if k < 2:
            total = total + k          # base case: fib(k) = k
        else:
            stack.push(k - 1)          # two smaller problems
            stack.push(k - 2)
    return total


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def fib_backtrack(n):
    work = Stack()                     # our own stack -> see stack_base.py
    values = Stack()                   # finished answers waiting to be combined
    work.push((n, "go"))
    while not work.is_empty():
        k, phase = work.pop()
        if phase == "go":              # ENTER
            if k < 2:
                values.push(k)         # base case: the answer is k
            else:
                work.push((k, "back"))     # combine later
                work.push((k - 2, "go"))
                work.push((k - 1, "go"))   # this one is explored first
        else:                          # "back": LEAVE, combine two answers
            values.push(values.pop() + values.pop())
    return values.pop()


# ----------------------------------------------------------
# Test cases   (python3 02_fibonacci.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [fib_loop, fib_recursion, fib_stack, fib_backtrack]
    tests = [
        ((0,), 0),
        ((1,), 1),
        ((4,), 3),
        ((6,), 8),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
