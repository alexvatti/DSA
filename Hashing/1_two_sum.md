# 1. Two Sum — LeetCode 1

🔗 **LeetCode:** https://leetcode.com/problems/two-sum/
💻 **Code file:** [`1_two_sum.py`](1_two_sum.py)

---

## 📝 Problem

Given an array `nums` and an integer `target`, return the **indices** of the two
numbers that add up to `target`. Exactly one solution exists; don't use the same
element twice.

**Examples**
```
nums = [2, 7, 11, 15], target = 9  -> [0, 1]
nums = [3, 2, 4],      target = 6  -> [1, 2]
nums = [3, 3],         target = 6  -> [0, 1]
```

---

## 🗂️ Hash Map Approach (one pass)

Brute force checks every pair (O(n²)). Instead, ask for each number:
**"have I already seen the number that completes the pair?"**

```
seen = { value : index }
```

**Steps**
1. For the current number `x`, compute `need = target - x`.
2. If `need` is in `seen` → return `[seen[need], i]`.
3. Otherwise store `seen[x] = i` and continue.

**Why it works:** when you reach the 2nd number of the pair, the 1st is already in the map.

---

## 💡 Tips to Remember

- "Find a pair summing to target" + **unsorted** ⇒ hash map. (Sorted? ⇒ two pointers.)
- Key = **value**, value = **index**.
- Check the map **before** inserting so a number never pairs with itself.
- **Time:** O(n) • **Space:** O(n)

---

## 💻 Code

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index

    for i, x in enumerate(nums):
        need = target - x          # the number that completes the pair

        if need in seen:           # O(1) lookup
            return [seen[need], i]

        seen[x] = i                # remember x for later numbers

    return []                      # (problem guarantees we never get here)
```

---

## ✅ Dry Run: `nums = [2, 7, 11, 15]`, `target = 9`

| i | x | need = 9 − x | need in seen? | seen after |
|---|---|--------------|---------------|------------|
| 0 | 2 | 7 | ❌ | `{2: 0}` |
| 1 | 7 | 2 | ✅ → return `[0, 1]` | — |

Result: `[0, 1]`
