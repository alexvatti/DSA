# 4. Find Minimum in Rotated Sorted Array — LeetCode 153

🔗 **LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
🔗 **Reference blog:** https://codeanddebug.in/blog/find-minimum-in-rotated-sorted-array/
💻 **Code file:** [`4_find_min_rotated.py`](4_find_min_rotated.py)

---

## 📝 Problem

A sorted array of **unique** numbers was rotated some unknown number of times.
Find the **minimum** element in **O(log n)**.

**Example**
```
[3, 4, 5, 1, 2]       ->  1
[4, 5, 6, 7, 0, 1, 2] ->  0
[11, 13, 15, 17]      ->  11   (no rotation)
```

---

## 🔎 Approach — find the unsorted half

The minimum is the only "pivot" point where order breaks. Compare `nums[mid]`
with `nums[high]` to know which half contains the minimum:

- If `nums[mid] > nums[high]` → the right half is **unsorted** and holds the
  minimum (pivot is to the right) → `low = mid + 1`.
- Else (`nums[mid] <= nums[high]`) → the right half is sorted, so the minimum
  is at `mid` or to its left → `high = mid`.

Loop until `low == high`, which lands on the minimum.

> Note: compare with `nums[high]` (not `nums[low]`) — it gives a clean rule.

**Steps**
1. `low = 0`, `high = n - 1`.
2. While `low < high`:
3. `mid = (low + high) // 2`.
4. If `nums[mid] > nums[high]` → `low = mid + 1`, else `high = mid`.
5. Return `nums[low]`.

---

## 💡 Tips to Remember

- Rotated sorted array ⇒ one half is always **properly sorted**.
- Compare `mid` with `high` to detect which side the pivot (min) is on.
- Use `low < high` and `high = mid` (not `mid - 1`) so you never skip the min.
- Works even with **no rotation** (already sorted).
- **Time:** O(log n) • **Space:** O(1)

---

## 💻 Code

```python
def find_min(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1     # min is in the right (unsorted) half
        else:
            high = mid        # min is at mid or to its left

    return nums[low]
```

---

## ✅ Dry Run: `[4, 5, 6, 7, 0, 1, 2]`

| low | high | mid | nums[mid] | nums[high] | action |
|-----|------|-----|-----------|------------|--------|
| 0 | 6 | 3 | 7 | 2 | 7 > 2 → low = 4 |
| 4 | 6 | 5 | 1 | 2 | 1 ≤ 2 → high = 5 |
| 4 | 5 | 4 | 0 | 1 | 0 ≤ 1 → high = 4 |
| 4 | 4 |   |   |   | low == high → return `nums[4]` = `0` |
