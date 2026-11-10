# 4. Most Frequent Even Element — LeetCode 2404

🔗 **LeetCode:** https://leetcode.com/problems/most-frequent-even-element/
💻 **Code file:** [`4_most_frequent_even_element.py`](4_most_frequent_even_element.py)
🪟 **Window type:** None (frequency-map counting problem)

---

## 📝 Problem

Given an integer array `nums`, return the **most frequent even element**.
If there is a **tie**, return the **smallest** one. If there are **no even
numbers**, return `-1`.

**Examples**
```
[0,1,2,2,4,4,1] -> 2    (2 and 4 both appear twice -> pick smaller, 2)
[4,4,4,9,2,4]   -> 4    (appears 4 times)
[29,47,21]      -> -1   (no even numbers)
```

---

## 🪟 Approach — Frequency Map

Same companion skill as the sliding-window problems: a **dict of counts**. Here we
only count the **even** numbers, then pick the winner by (highest count, smallest value).

```
counts -> dict mapping even value -> how many times it appeared
```

**Steps**
1. Walk through `nums`; if a number is even, increment `counts[num]`.
2. Scan the dict to find the best element:
   - higher count wins;
   - on a tie, the **smaller value** wins.
3. If no even numbers were counted → return `-1`.

**Why it works:** counting is one pass; choosing the winner with a clear tie-break
rule guarantees the smallest among the most frequent.

---

## 💡 Tips to Remember

- "Most frequent ... (with a filter)" ⇒ **frequency dict**, then pick max by rule.
- Tie-break "smallest value" → compare `(count, -value)` or check both conditions.
- Filter first (even only) so the dict stays clean.
- **Time:** O(n) • **Space:** O(n)

---

## 💻 Code

```python
def most_frequent_even(nums: list[int]) -> int:
    counts = {}
    for num in nums:
        if num % 2 == 0:                       # only even numbers
            counts[num] = counts.get(num, 0) + 1

    if not counts:                             # no even element
        return -1

    best_val = -1
    best_count = 0
    for val, cnt in counts.items():
        # higher count wins; on a tie pick the smaller value
        if cnt > best_count or (cnt == best_count and val < best_val):
            best_val = val
            best_count = cnt

    return best_val
```

---

## ✅ Dry Run: `[0,1,2,2,4,4,1]`

Count evens → `{0:1, 2:2, 4:2}`

| val | cnt | beats best? | best_val | best_count |
|-----|-----|-------------|----------|-----------|
| 0 | 1 | yes (cnt>0) | 0 | 1 |
| 2 | 2 | yes (cnt>1) | 2 | 2 |
| 4 | 2 | tie, 4 < 2? no | 2 | 2 |

Result: `2`
