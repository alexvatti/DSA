"""
============================================================
 5. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS (LeetCode 3)
============================================================

PROBLEM
-------
Given a string, return the length of the longest substring that
has NO repeating characters.

Example:
    "abcabcbb" -> 3   ("abc")
    "bbbbb"    -> 1   ("b")
    "pwwkew"   -> 3   ("wke")


VARIABLE SLIDING WINDOW APPROACH
--------------------------------
    left  -> start of the window
    right -> end of the window (moves forward every step)
    seen  -> set of characters currently inside the window

Step by step:
    1. Move `right` forward, one character at a time.
    2. While s[right] is already in the window (duplicate):
         remove s[left] from the set and move left forward.
    3. Add s[right] to the set.
    4. Window is now valid -> update the best length.

Why it works: the window ALWAYS holds unique characters. When a
duplicate shows up we shrink from the left just enough to remove it.


💡 TIPS TO REMEMBER
-------------------
- "Longest substring/subarray with a condition" => variable window.
- Expand with right, shrink with `while` (not `if`) when invalid.
- A set tracks "what is inside the window".
- Time: O(n)   Space: O(min(n, alphabet))
"""


def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        # Shrink the window until the duplicate is gone
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Expand: add the new character
        seen.add(s[right])

        # Window is valid -> update the answer
        best = max(best, right - left + 1)

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
