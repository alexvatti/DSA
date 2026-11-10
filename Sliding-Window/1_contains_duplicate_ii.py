"""
============================================================
 1. CONTAINS DUPLICATE II (LeetCode 219)
============================================================

PROBLEM
-------
Given an integer array `nums` and an integer `k`, return True if
there are two DISTINCT indices i and j such that
nums[i] == nums[j] AND abs(i - j) <= k.

Example:
    nums = [1,2,3,1],     k = 3  -> True   (indices 0 and 3)
    nums = [1,0,1,1],     k = 1  -> True   (indices 2 and 3)
    nums = [1,2,3,1,2,3], k = 2  -> False  (nearest repeat is distance 3)


FIXED SLIDING WINDOW APPROACH
-----------------------------
    window -> set holding the values of the last k indices
    right  -> current index

Step by step:
    1. Move `right` forward through the array.
    2. If nums[right] is already in `window` -> duplicate within k -> True.
    3. Add nums[right] to the window.
    4. If the window now holds more than k values, remove the element
       that fell off the left (nums[right - k]).
    5. Loop ends -> return False.

Why it works: the set never holds more than k items, so any match
inside it is guaranteed to be within distance k.


💡 TIPS TO REMEMBER
-------------------
- "Duplicate within distance k" => fixed window of size k + a set.
- Drop nums[right - k] when the window overflows -> that is the slide.
- Avoids the O(n*k) double loop.
- Time: O(n)   Space: O(min(n, k))
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    window = set()

    for right in range(len(nums)):
        # A match inside the window means distance <= k
        if nums[right] in window:
            return True

        window.add(nums[right])

        # Keep the window to at most k elements
        if len(window) > k:
            window.remove(nums[right - k])

    return False


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))           # True
    print(contains_nearby_duplicate([1, 0, 1, 1], 1))           # True
    print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))     # False
    print(contains_nearby_duplicate([1, 2, 3, 4], 0))           # False
