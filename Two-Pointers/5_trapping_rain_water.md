# 5. Trapping Rain Water — LeetCode 42

🔗 **LeetCode:** https://leetcode.com/problems/trapping-rain-water/
🔗 **Reference blog:** https://codeanddebug.in/blog/trapping-rain-water/
💻 **Code file:** [`5_trapping_rain_water.py`](5_trapping_rain_water.py)

---

## 📝 Problem

Given bar heights, compute how much rain water is trapped between them.

**Example**
```
height = [0,1,0,2,1,0,1,3,2,1,2,1]  ->  6
```

---

## 🔑 Key Idea

Water sitting **on top of a single bar** depends on the tallest wall to its
**left** and the tallest wall to its **right**:

```
water_on_bar = min(max_left, max_right) - height[bar]
```

The **shorter** of the two surrounding walls sets the water level, because
water would spill over the lower wall.

---

## 👉👈 Two-Pointer Approach (O(1) space)

Use opposite-ends pointers **plus** two running maxes:

```
left = 0,       right = last
left_max = 0,   right_max = 0
```

**Steps**
1. Process the **shorter** side (its wall is what limits the water, so it's safe
   to compute now).
2. If `height[left] < height[right]`:
   - update `left_max`
   - add `left_max - height[left]` to the answer
   - `left += 1`
   else (right side is shorter/equal):
   - update `right_max`
   - add `right_max - height[right]` to the answer
   - `right -= 1`
3. Repeat while `left < right`.

**Why it works:** if the left bar is shorter than the right bar, we already know
there's a wall on the right at least as tall, so the water over the left bar is
decided purely by `left_max`.

---

## 💡 Tips to Remember

- Water over a bar = **min(maxLeft, maxRight) − barHeight**.
- Two-pointer trick: always process the **shorter** side.
- Keep two running maxes: `left_max`, `right_max`.
- Sibling problem to **Container With Most Water** (same shrink idea).
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]          # new wall, no water
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]         # new wall, no water
            else:
                water += right_max - height[right]
            right -= 1

    return water
```
