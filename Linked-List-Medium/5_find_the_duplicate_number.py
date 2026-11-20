"""
============================================================
 5. FIND THE DUPLICATE NUMBER (LeetCode 287)
============================================================

PROBLEM
-------
Given an array nums of n + 1 integers, each in the range [1, n], exactly one number is repeated. Return it WITHOUT modifying the array and using only O(1) extra space.

Example:
    [1, 3, 4, 2, 2]   =>  2
    [3, 1, 3, 4, 2]   =>  3
    [3, 3, 3, 3, 3]   =>  3


WHEN TO USE
-----------
- Values are in 1..n in an array of n + 1, so nums[i] works as a next pointer
- The array must not change and extra space must be O(1)
- 🔍 Keywords: find the duplicate, 1..n, cannot modify, constant space


APPROACH — FLOYD ON AN ARRAY
----------------------------
An array of n + 1 numbers in 1..n is secretly a linked list: index i points to nums[i]. Two indexes hold the same value, so two nodes point to one node → a cycle, and the cycle entrance is the duplicate. Use slow & fast to get into the cycle, then find the entrance.

Step by step:
    1. Phase 1: slow = nums[slow], fast = nums[nums[fast]] until they meet (inside the cycle).
    2. Phase 2: put slow back at 0; keep fast at the meeting point.
    3. Move both one step at a time until they meet again.
    4. That meeting index is the duplicate.


💡 TIPS TO REMEMBER
-------------------
- Start at index 0: nothing points to 0 (values are ≥ 1), so 0 is outside the cycle.
- Do not change the array and use no extra set — that is why Floyd fits here.
- Time O(n) • Space O(1).
"""


# No ListNode here: the array itself is the linked list (index i -> nums[i]).


# ----------------------------------------------------------
# Solution
# ----------------------------------------------------------
def find_duplicate(nums):
    # Phase 1: find a meeting point inside the cycle
    slow = fast = 0
    while True:
        slow = nums[slow]               # 1 step
        fast = nums[nums[fast]]         # 2 steps
        if slow == fast:
            break

    # Phase 2: restart slow from 0; they meet at the cycle entrance
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow                         # the duplicate number


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))   # 2
    print(find_duplicate([3, 1, 3, 4, 2]))   # 3
    print(find_duplicate([3, 3, 3, 3, 3]))   # 3
