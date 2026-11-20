# 5. Find the Duplicate Number — LeetCode 287

🔗 **LeetCode:** https://leetcode.com/problems/find-the-duplicate-number/
💻 **Code file:** [`5_find_the_duplicate_number.py`](5_find_the_duplicate_number.py)
🔗 **Pattern:** 🐢🐇 Floyd on an Array

---

## 📝 Problem

Given an array nums of n + 1 integers, each in the range [1, n], exactly one number is repeated. Return it WITHOUT modifying the array and using only O(1) extra space.

**Examples**
```
[1, 3, 4, 2, 2]   =>  2
[3, 1, 3, 4, 2]   =>  3
[3, 3, 3, 3, 3]   =>  3
```

---

## ✅ When to use it

- Values are in `1..n` in an array of `n + 1`, so `nums[i]` works as a **next pointer**
- The array must not change and extra space must be **O(1)**
- 🔍 Keywords: *find the duplicate, 1..n, cannot modify, constant space*

---

## 🔗 Approach — Floyd on an Array

An array of `n + 1` numbers in `1..n` is secretly a **linked list**: index `i` points to `nums[i]`. Two indexes hold the same value, so two nodes point to one node → a **cycle**, and the cycle entrance is the duplicate. Use slow & fast to get into the cycle, then find the entrance.

**Steps**
1. Phase 1: `slow = nums[slow]`, `fast = nums[nums[fast]]` until they meet (inside the cycle).
2. Phase 2: put `slow` back at `0`; keep `fast` at the meeting point.
3. Move both **one** step at a time until they meet again.
4. That meeting index is the **duplicate**.

---

## 💡 Tips to Remember

- Start at index `0`: nothing points to `0` (values are ≥ 1), so `0` is outside the cycle.
- Do not change the array and use no extra set — that is why Floyd fits here.
- Time **O(n)** • Space **O(1)**.

---

## 💻 Code

```python
def find_duplicate(nums):
    # Phase 1: find a meeting point inside the cycle
    slow = fast = 0
    while True:
        slow = nums[slow]               # 1 step
        fast = nums[nums[fast]]         # 2 steps
        if slow == fast:
            break

    # Phase 2: restart slow from 0; they meet at the cycle entrance
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow                         # the duplicate number
```

---

## ✅ Dry run on `nums = [1, 3, 4, 2, 2]` (node `i` points to `nums[i]`):

| phase | slow | fast |
|-------|------|------|
| start | 0 | 0 |
| 1 | 1 | 3 |
| 1 | 3 | 4 |
| 1 | 2 | 4 |
| 1 | 4 | 4 ← meet |
| 2 restart | 0 | 4 |
| 2 | 1 | 2 |
| 2 | 3 | 4 |
| 2 | 2 | 2 ← meet |

The cycle entrance is `2` → the duplicate is `2`
