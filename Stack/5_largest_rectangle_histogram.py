"""
============================================================
 5. LARGEST RECTANGLE IN HISTOGRAM (LeetCode 84)
============================================================

PROBLEM
-------
Given an array heights of histogram bar heights (each bar has width 1), return the area of the
largest rectangle that fits inside the histogram.

Example:
    [2,1,5,6,2,3] -> 10  (bars 5 and 6: height 5 x width 2)
    [2,4]         -> 4
    [1]           -> 1


APPROACH — MONOTONIC INCREASING STACK OF (START, HEIGHT)
--------------------------------------------------------
Keep bars in increasing height order. A bar can keep extending right until a shorter bar appears — then its rectangle is finished. The shorter bar inherits the start of everything it popped, because it can stretch back that far.

    stack -> (start_index, height) of bars that can still extend to the right

Step by step:
    1. For each bar i with height h, set start = i.
    2. While the top is taller than h: pop (idx, height), area = height * (i - idx), update the best, and set start = idx.
    3. Push (start, h).
    4. After the loop, every bar left can extend to the end: area = height * (n - idx).

Why it works: Popping a bar is exactly when we learn its right boundary; its left boundary (idx) was stored when it was pushed. Each bar is pushed and popped once → O(n).


💡 TIPS TO REMEMBER
-------------------
- "Largest rectangle / next smaller element" ⇒ monotonic increasing stack.
- Store the start index — a bar can reach further left than its own position.
- Do not forget the cleanup loop after the for!
- Alternative: append a 0 sentinel to heights and the cleanup happens automatically.
- Time: O(n)   Space: O(n)
"""


def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # (start index, height), heights increasing
    best = 0

    for i, h in enumerate(heights):
        start = i
        # A shorter bar ends every taller bar on top of the stack
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            best = max(best, height * (i - idx))
            start = idx          # the new bar can stretch back to here
        stack.append((start, h))

    # Bars left on the stack extend all the way to the end
    while stack:
        idx, height = stack.pop()
        best = max(best, height * (len(heights) - idx))

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # 10
    print(largest_rectangle_area([2, 4]))                # 4
    print(largest_rectangle_area([1]))                   # 1
    print(largest_rectangle_area([]))                    # 0
