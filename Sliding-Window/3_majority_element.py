"""
============================================================
 3. MAJORITY ELEMENT (LeetCode 169)
============================================================

PROBLEM
-------
Given an array `nums` of size n, return the majority element -- the
element that appears more than floor(n / 2) times. You may assume it
always exists.

Example:
    [3, 2, 3]             -> 3
    [2, 2, 1, 1, 1, 2, 2] -> 2


APPROACH — HASH MAP COUNT (then Boyer-Moore)
--------------------------------------------
    counts -> dict mapping value -> how many times it appeared

Step by step (counts):
    1. Walk through nums, incrementing counts[num].
    2. The moment a count passes n // 2 -> that value is the answer.

BOYER-MOORE VOTING (O(1) space bonus):
    Keep a `candidate` and a `count`:
      - count 0 -> adopt the current number as candidate.
      - same as candidate -> count += 1, else count -= 1.
    The majority survives because it outnumbers everything else combined.


💡 TIPS TO REMEMBER
-------------------
- "Appears more than half the time" => counts dict or Boyer-Moore.
- A frequency dict is the same tool windows use for "count of each value".
- Boyer-Moore: cancel pairs of different elements; majority remains.
- Time: O(n)   Space: O(n) dict / O(1) voting
"""


def majority_element(nums: list[int]) -> int:
    # --- Boyer-Moore Voting: O(n) time, O(1) space ---
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num          # adopt a fresh candidate
        count += 1 if num == candidate else -1

    return candidate


def majority_element_counts(nums: list[int]) -> int:
    # --- Hash map version (easier to read) ---
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(majority_element([3, 2, 3]))                  # 3
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))      # 2
    print(majority_element_counts([3, 2, 3]))           # 3
    print(majority_element_counts([2, 2, 1, 1, 1, 2, 2]))  # 2
