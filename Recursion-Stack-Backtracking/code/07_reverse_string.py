"""
============================================================
 07. REVERSE A STRING   (Linear recursion (1 branch))
============================================================

PROBLEM
-------
Return the characters of s in reverse order.  (LC 344 asks to do it in place on a list.)

Examples:
    reverse("abc") = "cba"
    reverse("hello") = "olleh"
    reverse("") = ""


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Build the answer by putting each new character in FRONT of the
      result.
 2. RECURSION
      reverse(s) = reverse(everything after the first character) + the
      first character.
 3. RECURSION + OUR OWN STACK
      Push every character, then pop everything: last in, first out
      gives the reverse.
 4. OUR OWN STACK + BACKTRACKING
      'go' walks the index forward. On 'back' the LAST index returns
      first, so adding s[i] builds the string reversed.


💡 TAKEAWAY
-----------
Last in, first out: pushing every character and popping them all IS
the reverse.

LEETCODE
--------
LC 344 · Reverse String -> https://leetcode.com/problems/reverse-string/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def reverse_string_loop(s):
    result = ""
    for ch in s:
        result = ch + result           # new character goes in front
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def reverse_string_recursion(s):
    if len(s) <= 1:                    # base case
        return s
    return reverse_string_recursion(s[1:]) + s[0]


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def reverse_string_stack(s):
    stack = Stack()                    # our own stack -> see stack_base.py
    for ch in s:                       # going DOWN: push every character
        stack.push(ch)
    result = ""
    while not stack.is_empty():        # coming UP: the last character pops first
        result = result + stack.pop()
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def reverse_string_backtrack(s):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, "go"))
    result = ""
    while not stack.is_empty():
        i, phase = stack.pop()
        if phase == "go":              # ENTER
            if i < len(s):
                stack.push((i, "back"))
                stack.push((i + 1, "go"))
        else:                          # "back": LEAVE -> last index returns first
            result = result + s[i]
    return result


# ----------------------------------------------------------
# Test cases   (python3 07_reverse_string.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    methods = [reverse_string_loop, reverse_string_recursion, reverse_string_stack, reverse_string_backtrack]
    tests = [
        (('',), ''),
        (('a',), 'a'),
        (('abc',), 'cba'),
        (('hello',), 'olleh'),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(r == expected for r in results), results
    print("all four methods agree on every test ✅")
