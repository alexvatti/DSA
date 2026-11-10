# 3. Majority Element — LeetCode 169

🔗 **LeetCode:** https://leetcode.com/problems/majority-element/
💻 **Code file:** [`3_majority_element.py`](3_majority_element.py)
🪟 **Window type:** None (counting / Boyer–Moore companion problem)

---

## 📝 Problem

Given an array `nums` of size `n`, return the **majority element** — the element
that appears **more than `⌊n / 2⌋` times**. You may assume it always exists.

**Examples**
```
[3, 2, 3]             -> 3
[2, 2, 1, 1, 1, 2, 2] -> 2
```

---

## 🪟 Approach — Hash Map Count (then Boyer–Moore)

Like the window problems, we lean on a **hash map of counts** — the same tool used
to track "how many of each value is inside the window" in problems like #6 and #7.

```
counts -> dict mapping value -> how many times it has appeared
```

**Steps**
1. Walk through `nums`, incrementing `counts[num]`.
2. The moment a count passes `n // 2`, that value is the majority → return it.

### ⭐ Boyer–Moore Voting (O(1) space bonus)

Keep a `candidate` and a `count`:
- count 0 → adopt the current number as `candidate`.
- same as candidate → `count += 1`, else `count -= 1`.

Majority element survives because it outnumbers everything else combined.

---

## 💡 Tips to Remember

- "Appears more than half the time" ⇒ **counts dict** (or Boyer–Moore for O(1) space).
- A frequency dict is the same companion sliding windows use for "count of each value".
- Boyer–Moore: cancel out pairs of different elements; the majority always remains.
- **Time:** O(n) • **Space:** O(n) dict / O(1) voting

---

## 💻 Code

```python
def majority_element(nums: list[int]) -> int:
    # --- Boyer-Moore Voting: O(n) time, O(1) space ---
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num          # adopt a fresh candidate
        count += 1 if num == candidate else -1

    return candidate


def majority_element_counts(nums: list[int]) -> int:
    # --- Hash map version (easier to read) ---
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
```

---

## ✅ Dry Run (Boyer–Moore): `[2,2,1,1,1,2,2]`

| num | count before | candidate | count after |
|-----|--------------|-----------|-------------|
| 2 | 0 | 2 | 1 |
| 2 | 1 | 2 | 2 |
| 1 | 2 | 2 | 1 |
| 1 | 1 | 2 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 |
| 2 | 0 | 2 | 1 |

Result: `2`
