"""
============================================================
 2. TWO SUM II — Input Array Is Sorted   (LeetCode 1 / 167)
============================================================
 Reference: https://codeanddebug.in/blog/two-sum-leetcode-1/

PROBLEM
-------
Given a SORTED array of numbers and a target, find the TWO numbers
that add up to the target. Return their positions (1-indexed).

Example:
    numbers = [2, 7, 11, 15], target = 9
    2 + 7 = 9  -> return [1, 2]


TWO-POINTER APPROACH
--------------------
Because the array is SORTED, use opposite-ends pointers:
    left  -> smallest value (start)
    right -> largest value (end)

Step by step:
    1. Compute current_sum = numbers[left] + numbers[right].
    2. If current_sum == target -> found it! Return positions.
    3. If current_sum < target  -> we need a BIGGER sum,
                                    so move LEFT forward (left += 1).
    4. If current_sum > target  -> we need a SMALLER sum,
                                    so move RIGHT backward (right -= 1).
    5. Repeat until left meets right.

Why it works: sorting means moving left increases the sum and
moving right decreases it — so we can steer toward the target.


💡 TIPS TO REMEMBER
-------------------
- SORTED array + find a PAIR => opposite-ends two pointers.
- Sum too small? move LEFT.  Sum too big? move RIGHT.
- This beats the brute-force O(n²) hash approach in space: O(1).
- Remember the +1 if the problem wants 1-indexed answers.
- Time: O(n)   Space: O(1)
"""


def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # +1 because this problem uses 1-based indexing
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1    # need a bigger sum
        else:
            right -= 1   # need a smaller sum

    return []  # no valid pair found


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))   # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))         # [1, 3]
    print(two_sum_sorted([-1, 0], -1))          # [1, 2]
