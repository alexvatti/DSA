"""
============================================================
 4. FIND MINIMUM IN ROTATED SORTED ARRAY   (LeetCode 153)
============================================================
 Reference: https://codeanddebug.in/blog/find-minimum-in-rotated-sorted-array/

PROBLEM
-------
A sorted array of UNIQUE numbers was rotated an unknown number of times.
Find the MINIMUM element in O(log n).

Example:
    [3, 4, 5, 1, 2]       -> 1
    [4, 5, 6, 7, 0, 1, 2] -> 0


APPROACH — find the unsorted half
----------------------------------
The minimum is the pivot point where order breaks. Compare nums[mid] with
nums[high] to know which half holds the minimum:

    - If nums[mid] > nums[high] -> right half is UNSORTED and holds the min
      (pivot is to the right): low = mid + 1.
    - Else (nums[mid] <= nums[high]) -> right half is sorted, min is at mid
      or to its left: high = mid.

Loop until low == high, which lands exactly on the minimum.
(Compare with nums[high], not nums[low] — it gives a clean rule.)

Step by step:
    1. low = 0, high = n - 1.
    2. While low < high:
    3. mid = (low + high) // 2.
    4. If nums[mid] > nums[high] -> low = mid + 1, else high = mid.
    5. Return nums[low].


💡 TIPS TO REMEMBER
-------------------
- Rotated sorted array => one half is always properly sorted.
- Compare mid with high to find which side the pivot (min) is on.
- Use low < high and high = mid (not mid - 1) so you never skip the min.
- Works even with no rotation (already sorted).
- Time: O(log n)   Space: O(1)
"""


def find_min(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1     # min is in the right (unsorted) half
        else:
            high = mid        # min is at mid or to its left

    return nums[low]


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))         # 1
    print(find_min([4, 5, 6, 7, 0, 1, 2]))   # 0
    print(find_min([11, 13, 15, 17]))        # 11
    print(find_min([2, 1]))                  # 1
    print(find_min([1]))                     # 1
