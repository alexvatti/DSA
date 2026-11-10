# 0. Contains Duplicate — LeetCode 217

🔗 **LeetCode:** https://leetcode.com/problems/contains-duplicate/
💻 **Code file:** [`0_contains_duplicate.py`](0_contains_duplicate.py)
🪟 **Window type:** None (hash-set warm-up for the window pattern)

---

## 📝 Problem

Given an integer array `nums`, return `True` if **any value appears at least twice**,
and `False` if every element is distinct.

**Examples**
```
[1, 2, 3, 1]       -> True   (1 repeats)
[1, 2, 3, 4]       -> False  (all unique)
[1, 1, 1, 3, 3, 4] -> True
```

---

## 🪟 Approach — Hash Set

This is the **gateway** problem to sliding window: it teaches the single most
important window helper — *"is this value already seen?"* in **O(1)** using a set.

```
seen -> set of numbers we have already passed
```

**Steps**
1. Walk through each number once.
2. If the number is **already in `seen`** → duplicate found → return `True`.
3. Otherwise add it to `seen`.
4. Finished the loop with no clash → return `False`.

**Why it works:** a set answers membership instantly, so one pass is enough —
exactly the lookup trick every variable window uses to keep its contents unique.

---

## 💡 Tips to Remember

- "Any duplicate?" ⇒ dump everything into a **set** and watch for a repeat.
- A set gives **O(1)** membership — the backbone of window problems like #5.
- Shortcut: `len(set(nums)) != len(nums)` answers it in one line.
- **Time:** O(n) • **Space:** O(n)

---

## 💻 Code

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        # Already inside the set -> we found a repeat
        if num in seen:
            return True
        seen.add(num)

    return False
```

---

## ✅ Dry Run: `[1, 2, 3, 1]`

| num | in seen? | action | seen after |
|-----|----------|--------|------------|
| 1 | no | add 1 | `{1}` |
| 2 | no | add 2 | `{1,2}` |
| 3 | no | add 3 | `{1,2,3}` |
| 1 | **yes** | return `True` | — |

Result: `True`
