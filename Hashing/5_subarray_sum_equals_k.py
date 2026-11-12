"""
============================================================
 5. SUBARRAY SUM EQUALS K   (LeetCode 560)
============================================================

PROBLEM
-------
Given an integer array `nums` (may contain negatives) and an integer k,
return the NUMBER of contiguous subarrays whose sum equals k.

Example:
    nums = [1, 1, 1], k = 2  -> 2   ([1,1] twice)
    nums = [1, 2, 3], k = 3  -> 2   ([1,2] and [3])


WHY NOT SLIDING WINDOW?
-----------------------
Negatives break the "grow / shrink" logic, so a window can't be trusted.
Use PREFIX SUMS + a HASH MAP instead.


PREFIX SUM IDEA
---------------
    prefix[i] = nums[0] + ... + nums[i]

Sum of subarray (j+1 .. i)  =  prefix[i] - prefix[j]
We want that to equal k   =>  prefix[j] = prefix[i] - k

So at each i ask: "how many EARLIER prefixes equal prefix[i] - k?"
Each one is a valid subarray ending at i.


HASH MAP APPROACH
-----------------
    freq = { prefix_sum : how many times seen }     start: {0: 1}

Step by step:
    1. Add nums[i] to the running `prefix`.
    2. count += freq.get(prefix - k, 0)
    3. freq[prefix] += 1
    4. Return count.

The starting {0: 1} represents the empty prefix, so subarrays that
begin at index 0 are counted too.


💡 TIPS TO REMEMBER
-------------------
- "Count subarrays with sum k" (negatives allowed) => PREFIX SUM + MAP.
- Look up BEFORE inserting the current prefix.
- Never forget freq = {0: 1}.
- Time: O(n)   Space: O(n)
"""


def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    freq = {0: 1}                 # the empty prefix

    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)       # earlier prefixes that fit
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))        # 2
    print(subarray_sum([1, 2, 3], 3))        # 2
    print(subarray_sum([1, -1, 0], 0))       # 3
    print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # 4
