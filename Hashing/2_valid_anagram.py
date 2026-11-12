"""
============================================================
 2. VALID ANAGRAM   (LeetCode 242)
============================================================

PROBLEM
-------
Given two strings `s` and `t`, return True if `t` is an anagram of `s`
(same letters, same counts, any order).

Example:
    s = "anagram", t = "nagaram" -> True
    s = "rat",     t = "car"     -> False


HASH MAP APPROACH (frequency count)
-----------------------------------
    count = { character : how many times }

Step by step:
    1. If the lengths differ -> False immediately.
    2. Walk through `s` and ADD 1 to count[char].
    3. Walk through `t` and SUBTRACT 1 from count[char].
       If a char is missing (or already 0) -> False.
    4. If we finish `t` without a problem -> True.

Why it works: same length + never subtracting below zero means every
letter in `t` was "paid for" by a letter in `s`.


💡 TIPS TO REMEMBER
-------------------
- "Same characters, any order" => FREQUENCY COUNT.
- Check the lengths first — it is a free early exit.
- Lowercase-only input? A fixed array of 26 ints works too.
- Sorting both strings also works, but is O(n log n).
- Time: O(n)   Space: O(1)  (at most 26 / alphabet-size keys)
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Pass 1: count every character of s
    for c in s:
        count[c] = count.get(c, 0) + 1

    # Pass 2: "spend" those counts using t
    for c in t:
        if count.get(c, 0) == 0:   # t has a char s can't supply
            return False
        count[c] -= 1

    return True


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("a", "ab"))             # False (different length)
    print(is_anagram("aacc", "ccac"))        # False (counts differ)
