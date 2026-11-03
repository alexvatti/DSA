"""
============================================================
 6. REMOVE DUPLICATES FROM SORTED ARRAY   (LeetCode 26)
============================================================
 Reference:
 https://codeanddebug.in/blog/remove-duplicates-from-sorted-array-leetcode-26/

PROBLEM
-------
Given a SORTED array, remove duplicates IN PLACE so each element
appears only once. Return the new length k. The first k elements
must hold the unique values (order kept).

    nums = [0,0,1,1,1,2,2,3,3,4]
    -> k = 5, and nums starts with [0,1,2,3,4,...]


TWO-POINTER APPROACH  (SAME-direction / slow & fast)
----------------------------------------------------
This is a DIFFERENT style from opposite-ends. Both pointers
start on the left and move the same way:

    slow -> position of the LAST unique value we've locked in
    fast -> scans ahead looking for the NEXT new value

Step by step:
    1. slow = 0 (first element is always unique).
    2. fast goes from 1 to the end.
    3. If nums[fast] != nums[slow]:
          - we found a NEW unique value
          - slow += 1
          - copy it: nums[slow] = nums[fast]
    4. If they're equal, it's a duplicate -> just let fast move on.
    5. At the end, the count of unique values is slow + 1.

Because the array is SORTED, all equal values are grouped
together, so a simple "is it different from the last kept one?"
check is enough to detect duplicates.


💡 TIPS TO REMEMBER
-------------------
- "Modify array IN PLACE" => slow & fast (same-direction) pointers.
- slow = write position, fast = read/scan position.
- Only advance slow and copy when fast finds a NEW value.
- Works because the array is SORTED (duplicates are adjacent).
- Answer length = slow + 1.
- Time: O(n)   Space: O(1)
"""


def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0  # last unique value sits here

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]   # write the new unique value

    return slow + 1  # number of unique elements


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(a)
    print("Length:", k)            # 5
    print("Unique part:", a[:k])   # [0, 1, 2, 3, 4]

    b = [1, 1, 2]
    k = remove_duplicates(b)
    print("Length:", k)            # 2
    print("Unique part:", b[:k])   # [1, 2]
