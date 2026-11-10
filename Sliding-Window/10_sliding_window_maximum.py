"""
============================================================
 10. SLIDING WINDOW MAXIMUM   (LeetCode 239)
============================================================

PROBLEM
-------
Given an array nums and a window size k, the window slides from the
left to the right, one step at a time. Return the maximum of every
window.

Example:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    -> [3, 3, 5, 5, 6, 7]


FIXED WINDOW + MONOTONIC DEQUE APPROACH
---------------------------------------
Brute force (max of each window) is O(n*k). Instead keep a deque of
INDICES whose values are in DECREASING order:

    front of deque -> index of the current window's maximum
    back of deque  -> newest, smaller candidates

Step by step (for each index i):
    1. If the front index is outside the window (<= i - k) -> popleft.
    2. While the back value is SMALLER than nums[i] -> pop it
       (it can never be a maximum while nums[i] is in the window).
    3. Append i.
    4. Once the first window is full (i >= k - 1),
       the answer for this window is nums[deque[0]].

Why it works: smaller elements before a bigger one are useless, so the
deque stays sorted and its front is always the maximum.


💡 TIPS TO REMEMBER
-------------------
- "Max/min of every window" => monotonic deque.
- Store INDICES, not values (so you can check if they left the window).
- Each index is added once and removed once -> O(n) total.
- Time: O(n)   Space: O(k)
"""
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()   # indices, values decreasing
    result = []

    for i in range(len(nums)):
        # 1. Drop the front if it slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # 2. Drop smaller values from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3. Add the current index
        dq.append(i)

        # 4. Window is full -> front is the maximum
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                         # [1]
    print(max_sliding_window([9, 11], 2))                     # [11]
    print(max_sliding_window([4, 3, 2, 1], 2))                # [4,3,2]
