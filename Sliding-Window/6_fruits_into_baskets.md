# 6. Fruit Into Baskets — LeetCode 904

🔗 **LeetCode:** https://leetcode.com/problems/fruit-into-baskets/
💻 **Code file:** [`6_fruits_into_baskets.py`](6_fruits_into_baskets.py)
🪟 **Window type:** Variable

---

## 📝 Problem

`fruits[i]` is the fruit type on tree `i`. You have **2 baskets**, each holding **one type** of fruit (unlimited quantity). Start at any tree and pick one fruit from every tree moving right until you can't. Return the **maximum fruits** you can pick.

**Examples**
```
[1, 2, 1]        -> 3
[0, 1, 2, 2]     -> 3   ([1, 2, 2])
[1, 2, 3, 2, 2]  -> 4   ([2, 3, 2, 2])
```

👉 In plain words: **longest subarray with at most 2 distinct values**.

---

## 🪟 Variable Sliding Window Approach

```
left, right -> window edges
count       -> dict {fruit type: how many in window}
```

**Steps**
1. Add `fruits[right]` to `count`.
2. **While** `len(count) > 2` (more than 2 types) → decrease `count[fruits[left]]`, delete the key if it hits 0, move `left` forward.
3. Window is valid → update the best length.

**Why it works:** `len(count)` is the number of distinct types in the window; we only shrink when it exceeds 2.

---

## 💡 Tips to Remember

- "**At most K distinct**" ⇒ dict of counts + `len(dict)`.
- **Delete the key at count 0**, otherwise `len()` is wrong.
- Same shape as problem 5 — only the *invalid* condition changes.
- **Time:** O(n) • **Space:** O(1) (at most 3 keys)

---

## 💻 Code

```python
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
```

---

## ✅ Dry Run: `[1, 2, 3, 2, 2]`

| right | fruit | count (after shrink) | left | window | best |
|-------|-------|----------------------|------|--------|------|
| 0 | 1 | {1:1} | 0 | [1] | 1 |
| 1 | 2 | {1:1, 2:1} | 0 | [1, 2] | 2 |
| 2 | 3 | 3 types → drop `1` → {2:1, 3:1} | 1 | [2, 3] | 2 |
| 3 | 2 | {2:2, 3:1} | 1 | [2, 3, 2] | 3 |
| 4 | 2 | {2:3, 3:1} | 1 | [2, 3, 2, 2] | 4 |

Result: `4`
