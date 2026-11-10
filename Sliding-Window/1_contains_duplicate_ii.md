# 1. Contains Duplicate II — LeetCode 219

🔗 **LeetCode:** https://leetcode.com/problems/contains-duplicate-ii/
💻 **Code file:** [`1_contains_duplicate_ii.py`](1_contains_duplicate_ii.py)
🪟 **Window type:** Fixed (size `k`) — a true sliding window of indices

---

## 📝 Problem

Given an integer array `nums` and an integer `k`, return `True` if there are **two
distinct indices** `i` and `j` such that `nums[i] == nums[j]` **and** `abs(i - j) <= k`.

**Examples**
```
nums = [1,2,3,1],     k = 3  -> True   (indices 0 and 3, distance 3)
nums = [1,0,1,1],     k = 1  -> True   (indices 2 and 3, distance 1)
nums = [1,2,3,1,2,3], k = 2  -> False  (nearest repeat is distance 3)
```

---

## 🪟 Fixed Sliding Window Approach

We keep a window of **the last `k` elements** and ask: *is the new value already
inside this window?* If yes, a duplicate exists within distance `k`.

```
window -> set holding the values of the last k indices
right  -> current index
```

**Steps**
1. Move `right` forward through the array.
2. If `nums[right]` is **already in `window`** → duplicate within `k` → return `True`.
3. Add `nums[right]` to the window.
4. If the window now holds more than `k` values, **remove the element that fell off
   the left** (`nums[right - k]`).
5. Loop finishes → return `False`.

**Why it works:** the set never holds more than `k` items, so any match inside it is
guaranteed to be within distance `k`.

---

## 💡 Tips to Remember

- "Duplicate **within distance k**" ⇒ fixed window of size `k` + a set.
- Drop `nums[right - k]` the moment the window overflows — that's the "slide".
- The window answers "duplicate nearby?" without an O(n·k) double loop.
- **Time:** O(n) • **Space:** O(min(n, k))

---

## 💻 Code

```python
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    window = set()

    for right in range(len(nums)):
        # A match inside the window means distance <= k
        if nums[right] in window:
            return True

        window.add(nums[right])

        # Keep the window to at most k elements
        if len(window) > k:
            window.remove(nums[right - k])

    return False
```

---

## ✅ Dry Run: `nums = [1,2,3,1], k = 3`

| right | num | in window? | window after add | removed | window end |
|-------|-----|-----------|------------------|---------|-----------|
| 0 | 1 | no | `{1}` | — | `{1}` |
| 1 | 2 | no | `{1,2}` | — | `{1,2}` |
| 2 | 3 | no | `{1,2,3}` | — | `{1,2,3}` |
| 3 | 1 | **yes** | return `True` | — | — |

Result: `True`
