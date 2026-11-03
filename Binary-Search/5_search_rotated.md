# 5. Search in Rotated Sorted Array — LeetCode 33

🔗 **LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/
🔗 **Reference blog:** https://codeanddebug.in/blog/search-in-rotated-sorted-array/
💻 **Code file:** [`5_search_rotated.py`](5_search_rotated.py)

---

## 📝 Problem

A sorted array of **unique** numbers was rotated. Given `target`, return its
**index** or `-1`, all in **O(log n)**.

**Example**
```
nums = [4, 5, 6, 7, 0, 1, 2], target = 0  ->  4
nums = [4, 5, 6, 7, 0, 1, 2], target = 3  -> -1
```

---

## 🔎 Approach — identify the sorted half each step

At any `mid`, **at least one half is sorted**. Figure out which, then check if
the target lies inside that sorted half:

1. `mid = (low + high) // 2`; if `nums[mid] == target` → return `mid`.
2. **Left half sorted** (`nums[low] <= nums[mid]`):
   - If `nums[low] <= target < nums[mid]` → target is in left → `high = mid - 1`.
   - Else → search right → `low = mid + 1`.
3. **Right half sorted** (otherwise):
   - If `nums[mid] < target <= nums[high]` → target is in right → `low = mid + 1`.
   - Else → search left → `high = mid - 1`.
4. If loop ends → return `-1`.

**Why it works:** we always narrow to the half we can reason about (the sorted
one), so we never lose the target.

---

## 💡 Tips to Remember

- Rotated + search for a value ⇒ "find the sorted half, then range-check".
- Decide sorted side with `nums[low] <= nums[mid]`.
- Use **inclusive** range checks (`<=`) with the sorted half's endpoints.
- Classic exact-match loop uses `low <= high`.
- **Time:** O(log n) • **Space:** O(1)

---

## 💻 Code

```python
def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
```

---

## ✅ Dry Run: `[4, 5, 6, 7, 0, 1, 2], target = 0`

| low | high | mid | nums[mid] | sorted half | action |
|-----|------|-----|-----------|-------------|--------|
| 0 | 6 | 3 | 7 | left (4≤7) | 0 not in [4,7) → low = 4 |
| 4 | 6 | 5 | 1 | left (0≤1) | 0 not in [0,1)? 0 is, wait target<1 and ≥0 → high = 4 |
| 4 | 4 | 4 | 0 | — | match → return `4` |
