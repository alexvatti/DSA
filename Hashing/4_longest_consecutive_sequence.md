# 4. Longest Consecutive Sequence — LeetCode 128

🔗 **LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/
💻 **Code file:** [`4_longest_consecutive_sequence.py`](4_longest_consecutive_sequence.py)

---

## 📝 Problem

Given an **unsorted** array of integers, return the length of the longest run of
consecutive values (e.g. `1,2,3,4`). Must run in **O(n)**.

**Examples**
```
[100, 4, 200, 1, 3, 2]            -> 4   (1,2,3,4)
[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]    -> 9   (0..8)
```

---

## 🗂️ Hash Set Approach (start only at run beginnings)

Sorting is O(n log n) — too slow. Use a set for O(1) existence checks.

```
num_set = set(nums)
```

**Steps**
1. Put everything in a set (duplicates vanish).
2. For each `x`: is `x - 1` in the set?
   - **Yes** → `x` is mid-run, skip it.
   - **No** → `x` **starts** a run. Count `x+1, x+2, …` while they exist.
3. Keep the longest length.

**Why it's O(n):** each number is walked only by the run that begins before it — total walking ≤ n.

---

## 💡 Tips to Remember

- "Consecutive numbers + O(n)" ⇒ **set** + only start from run beginnings.
- The magic check: `if x - 1 not in num_set`.
- Loop over the **set**, not the list, to avoid repeat work on duplicates.
- **Time:** O(n) • **Space:** O(n)

---

## 💻 Code

```python
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0

    for x in num_set:
        if x - 1 not in num_set:          # x starts a new run
            length = 1
            while x + length in num_set:  # walk the run
                length += 1
            best = max(best, length)

    return best
```

---

## ✅ Dry Run: `nums = [100, 4, 200, 1, 3, 2]`

| x | x−1 in set? | action | run length |
|---|-------------|--------|------------|
| 100 | ❌ | start: 101? no | 1 |
| 4 | ✅ (3) | skip | — |
| 200 | ❌ | start: 201? no | 1 |
| 1 | ❌ | start: 2,3,4 ✓, 5? no | **4** |
| 3 | ✅ | skip | — |
| 2 | ✅ | skip | — |

Result: `4`
