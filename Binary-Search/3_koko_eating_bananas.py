"""
============================================================
 3. KOKO EATING BANANAS   (LeetCode 875)
============================================================
 Reference: https://codeanddebug.in/blog/koko-eating-bananas-leetcode-875/

PROBLEM
-------
Koko has `piles` of bananas and `h` hours. Each hour she eats up to k
bananas from one pile (if a pile has fewer, she finishes it and waits the
rest of the hour). Find the MINIMUM eating speed k so she finishes all
bananas within h hours.

Example:
    piles = [3, 6, 7, 11], h = 8  -> 4


BINARY SEARCH ON THE ANSWER (not the array)
-------------------------------------------
The search space is the SPEED k, from 1 to max(piles).
Monotonicity (the key idea):
    - If speed k finishes in <= h hours, any LARGER speed also works.
    - If speed k fails, any SMALLER speed also fails.
So binary search for the smallest working speed.

Hours needed at speed k = sum(ceil(pile / k) for pile in piles)

Step by step:
    1. low = 1, high = max(piles).
    2. While low < high:
    3. mid = (low + high) // 2.
    4. If hours(mid) <= h -> mid might be the answer, try smaller: high = mid.
    5. Else -> too slow: low = mid + 1.
    6. Return low.


💡 TIPS TO REMEMBER
-------------------
- "Min/max value such that a condition holds" => binary search on ANSWER.
- Search space = range of answers (1..max(piles)), NOT indices.
- Build a monotonic feasibility check: hours(k) <= h.
- ceil(a/b) without floats: (a + b - 1) // b.
- Time: O(n * log(max pile))   Space: O(1)
"""

import math


def min_eating_speed(piles, h):
    def hours_needed(k):
        # how many hours to eat everything at speed k
        return sum(math.ceil(pile / k) for pile in piles)

    low, high = 1, max(piles)

    while low < high:
        mid = (low + high) // 2
        if hours_needed(mid) <= h:
            high = mid        # mid works, try a slower (smaller) speed
        else:
            low = mid + 1     # too slow, need a faster speed

    return low


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))        # 4
    print(min_eating_speed([30, 11, 23, 4, 20], 5))  # 30
    print(min_eating_speed([30, 11, 23, 4, 20], 6))  # 23
    print(min_eating_speed([312884470], 312884469))  # 2
