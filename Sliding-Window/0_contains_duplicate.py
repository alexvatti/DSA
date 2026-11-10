"""
============================================================
 0. CONTAINS DUPLICATE (LeetCode 217)
============================================================

PROBLEM
-------
Given an integer array `nums`, return True if any value appears
at least twice, and False if every element is distinct.

Example:
    [1, 2, 3, 1]       -> True   (1 repeats)
    [1, 2, 3, 4]       -> False  (all unique)
    [1, 1, 1, 3, 3, 4] -> True


APPROACH — HASH SET
-------------------
    seen -> set of numbers we have already passed

Step by step:
    1. Walk through each number once.
    2. If the number is already in `seen` -> duplicate -> return True.
    3. Otherwise add it to `seen`.
    4. Loop ends with no clash -> return False.

Why it works: a set answers "have I seen this?" in O(1). This is the
exact lookup trick every variable sliding window uses to keep its
contents unique, so it is the perfect warm-up for the pattern.


💡 TIPS TO REMEMBER
-------------------
- "Any duplicate?" => dump into a set and watch for a repeat.
- A set gives O(1) membership -> backbone of window problems.
- One-liner: len(set(nums)) != len(nums)
- Time: O(n)   Space: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        # Already inside the set -> we found a repeat
        if num in seen:
            return True
        seen.add(num)

    return False


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))        # True
    print(contains_duplicate([1, 2, 3, 4]))        # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4]))  # True
    print(contains_duplicate([]))                  # False
