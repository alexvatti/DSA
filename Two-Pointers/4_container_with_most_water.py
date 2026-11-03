"""
============================================================
 4. CONTAINER WITH MOST WATER   (LeetCode 11)
============================================================

PROBLEM
-------
Each number in the array is the height of a vertical line.
Pick two lines that, together with the x-axis, hold the MOST water.
Return that maximum area.

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  -> 49

Area between two lines =
    width  (distance between them)  ×  height (the SHORTER line)
Water spills over the shorter wall, so the short line limits it.


TWO-POINTER APPROACH
--------------------
Start as WIDE as possible, then shrink smartly:
    left  = 0
    right = last index

Step by step:
    1. area = (right - left) * min(height[left], height[right])
    2. Keep track of the maximum area seen so far.
    3. Move the pointer at the SHORTER line inward:
          - if height[left] < height[right]:  left  += 1
          - else:                             right -= 1
    4. Repeat until left meets right.

Why move the shorter one? The shorter line caps the height.
Moving the taller line can only keep or reduce the area (width
shrinks, height still capped by the short side). Moving the
shorter line gives a CHANCE to find a taller wall -> bigger area.


💡 TIPS TO REMEMBER
-------------------
- Area = width × min(two heights). The SHORT line decides height.
- Start at the widest gap (both ends).
- Always move the pointer at the SHORTER line.
- Never move both; move exactly one per step.
- Time: O(n)   Space: O(1)
"""


def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        width = right - left
        current = width * min(height[left], height[right])
        best = max(best, current)

        # Move the pointer at the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                         # 1
    print(max_area([4, 3, 2, 1, 4]))                # 16
