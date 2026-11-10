"""
============================================================
 4. MOST FREQUENT EVEN ELEMENT (LeetCode 2404)
============================================================

PROBLEM
-------
Given an integer array `nums`, return the most frequent even element.
If there is a tie, return the smallest one. If there are no even
numbers, return -1.

Example:
    [0,1,2,2,4,4,1] -> 2    (2 and 4 both twice -> pick smaller, 2)
    [4,4,4,9,2,4]   -> 4    (appears 4 times)
    [29,47,21]      -> -1   (no even numbers)


APPROACH — FREQUENCY MAP
------------------------
    counts -> dict mapping even value -> how many times it appeared

Step by step:
    1. Walk through nums; if a number is even, increment counts[num].
    2. Scan the dict for the best element:
         - higher count wins;
         - on a tie, the smaller value wins.
    3. If no even numbers were counted -> return -1.

Why it works: counting is one pass; a clear tie-break rule guarantees
the smallest among the most frequent.


💡 TIPS TO REMEMBER
-------------------
- "Most frequent ... (with a filter)" => frequency dict, pick max by rule.
- Tie-break "smallest value" -> check (count, value) carefully.
- Filter first (even only) so the dict stays clean.
- Time: O(n)   Space: O(n)
"""


def most_frequent_even(nums: list[int]) -> int:
    counts = {}
    for num in nums:
        if num % 2 == 0:                       # only even numbers
            counts[num] = counts.get(num, 0) + 1

    if not counts:                             # no even element
        return -1

    best_val = -1
    best_count = 0
    for val, cnt in counts.items():
        # higher count wins; on a tie pick the smaller value
        if cnt > best_count or (cnt == best_count and val < best_val):
            best_val = val
            best_count = cnt

    return best_val


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(most_frequent_even([0, 1, 2, 2, 4, 4, 1]))  # 2
    print(most_frequent_even([4, 4, 4, 9, 2, 4]))     # 4
    print(most_frequent_even([29, 47, 21]))           # -1
    print(most_frequent_even([8, 8]))                 # 8
