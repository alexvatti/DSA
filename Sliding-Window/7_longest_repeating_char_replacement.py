"""
============================================================
 7. LONGEST REPEATING CHARACTER REPLACEMENT (LeetCode 424)
============================================================

PROBLEM
-------
Given an uppercase string s and an integer k, you may change at most
k characters to any other letter. Return the length of the longest
substring containing the same letter after those changes.

Example:
    s = "ABAB",    k = 2 -> 4
    s = "AABABBA", k = 1 -> 4


VARIABLE SLIDING WINDOW APPROACH
--------------------------------
Key insight:
    changes needed for a window = window length - (count of the
                                  most frequent letter in it)

We keep the most frequent letter and replace all the others.
The window is VALID when  changes needed <= k.

    left, right -> window edges
    count       -> dict {letter: frequency in window}

Step by step:
    1. Add s[right] to `count`.
    2. While (window length - max frequency) > k:
         remove s[left] from `count`, move left forward.
    3. Window is valid -> update the best length.


💡 TIPS TO REMEMBER
-------------------
- Formula to memorize:  (window size - max freq) <= k
- This version recomputes max(count.values()) -> at most 26 values,
  so still O(26 * n) = O(n).
- Known optimization: keep a running max_freq that never decreases
  and use `if` instead of `while` (the window never shrinks).
- Time: O(n)   Space: O(1)  (at most 26 letters)
"""


def character_replacement(s: str, k: int) -> int:
    count = {}
    left = 0
    best = 0

    for right in range(len(s)):
        # Expand
        count[s[right]] = count.get(s[right], 0) + 1

        # Shrink while we need more than k replacements
        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(character_replacement("ABAB", 2))      # 4
    print(character_replacement("AABABBA", 1))   # 4
    print(character_replacement("AAAA", 0))      # 4
    print(character_replacement("ABCDE", 1))     # 2
