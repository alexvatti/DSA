"""
============================================================
 08. NUMBERS 1 TO N  (BEFORE VS AFTER)   (Work BEFORE vs AFTER the call)
============================================================

PROBLEM
-------
Return the list [1, 2, …, n] in order.  The point: the work done AFTER the recursive call happens on the way back.

Examples:
    numbers(3) = [1, 2, 3]
    numbers(5) = [1, 2, 3, 4, 5]
    numbers(0) = []


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Loop from 1 to n and add each number.
 2. RECURSION
      First solve for n−1, THEN add n. The adding happens after the call
      returns (on the way back).
 3. RECURSION + OUR OWN STACK
      DOWN: push n, n−1, …, 1. UP: pop. The number 1 sits on top, so it
      comes out first.
 4. OUR OWN STACK + BACKTRACKING
      'back' adds n. The deepest level (n = 1) comes back first, so the
      list is in order.


💡 TAKEAWAY
-----------
Work BEFORE the call = going down (gives n … 1). Work AFTER the call =
coming back (gives 1 … n). Moving one line changes the order.

LEETCODE
--------
(no direct LeetCode problem: it is the warm-up)
also: LC 344 · Reverse String -> https://leetcode.com/problems/reverse-string/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def numbers_loop(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def numbers_recursion(n):
    if n == 0:                         # base case: nothing to list
        return []
    return numbers_recursion(n - 1) + [n]     # add n AFTER the smaller answer


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def numbers_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push n, n-1, ... 1
        stack.push(n)
        n = n - 1
    result = []
    while not stack.is_empty():        # coming UP: 1 comes out first
        result.append(stack.pop())
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def numbers_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = []
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n - 1, "go"))
        else:                          # "back": LEAVE -> do the work
            result.append(n)
    return result


# ----------------------------------------------------------
# Test cases   (python3 08_numbers_1_to_n.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [numbers_loop, numbers_recursion, numbers_stack, numbers_backtrack]
    tests = [
        ((0,), []),
        ((1,), [1]),
        ((3,), [1, 2, 3]),
        ((5,), [1, 2, 3, 4, 5]),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
