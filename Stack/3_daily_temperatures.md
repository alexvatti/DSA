# 3. Daily Temperatures — LeetCode 739

🔗 **LeetCode:** https://leetcode.com/problems/daily-temperatures/
💻 **Code file:** [`3_daily_temperatures.py`](3_daily_temperatures.py)
🥞 **Stack type:** Monotonic decreasing stack

---

## 📝 Problem

Given an array `temperatures`, return an array `answer` where `answer[i]` is the number of days
you must wait after day `i` to get a **warmer** temperature. If there is none, `answer[i] = 0`.

**Examples**
```
[73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
[30,40,50,60]             -> [1,1,1,0]
[30,60,90]                -> [1,1,0]
```

---

## 🥞 Approach — Monotonic Decreasing Stack

Keep a stack of **indices of days still waiting** for a warmer day. Their temperatures are always in **decreasing** order (that is why it is called monotonic). When today is warmer than the top, that day's wait is over.

```
stack -> indices of days waiting for a warmer day (temps decreasing)
```

**Steps**
1. For each day `i` with temperature `t`.
2. **While** the stack is non-empty and `t` is **warmer** than the day on top: pop `j` and set `answer[j] = i - j`.
3. Push `i` (it now waits for its own warmer day).
4. Days left on the stack never found one → they stay `0`.

**Why it works:** Each index is pushed once and popped at most once → **O(n)**, even though there is a `while` inside the `for`.

---

## 💡 Tips to Remember

- "Next greater / warmer / taller" ⇒ **monotonic decreasing stack** of indices.
- Store **indices**, not values — you need them to compute the distance.
- Use `while`, not `if` — one warm day can resolve several waiting days.
- Pre-fill the answer with `0` and leftovers need no extra handling.
- **Time: O(n) • Space: O(n)**

---

## 💻 Code

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []  # indices of days waiting for a warmer day

    for i, temp in enumerate(temperatures):
        # Today is warmer than the waiting days on top -> resolve them
        while stack and temp > temperatures[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer
```

---

## ✅ Dry Run: `[73, 74, 75, 71, 69, 72, 76, 73]`

| i | temp | pops (`j` → wait) | stack after (indices) |
|---|------|-------------------|-----------------------|
| 0 | 73 | — | `[0]` |
| 1 | 74 | 0 → 1 | `[1]` |
| 2 | 75 | 1 → 1 | `[2]` |
| 3 | 71 | — | `[2, 3]` |
| 4 | 69 | — | `[2, 3, 4]` |
| 5 | 72 | 4 → 1, 3 → 2 | `[2, 5]` |
| 6 | 76 | 5 → 1, 2 → 4 | `[6]` |
| 7 | 73 | — | `[6, 7]` |

Days 6 and 7 stay `0` → `[1, 1, 4, 2, 1, 1, 0, 0]`
