# 6. Remove Duplicates from Sorted Array — LeetCode 26

🔗 **LeetCode:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/
🔗 **Reference blog:** https://codeanddebug.in/blog/remove-duplicates-from-sorted-array-leetcode-26/
💻 **Code file:** [`6_remove_duplicates_sorted.py`](6_remove_duplicates_sorted.py)

---

## 📝 Problem

Given a **sorted** array, remove duplicates **in place** so each element appears
once. Return the new length `k`; the first `k` elements must hold the unique
values in order.

**Example**
```
nums = [0,0,1,1,1,2,2,3,3,4]
->  k = 5, nums starts with [0,1,2,3,4,...]
```

---

## 👉👉 Two-Pointer Approach (slow & fast — same direction)

A **different** style from opposite-ends. Both pointers start on the left and
move the same way:

```
slow -> position of the last unique value locked in
fast -> scans ahead for the next NEW value
```

**Steps**
1. `slow = 0` (the first element is always unique).
2. `fast` goes from `1` to the end.
3. If `nums[fast] != nums[slow]`:
   - found a new unique value
   - `slow += 1`
   - copy it: `nums[slow] = nums[fast]`
4. If equal → duplicate → just let `fast` keep moving.
5. The unique count is `slow + 1`.

**Why it works:** the array is **sorted**, so equal values are grouped together;
checking "is it different from the last kept value?" is enough to detect dupes.

---

## 💡 Tips to Remember

- **"Modify array in place / remove items"** ⇒ slow & fast (same-direction) pointers.
- `slow` = **write** position, `fast` = **read/scan** position.
- Only advance `slow` and copy when `fast` finds a **new** value.
- Relies on the array being **sorted** (duplicates adjacent).
- Answer length = `slow + 1`.
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0  # last unique value sits here
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]   # write the new unique value

    return slow + 1
```

---

## ✅ Dry Run: `[1, 1, 2]`

| fast | nums[fast] | nums[slow] | action | array |
|------|-----------|-----------|--------|-------|
| 1 | 1 | 1 | equal → skip | [1,1,2] |
| 2 | 2 | 1 | new → slow=1, copy | [1,2,2] |

Result: `k = 2`, unique part = `[1, 2]`
