"""
============================================================
 6. FRUIT INTO BASKETS   (LeetCode 904)
============================================================

PROBLEM
-------
fruits[i] is the fruit type on tree i. You have 2 baskets and each
basket holds ONE type of fruit (unlimited amount). Start anywhere and
pick one fruit from every tree moving right until you can't.
Return the maximum number of fruits you can pick.

Example:
    [1, 2, 1]          -> 3
    [0, 1, 2, 2]       -> 3   ([1, 2, 2])
    [1, 2, 3, 2, 2]    -> 4   ([2, 3, 2, 2])

In other words: longest subarray with AT MOST 2 distinct values.


VARIABLE SLIDING WINDOW APPROACH
--------------------------------
    left, right -> window edges
    count       -> dict {fruit type: how many in the window}

Step by step:
    1. Add fruits[right] to `count`.
    2. While the window has MORE than 2 distinct types:
         decrease count of fruits[left]; delete it if it hits 0;
         move left forward.
    3. Window is valid -> update the best length.

Why it works: len(count) is the number of distinct types in the
window. We shrink only when it goes above 2.


💡 TIPS TO REMEMBER
-------------------
- "At most K distinct" => dict of counts + len(dict).
- Delete a key when its count reaches 0, or len() will be wrong.
- Same shape as problem 5, only the "invalid" condition changes.
- Time: O(n)   Space: O(1)  (at most 3 keys)
"""


def total_fruit(fruits: list[int]) -> int:
    count = {}
    left = 0
    best = 0

    for right in range(len(fruits)):
        # Expand: take the fruit at `right`
        count[fruits[right]] = count.get(fruits[right], 0) + 1

        # Shrink while we hold more than 2 types
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        best = max(best, right - left + 1)

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(total_fruit([1, 2, 1]))            # 3
    print(total_fruit([0, 1, 2, 2]))         # 3
    print(total_fruit([1, 2, 3, 2, 2]))      # 4
    print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5
