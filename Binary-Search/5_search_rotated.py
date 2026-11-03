"""
============================================================
 5. SEARCH IN ROTATED SORTED ARRAY   (LeetCode 33)
============================================================
 Reference: https://codeanddebug.in/blog/search-in-rotated-sorted-array/

PROBLEM
-------
A sorted array of UNIQUE numbers was rotated. Given target, return its
INDEX or -1, in O(log n).

Example:
    nums = [4, 5, 6, 7, 0, 1, 2], target = 0  -> 4
    nums = [4, 5, 6, 7, 0, 1, 2], target = 3  -> -1


APPROACH — identify the sorted half each step
----------------------------------------------
At any mid, AT LEAST ONE half is sorted. Find which, then check if target
lies inside that sorted half:

    1. mid = (low + high) // 2; if nums[mid] == target -> return mid.
    2. Left half sorted (nums[low] <= nums[mid]):
         - if nums[low] <= target < nums[mid] -> go left:  high = mid - 1
         - else                               -> go right: low  = mid + 1
    3. Right half sorted (otherwise):
         - if nums[mid] < target <= nums[high] -> go right: low  = mid + 1
         - else                                -> go left:  high = mid - 1
    4. If the loop ends -> return -1.

Why it works: we always narrow to the half we can reason about (the sorted
one), so we never lose the target.


💡 TIPS TO REMEMBER
-------------------
- Rotated + search a value => "find the sorted half, then range-check".
- Decide sorted side with nums[low] <= nums[mid].
- Use INCLUSIVE checks (<=) against the sorted half's endpoints.
- Classic exact-match loop uses low <= high.
- Time: O(log n)   Space: O(1)
"""


def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1     # target in sorted left half
            else:
                low = mid + 1      # search right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1      # target in sorted right half
            else:
                high = mid - 1     # search left half

    return -1  # not found


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))   # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))   # -1
    print(search([1], 0))                      # -1
    print(search([5, 1, 3], 5))                # 0
    print(search([4, 5, 6, 7, 0, 1, 2], 6))   # 2
