"""
============================================================
 7. MEDIAN OF TWO SORTED ARRAYS   (LeetCode 4)
============================================================
 Reference: https://codeanddebug.in/blog/median-of-two-sorted-arrays/

PROBLEM
-------
Given two sorted arrays nums1 and nums2, return the MEDIAN of the combined
sorted array in O(log(m + n)).

Example:
    nums1 = [1, 3], nums2 = [2]      -> 2.0
    nums1 = [1, 2], nums2 = [3, 4]   -> 2.5


APPROACH — binary search the PARTITION
---------------------------------------
Don't merge. Instead PARTITION both arrays so the left side holds exactly
half the total elements, with everything on the left <= everything on the right.

Binary search the SMALLER array for a cut i; the cut j is forced:
    j = half - i
At each cut:
    L1 = nums1[i-1] or -inf      R1 = nums1[i] or +inf
    L2 = nums2[j-1] or -inf      R2 = nums2[j] or +inf

    - If L1 <= R2 and L2 <= R1 -> correct partition found.
    - If L1 > R2 -> cut i too far right -> high = i - 1.
    - If L2 > R1 -> cut i too far left  -> low  = i + 1.

Median:
    - total even -> (max(L1, L2) + min(R1, R2)) / 2
    - total odd  -> max(L1, L2)


💡 TIPS TO REMEMBER
-------------------
- Always binary search the SMALLER array: O(log(min(m, n))).
- Use -inf / +inf sentinels for cuts at edges (kills edge cases).
- Correct partition: L1 <= R2 and L2 <= R1.
- half = (m + n + 1) // 2 puts the extra (odd) element on the left.
- Time: O(log(min(m, n)))   Space: O(1)
"""


def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    low, high = 0, m
    while low <= high:
        i = (low + high) // 2     # cut in nums1
        j = half - i              # cut in nums2

        L1 = nums1[i - 1] if i > 0 else float('-inf')
        R1 = nums1[i]     if i < m else float('inf')
        L2 = nums2[j - 1] if j > 0 else float('-inf')
        R2 = nums2[j]     if j < n else float('inf')

        if L1 <= R2 and L2 <= R1:
            if total % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            return float(max(L1, L2))
        elif L1 > R2:
            high = i - 1          # move cut left
        else:
            low = i + 1           # move cut right

    return 0.0  # inputs guaranteed valid; unreachable


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 3], [2]))        # 2.0
    print(find_median_sorted_arrays([1, 2], [3, 4]))     # 2.5
    print(find_median_sorted_arrays([], [1]))            # 1.0
    print(find_median_sorted_arrays([0, 0], [0, 0]))     # 0.0
    print(find_median_sorted_arrays([1, 3, 8], [7, 9, 10, 11]))  # 8.0
