"""
============================================================
 1. BINARY SEARCH   (LeetCode 704)
============================================================
 Reference: https://codeanddebug.in/blog/binary-search-leetcode-704/

PROBLEM
-------
Given a SORTED array nums and a target, return the INDEX of target
if it exists, otherwise return -1.

Example:
    nums = [-1, 0, 3, 5, 9, 12], target = 9  -> 4


BINARY SEARCH APPROACH (search space halving)
---------------------------------------------
Keep two pointers bounding the search space:
    low  -> start of search space
    high -> end of search space
    mid  -> middle index = low + (high - low) // 2

Step by step:
    1. While low <= high:
    2. Compute mid.
    3. If nums[mid] == target -> found it! Return mid.
    4. If nums[mid] < target  -> target is on the RIGHT, low = mid + 1.
    5. If nums[mid] > target  -> target is on the LEFT,  high = mid - 1.
    6. If the loop ends, target is absent -> return -1.

Why it works: the array is sorted, so the middle element tells us
which half can contain the target. We discard the other half each step.


💡 TIPS TO REMEMBER
-------------------
- SORTED input + find index/value => binary search.
- Loop condition low <= high for the classic "find exact" variant.
- mid = low + (high - low) // 2 avoids integer overflow (good habit).
- Each step halves the space.
- Time: O(log n)   Space: O(1)
"""


def binary_search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1     # go right
        else:
            high = mid - 1    # go left

    return -1  # target not found


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # -1
    print(binary_search([5], 5))                     # 0
    print(binary_search([], 1))                      # -1
