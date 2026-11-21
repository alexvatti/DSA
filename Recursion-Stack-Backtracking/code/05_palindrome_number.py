"""
============================================================
 05. PALINDROME NUMBER   (Two-ended check)
============================================================

PROBLEM
-------
Return True if the number reads the same forwards and backwards. Negative numbers are not palindromes.

Examples:
    121 → True
    123 → False
    -121 → False
    1221 → True


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Two pointers on the digit string: compare the outer pair, then
      move inwards.
 2. RECURSION
      Palindrome if the outer two match AND the inside is a palindrome.
      Base case: fewer than 2 digits.
 3. RECURSION + OUR OWN STACK
      Push every digit. Popping gives the digits backwards, so compare
      each original digit with the popped one.
 4. OUR OWN STACK + BACKTRACKING
      'go' walks the index i towards the middle. On 'back' (innermost
      pair first) compare s[i] with its mirror s[j]. A mismatch
      stops early.


💡 TAKEAWAY
-----------
A stack gives the digits backwards for free: compare "forwards" with
"popped" and you are done.

LEETCODE
--------
LC 9 · Palindrome Number -> https://leetcode.com/problems/palindrome-number/
also: LC 125 · Valid Palindrome -> https://leetcode.com/problems/valid-palindrome/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def palindrome_loop(n):
    s = str(n)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:        # outer pair differs
            return False
        left = left + 1
        right = right - 1
    return True


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def palindrome_recursion(n, s=None):
    if s is None:
        s = str(n)                     # first call: number -> text
    if len(s) < 2:                     # base case: 0 or 1 digit
        return True
    if s[0] != s[-1]:                  # outer pair differs
        return False
    return palindrome_recursion(n, s[1:-1])    # check the inside


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def palindrome_stack(n):
    s = str(n)
    stack = Stack()                    # our own stack -> see stack_base.py
    for ch in s:                       # going DOWN: push every digit
        stack.push(ch)
    for ch in s:                       # coming UP: pop = the digits backwards
        if ch != stack.pop():
            return False
    return True


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def palindrome_backtrack(n):
    s = str(n)
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, "go"))
    while not stack.is_empty():
        i, phase = stack.pop()
        j = len(s) - 1 - i             # the mirror position of i
        if phase == "go":              # ENTER
            if i < j:
                stack.push((i, "back"))
                stack.push((i + 1, "go"))
        else:                          # "back": LEAVE -> compare the pair
            if s[i] != s[j]:
                return False
    return True


# ----------------------------------------------------------
# Test cases   (python3 05_palindrome_number.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [palindrome_loop, palindrome_recursion, palindrome_stack, palindrome_backtrack]
    tests = [
        ((121,), True),
        ((123,), False),
        ((-121,), False),
        ((1221,), True),
        ((7,), True),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
