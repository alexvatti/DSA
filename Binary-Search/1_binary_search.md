# 1. Binary Search — LeetCode 704

🔗 **LeetCode:** https://leetcode.com/problems/binary-search/
🔗 **Reference blog:** https://codeanddebug.in/blog/binary-search-leetcode-704/
💻 **Code file:** [`1_binary_search.py`](1_binary_search.py)

---

## 📝 Problem

Given a **sorted** array `nums` and a `target`, return the **index** of
`target` if it exists, otherwise return `-1`.

**Examples**
```
nums = [-1, 0, 3, 5, 9, 12], target = 9   ->  4
nums = [-1, 0, 3, 5, 9, 12], target = 2   -> -1
```

---

## 🔎 Binary Search Approach (search space halving)

Keep two pointers `low` and `high` bounding the search space.
Each step look at the **middle** element and throw away half:

```
low  -> start of search space
high -> end of search space
mid  -> (low + high) // 2
```

**Steps**
1. While `low <= high`:
2. Compute `mid` (use `low + (high - low) // 2` to avoid overflow in other languages).
3. If `nums[mid] == target` → return `mid`.
4. If `nums[mid] < target` → answer is on the **right** → `low = mid + 1`.
5. If `nums[mid] > target` → answer is on the **left** → `high = mid - 1`.
6. If loop ends, target is absent → return `-1`.

**Why it works:** the array is sorted, so comparing with the middle tells us
which half can possibly contain the target. We discard the other half every step.

---

## 💡 Tips to Remember

- **Sorted input + find index/value** ⇒ binary search.
- Loop condition is `low <= high` for the classic "find exact" variant.
- `mid = low + (high - low) // 2` avoids integer overflow (good habit).
- Each step halves the space ⇒ **O(log n)** time, **O(1)** space.
- This is the template every other binary-search problem builds on.

---

## 💻 Code

```python
def binary_search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1     # go right
        else:
            high = mid - 1    # go left

    return -1
```

---

## ✅ Dry Run: `[-1, 0, 3, 5, 9, 12], target = 9`

| low | high | mid | nums[mid] | action |
|-----|------|-----|-----------|--------|
| 0 | 5 | 2 | 3  | 3 < 9 → low = 3 |
| 3 | 5 | 4 | 9  | match → return `4` |
