"""
============================================================
 1. TWO SUM   (LeetCode 1)
============================================================

PROBLEM
-------
Given an array of integers `nums` and an integer `target`, return the
INDICES of the two numbers that add up to `target`.
Exactly one solution exists, and you can't use the same element twice.

Example:
    nums = [2, 7, 11, 15], target = 9  -> [0, 1]   (2 + 7 = 9)
    nums = [3, 2, 4],      target = 6  -> [1, 2]
    nums = [3, 3],         target = 6  -> [0, 1]


BRUTE FORCE vs HASH MAP
-----------------------
Brute force: try every pair with 2 nested loops  -> O(n^2).
Hash map:    for each number, ask "have I already seen the
             number that completes the pair?"   -> O(n).


HASH MAP APPROACH (one pass)
----------------------------
    seen = { value : index }

Step by step:
    1. For the current number x, compute need = target - x.
    2. If `need` is already in `seen` -> answer is [seen[need], i].
    3. Otherwise store seen[x] = i and move on.

Why it works: when we reach the 2nd number of the pair, the 1st one
is guaranteed to be in the map already.


💡 TIPS TO REMEMBER
-------------------
- "Find a pair that sums to target" + UNSORTED => hash map.
  (Sorted? => two pointers instead.)
- Store the VALUE as key and the INDEX as value.
- Check the map BEFORE inserting, so an element never pairs with itself.
- Time: O(n)   Space: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index

    for i, x in enumerate(nums):
        need = target - x          # the number that completes the pair

        if need in seen:           # O(1) lookup
            return [seen[need], i]

        seen[x] = i                # remember x for later numbers

    return []                      # (problem guarantees we never get here)


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]
