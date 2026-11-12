"""
============================================================
 4. LONGEST CONSECUTIVE SEQUENCE   (LeetCode 128)
============================================================

PROBLEM
-------
Given an UNSORTED array of integers, return the length of the longest
run of consecutive values (like 1,2,3,4). Must run in O(n).

Example:
    [100, 4, 200, 1, 3, 2]          -> 4   (1,2,3,4)
    [0,3,7,2,5,8,4,6,0,1]           -> 9   (0..8)


WHY NOT SORT?
-------------
Sorting is O(n log n). The problem demands O(n) -> use a HASH SET.


HASH SET APPROACH
-----------------
    num_set = set(nums)         # O(1) "does it exist?" checks

Step by step:
    1. Put all numbers in a set (also removes duplicates).
    2. For each x, check: is x - 1 in the set?
         YES -> x is in the MIDDLE of a run, skip it.
         NO  -> x is the START of a run. Count upward:
                x+1, x+2, ... while they exist in the set.
    3. Track the longest length.

Why it's still O(n): each number is "walked over" only by the run that
starts at its beginning. Total walking across all runs = n.


💡 TIPS TO REMEMBER
-------------------
- "Consecutive numbers + O(n)" => SET + only start from run beginnings.
- The magic check:  if x - 1 not in num_set.
- Loop over the SET (not the list) to skip duplicates.
- Time: O(n)   Space: O(n)
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0

    for x in num_set:
        if x - 1 not in num_set:          # x starts a new run
            length = 1
            while x + length in num_set:  # walk the run
                length += 1
            best = max(best, length)

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))        # 4
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))# 9
    print(longest_consecutive([]))                            # 0
    print(longest_consecutive([1, 2, 0, 1]))                  # 3
