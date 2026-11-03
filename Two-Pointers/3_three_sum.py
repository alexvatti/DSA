"""
============================================================
 3. 3SUM   (LeetCode 15)
============================================================
 Reference: https://codeanddebug.in/blog/3sum-leetcode-15/

PROBLEM
-------
Given an array, find ALL unique triplets [a, b, c] such that
a + b + c == 0. No duplicate triplets allowed.

Example:
    nums = [-1, 0, 1, 2, -1, -4]
    -> [[-1, -1, 2], [-1, 0, 1]]


TWO-POINTER APPROACH  (3Sum = sort + fix one + Two Sum)
-------------------------------------------------------
1. SORT the array first. (Sorting unlocks two pointers + easy
   duplicate skipping.)
2. Loop i from 0 to end. FIX nums[i] as the first number.
3. Now we just need TWO numbers (in the rest of the array) that
   sum to  -nums[i].  That's the "Two Sum sorted" problem!
   Use opposite-ends pointers:
       left  = i + 1
       right = last index
4. For each i:
       s = nums[i] + nums[left] + nums[right]
       s == 0  -> record triplet, then move BOTH pointers inward
                  AND skip duplicates.
       s < 0   -> move left  forward (need bigger sum)
       s > 0   -> move right backward (need smaller sum)


HANDLING DUPLICATES (the tricky part!)
--------------------------------------
- Skip duplicate `i`:     if i > 0 and nums[i] == nums[i-1]: continue
- After finding a triplet, skip duplicate left and right values.


💡 TIPS TO REMEMBER
-------------------
- 3Sum = SORT  ➜  FIX one number  ➜  Two-Sum the rest.
- Always sort first; it enables both pointers AND dedup.
- Dedup in 3 places: the outer i, the left, and the right.
- Optional speed-up: if nums[i] > 0, break (sum can't be 0).
- Time: O(n²)   Space: O(1) (ignoring output)
"""


def three_sum(nums):
    nums.sort()                 # Step 1: sort
    result = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate first numbers
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Since sorted, if the smallest is > 0, no triplet can sum to 0
        if nums[i] > 0:
            break

        # Step 3: Two-Sum on the remaining part
        left = i + 1
        right = n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1      # need a bigger sum
            else:
                right -= 1     # need a smaller sum

    return result


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))               # []
    print(three_sum([0, 0, 0]))               # [[0, 0, 0]]
