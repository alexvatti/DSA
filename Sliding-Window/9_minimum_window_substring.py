"""
============================================================
 9. MINIMUM WINDOW SUBSTRING   (LeetCode 76)
============================================================

PROBLEM
-------
Given strings s and t, return the smallest substring of s that
contains every character of t (including duplicates).
Return "" if none exists.

Example:
    s = "ADOBECODEBANC", t = "ABC" -> "BANC"
    s = "a",            t = "a"   -> "a"
    s = "a",            t = "aa"  -> ""


VARIABLE SLIDING WINDOW APPROACH
--------------------------------
    need     -> dict {char: how many we need} (from t)
    window   -> dict {char: how many we have in the window}
    have     -> number of distinct chars whose requirement is met
    required -> len(need)  (distinct chars in t)

Step by step:
    1. Expand `right`: add s[right] to `window`.
       If its count now equals need[char] -> have += 1.
    2. While have == required (window is VALID):
         - record the window if it is the smallest so far
         - remove s[left]; if that breaks a requirement, have -= 1
         - move left forward  (try to make the window smaller)
    3. Continue until right reaches the end.

Why it works: expand until valid, then shrink as much as possible
while still valid. Every candidate smallest window is checked.


💡 TIPS TO REMEMBER
-------------------
- "Smallest window containing ..." => expand to be valid, then shrink.
- Track `have` vs `required` so validity is checked in O(1).
- Use a strict `<` when comparing lengths to keep the first best.
- Time: O(n + m)   Space: O(m)
"""


def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    have = 0
    required = len(need)

    best_len = float("inf")
    best_start = 0
    left = 0

    for right in range(len(s)):
        # Expand: add the new character
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1

        # Shrink while the window is valid
        while have == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left

            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                have -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_start:best_start + best_len]


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # BANC
    print(min_window("a", "a"))                # a
    print(min_window("a", "aa"))               # "" (empty)
    print(min_window("aa", "aa"))              # aa
