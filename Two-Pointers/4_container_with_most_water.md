# 4. Container With Most Water — LeetCode 11

🔗 **LeetCode:** https://leetcode.com/problems/container-with-most-water/
💻 **Code file:** [`4_container_with_most_water.py`](4_container_with_most_water.py)

---

## 📝 Problem

Each number is the height of a vertical line. Pick **two lines** that, with the
x-axis, hold the **most water**. Return that maximum area.

**Example**
```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  ->  49
```

**Area formula**
```
area = width × min(height[left], height[right])
     = (right - left) × (shorter of the two lines)
```
Water spills over the **shorter** wall, so the short line limits the height.

---

## 👉👈 Two-Pointer Approach (opposite ends)

Start as **wide** as possible, then shrink smartly:

```
left  = 0
right = last index
```

**Steps**
1. `area = (right - left) * min(height[left], height[right])`.
2. Track the maximum area seen so far.
3. Move the pointer at the **shorter** line inward:
   - if `height[left] < height[right]` → `left += 1`
   - else → `right -= 1`
4. Repeat while `left < right`.

**Why move the shorter line?** The short line caps the height. Moving the
**taller** line can only keep or shrink the area (width drops, height still
capped). Moving the **shorter** line gives a chance at a taller wall → bigger area.

---

## 💡 Tips to Remember

- Area = **width × min(two heights)**. The **short** line decides height.
- Start at the **widest** gap (both ends).
- Always move the pointer at the **shorter** line.
- Move exactly **one** pointer per step, never both.
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        width = right - left
        current = width * min(height[left], height[right])
        best = max(best, current)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best
```

---

## 🆚 Compare with Trapping Rain Water

Both use opposite-ends pointers and the "shorter side matters" idea — but
**Container** wants ONE best pair, while **Trapping Rain Water** sums water
over every bar. Learning them together cements the pattern.
