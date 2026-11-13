"""
============================================================
 1. VALID PARENTHESES (LeetCode 20)
============================================================

PROBLEM
-------
Given a string s containing only the characters ( ) [ ] { }, return True if it is valid:
every opener is closed by the same type, in the correct order.

Example:
    "()"      -> True
    "()[]{}"  -> True
    "(]"      -> False  (wrong type)
    "([)]"    -> False  (wrong order)


APPROACH — STACK (MATCH AND POP)
--------------------------------
The last opener we saw must be the first one closed — that is exactly Last-In-First-Out.

    stack -> openers still waiting for their closer

Step by step:
    1. Walk through each character.
    2. Opener ( [ { → push it.
    3. Closer → the stack must be non-empty and its top must be the matching opener, then pop it. Otherwise → False.
    4. At the end the stack must be empty (no unmatched opener left).

Why it works: A closer can only legally pair with the most recent unmatched opener — the top of the stack. Nesting is naturally LIFO.


💡 TIPS TO REMEMBER
-------------------
- Nested / paired / "most recent" things ⇒ think stack.
- Use a dict closer -> opener to avoid a long if/elif chain.
- Forgetting the final not stack check fails inputs like "(((".
- Quick reject: an odd length can never be valid.
- Time: O(n)   Space: O(n)
"""


def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in pairs:
            # Closer -> top must be its matching opener
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # Opener -> wait for its closer
            stack.append(ch)

    # Every opener must have been matched
    return not stack


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("()[]{}"))    # True
    print(is_valid("(]"))        # False
    print(is_valid("([)]"))      # False
    print(is_valid("{[]}"))      # True
    print(is_valid("((("))       # False
    print(is_valid(""))          # True
