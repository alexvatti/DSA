"""
============================================================
 8. PERMUTATION IN STRING   (LeetCode 567)
============================================================

PROBLEM
-------
Given strings s1 and s2, return True if s2 contains a permutation
of s1 (i.e. some substring of s2 is an anagram of s1).

Example:
    s1 = "ab", s2 = "eidbaooo" -> True   ("ba")
    s1 = "ab", s2 = "eidboaoo" -> False


FIXED SLIDING WINDOW APPROACH
-----------------------------
A permutation has the same length and same letter counts as s1,
so the window size is FIXED = len(s1).

    need   -> letter counts of s1        (26 slots)
    window -> letter counts of the current window in s2

Step by step:
    1. Build `need` from s1 and `window` from the first len(s1)
       characters of s2.
    2. If window == need -> True.
    3. Slide one step: add the new right character, remove the
       character that left the window.
    4. Compare again. Repeat until the end of s2.


💡 TIPS TO REMEMBER
-------------------
- "Permutation / anagram in a string" => fixed window + counts.
- Window size never changes: add one on the right, remove one on the left.
- Comparing two lists of 26 numbers is O(26) = O(1).
- Time: O(n)   Space: O(1)
"""


def check_inclusion(s1: str, s2: str) -> bool:
    k = len(s1)
    if k > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26

    for ch in s1:
        need[ord(ch) - ord("a")] += 1

    for i in range(len(s2)):
        # Add the new character on the right
        window[ord(s2[i]) - ord("a")] += 1

        # Remove the character that fell out on the left
        if i >= k:
            window[ord(s2[i - k]) - ord("a")] -= 1

        # Window is full-size -> compare counts
        if i >= k - 1 and window == need:
            return True

    return False


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(check_inclusion("ab", "eidbaooo"))  # True
    print(check_inclusion("ab", "eidboaoo"))  # False
    print(check_inclusion("abc", "ab"))       # False
    print(check_inclusion("adc", "dcda"))     # True
