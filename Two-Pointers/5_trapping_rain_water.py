"""
============================================================
 5. TRAPPING RAIN WATER   (LeetCode 42)
============================================================
 Reference: https://codeanddebug.in/blog/trapping-rain-water/

PROBLEM
-------
Given heights of bars, compute how much rain water is trapped
between them after it rains.

    height = [0,1,0,2,1,0,1,3,2,1,2,1]  -> 6 units of water


KEY IDEA (very important!)
--------------------------
Water sitting ON TOP of any single bar depends on the TALLEST
wall to its LEFT and the TALLEST wall to its RIGHT:

    water_on_bar = min(max_left, max_right) - height[bar]

(The shorter of the two surrounding walls decides the level,
because water would spill over the lower wall.)


TWO-POINTER APPROACH (clever O(1) space version)
-------------------------------------------------
Use opposite-ends pointers PLUS two running maxes:
    left  = 0,         right = last
    left_max = 0,      right_max = 0

Step by step:
    1. Look at the shorter SIDE (because the shorter side's wall
       is the one that limits the water — we can safely compute it).
    2. If height[left] < height[right]:
         - update left_max
         - add (left_max - height[left]) to the answer
         - left += 1
       Else (right side is the shorter/equal one):
         - update right_max
         - add (right_max - height[right]) to the answer
         - right -= 1
    3. Repeat until left meets right.

Why it works: if the left bar is shorter than the right bar,
then we KNOW there is some wall on the right at least as tall,
so the water over the left bar is decided purely by left_max.


💡 TIPS TO REMEMBER
-------------------
- Water over a bar = min(maxLeft, maxRight) - barHeight.
- Two-pointer trick: always process the SHORTER side.
- Keep two running maxes (left_max, right_max).
- Compare with "Container With Most Water" — similar shrink idea.
- Time: O(n)   Space: O(1)
"""


def trap(height):
    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            # Left side is the limiting (shorter) side
            if height[left] >= left_max:
                left_max = height[left]      # new wall, no water here
            else:
                water += left_max - height[left]
            left += 1
        else:
            # Right side is the limiting (shorter/equal) side
            if height[right] >= right_max:
                right_max = height[right]    # new wall, no water here
            else:
                water += right_max - height[right]
            right -= 1

    return water


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))                      # 9
    print(trap([]))                                       # 0
