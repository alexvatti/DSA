# 10. Sliding Window Maximum — LeetCode 239

🔗 **LeetCode:** https://leetcode.com/problems/sliding-window-maximum/
💻 **Code file:** [`10_sliding_window_maximum.py`](10_sliding_window_maximum.py)
🪟 **Window type:** Fixed (+ monotonic deque)

---

## 📝 Problem

Given an array `nums` and a window size `k`, the window slides from left to right one step at a time. Return the **maximum of every window**.

**Example**
```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
-> [3, 3, 5, 5, 6, 7]
```

---

## 🪟 Fixed Window + Monotonic Deque

Brute force (take the max of each window) is **O(n·k)**. Instead keep a **deque of indices** whose values are in **decreasing order**:

```
front of deque -> index of the current window's maximum
back of deque  -> newest, smaller candidates
```

**Steps** (for each index `i`)
1. If the front index is outside the window (`<= i - k`) → `popleft()`.
2. **While** the back value is **smaller** than `nums[i]` → `pop()` it (it can never be the max while `nums[i]` is in the window).
3. Append `i`.
4. Once the first window is full (`i >= k - 1`) → answer is `nums[dq[0]]`.

**Why it works:** smaller elements sitting before a bigger one are useless, so the deque stays sorted and its front is always the maximum.

---

## 💡 Tips to Remember

- "**Max/min of every window**" ⇒ monotonic deque.
- Store **indices**, not values — you need them to detect expiry.
- Each index is pushed once and popped once ⇒ O(n) total.
- **Time:** O(n) • **Space:** O(k)

---

## 💻 Code

```python
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()   # indices, values decreasing
    result = []

    for i in range(len(nums)):
        # 1. Drop the front if it slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # 2. Drop smaller values from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3. Add the current index
        dq.append(i)

        # 4. Window is full -> front is the maximum
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

---

## ✅ Dry Run: `[1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

| i | nums[i] | deque (values) | output |
|---|---------|----------------|--------|
| 0 | 1 | [1] | – |
| 1 | 3 | pop 1 → [3] | – |
| 2 | -1 | [3, -1] | **3** |
| 3 | -3 | [3, -1, -3] | **3** |
| 4 | 5 | drop 3 (expired), pop -3, -1 → [5] | **5** |
| 5 | 3 | [5, 3] | **5** |
| 6 | 6 | pop 3, 5 → [6] | **6** |
| 7 | 7 | pop 6 → [7] | **7** |

Result: `[3, 3, 5, 5, 6, 7]`
