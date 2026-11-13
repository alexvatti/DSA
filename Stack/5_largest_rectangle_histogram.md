# 5. Largest Rectangle in Histogram — LeetCode 84

🔗 **LeetCode:** https://leetcode.com/problems/largest-rectangle-in-histogram/
💻 **Code file:** [`5_largest_rectangle_histogram.py`](5_largest_rectangle_histogram.py)
🥞 **Stack type:** Monotonic increasing stack

---

## 📝 Problem

Given an array `heights` of histogram bar heights (each bar has width 1), return the area of the
**largest rectangle** that fits inside the histogram.

**Examples**
```
[2,1,5,6,2,3] -> 10  (bars 5 and 6: height 5 x width 2)
[2,4]         -> 4
[1]           -> 1
```

---

## 🥞 Approach — Monotonic Increasing Stack of `(start, height)`

Keep bars in **increasing** height order. A bar can keep extending right until a **shorter** bar appears — then its rectangle is finished. The shorter bar **inherits the start** of everything it popped, because it can stretch back that far.

```
stack -> (start_index, height) of bars that can still extend to the right
```

**Steps**
1. For each bar `i` with height `h`, set `start = i`.
2. **While** the top is **taller** than `h`: pop `(idx, height)`, area = `height * (i - idx)`, update the best, and set `start = idx`.
3. Push `(start, h)`.
4. After the loop, every bar left can extend to the **end**: area = `height * (n - idx)`.

**Why it works:** Popping a bar is exactly when we learn its right boundary; its left boundary (`idx`) was stored when it was pushed. Each bar is pushed and popped once → **O(n)**.

---

## 💡 Tips to Remember

- "Largest rectangle / next smaller element" ⇒ **monotonic increasing stack**.
- Store the **start index** — a bar can reach further left than its own position.
- Do not forget the cleanup loop after the `for`!
- Alternative: append a `0` sentinel to `heights` and the cleanup happens automatically.
- **Time: O(n) • Space: O(n)**

---

## 💻 Code

```python
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
```

---

## ✅ Dry Run: `[2, 1, 5, 6, 2, 3]`

| i | h | pops (area) | stack after `(start,h)` | best |
|---|---|-------------|--------------------------|------|
| 0 | 2 | — | `(0,2)` | 0 |
| 1 | 1 | `(0,2)` → 2×1 = 2 | `(0,1)` | 2 |
| 2 | 5 | — | `(0,1) (2,5)` | 2 |
| 3 | 6 | — | `(0,1) (2,5) (3,6)` | 2 |
| 4 | 2 | `(3,6)` → 6×1 = 6, `(2,5)` → 5×2 = 10 | `(0,1) (2,2)` | 10 |
| 5 | 3 | — | `(0,1) (2,2) (5,3)` | 10 |
| end | — | `(5,3)` → 3, `(2,2)` → 8, `(0,1)` → 6 | empty | 10 |

Result: `10`
