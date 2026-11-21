"""
============================================================
 09. BINARY STRINGS OF LENGTH N   (Backtracking: choose / explore / undo)
============================================================

PROBLEM
-------
Return every binary string of length n.  At each position you CHOOSE "0" or "1", EXPLORE further, then UNDO the choice.

Examples:
    binary_strings(2) = ["00", "01", "10", "11"]
    binary_strings(1) = ["0", "1"]


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Start with a list holding one empty string. Repeat n times: every
      string gets a "0" and a "1" added.
 2. RECURSION
      Grow a path one character at a time. When the path has length n it
      is a finished answer; otherwise try "0" and try "1".
 3. RECURSION + OUR OWN STACK
      The stack holds unfinished paths. Pop a path: if complete save it,
      else push the path with "1" and with "0" added.
 4. OUR OWN STACK + BACKTRACKING
      ONE shared path list. 'go' = CHOOSE a character (append). A
      finished path is saved and undone at once. Otherwise a
      'back' frame is left, so when the choices below are done we
      UNDO (pop).


💡 TAKEAWAY
-----------
This is the real backtracking pattern: choose → explore → UNDO. In
method 4 the shared path list and the "back" frames do the undo.

LEETCODE
--------
(no direct LeetCode problem: it is the warm-up)
also: LC 17 · Letter Combinations of a Phone Number -> https://leetcode.com/problems/letter-combinations-of-a-phone-number/
also: LC 22 · Generate Parentheses -> https://leetcode.com/problems/generate-parentheses/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def binary_strings_loop(n):
    result = [""]
    for _ in range(n):
        new_result = []
        for s in result:
            new_result.append(s + "0")
            new_result.append(s + "1")
        result = new_result
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def binary_strings_recursion(n, path=""):
    if len(path) == n:                 # base case: a complete string
        return [path]
    return (binary_strings_recursion(n, path + "0")
            + binary_strings_recursion(n, path + "1"))


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def binary_strings_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push("")
    result = []
    while not stack.is_empty():
        path = stack.pop()
        if len(path) == n:
            result.append(path)        # a complete string
        else:
            stack.push(path + "1")     # pushed first -> comes out last
            stack.push(path + "0")
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def binary_strings_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    path = []                          # the string we are building (shared)
    result = []
    stack.push(("1", "go"))            # second choice (comes out last)
    stack.push(("0", "go"))            # first choice
    while not stack.is_empty():
        choice, phase = stack.pop()
        if phase == "go":
            path.append(choice)                # CHOOSE
            if len(path) == n:
                result.append("".join(path))   # a complete string
                path.pop()                     # UNDO right away
            else:
                stack.push((choice, "back"))   # UNDO later
                stack.push(("1", "go"))        # next position: try 1 ...
                stack.push(("0", "go"))        # ... and 0 (explored first)
        else:                                  # "back": UNDO
            path.pop()
    return result


# ----------------------------------------------------------
# Test cases   (python3 09_binary_strings.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [binary_strings_loop, binary_strings_recursion, binary_strings_stack, binary_strings_backtrack]
    tests = [
        ((1,), ['0', '1']),
        ((2,), ['00', '01', '10', '11']),
        ((3,), ['000', '001', '010', '011', '100', '101', '110', '111']),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
