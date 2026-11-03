"""
============================================================
 1. VALID PALINDROME   (LeetCode 125)
============================================================

PROBLEM
-------
Given a string, return True if it reads the same forwards and
backwards, considering ONLY letters and numbers, and ignoring case.

Example:
    "A man, a plan, a canal: Panal"  -> ... let's use a real one
    "A man, a plan, a canal: Panama" -> True
    "race a car"                     -> False


TWO-POINTER APPROACH
--------------------
Use two pointers at opposite ends:
    left  -> starts at the beginning
    right -> starts at the end

Step by step:
    1. Skip any character that is NOT a letter/number.
    2. Compare the characters at `left` and `right` (lowercased).
    3. If they differ -> NOT a palindrome -> return False.
    4. Move left forward (+1) and right backward (-1).
    5. Repeat until the pointers meet in the middle.

Why it works: a palindrome mirrors around its center, so the
1st char must match the last, 2nd must match 2nd-last, etc.


💡 TIPS TO REMEMBER
-------------------
- "Compare front vs back" => opposite-ends pointers.
- Loop while  left < right.
- Clean the input: use .isalnum() to keep only letters/digits.
- Always lowercase before comparing.
- Time: O(n)   Space: O(1)
"""


def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the two valid characters (ignore case)
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers inward
        left += 1
        right -= 1

    return True


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                       # False
    print(is_palindrome(" "))                                # True (empty)
    print(is_palindrome("0P"))                               # False
