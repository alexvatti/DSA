# 3. 3Sum — LeetCode 15

🔗 **LeetCode:** https://leetcode.com/problems/3sum/
🔗 **Reference blog:** https://codeanddebug.in/blog/3sum-leetcode-15/
💻 **Code file:** [`3_three_sum.py`](3_three_sum.py)

---

## 📝 Problem

Find **all unique triplets** `[a, b, c]` in the array such that
`a + b + c == 0`. No duplicate triplets allowed.

**Example**
```
nums = [-1, 0, 1, 2, -1, -4]
->  [[-1, -1, 2], [-1, 0, 1]]
```

---

## 👉👈 Two-Pointer Approach (sort + fix one + Two Sum)

3Sum is really just **Two Sum sorted** repeated for each element.

**Steps**
1. **Sort** the array. (Unlocks two pointers + easy duplicate skipping.)
2. Loop `i` over the array. **Fix** `nums[i]` as the first number.
3. Now find two numbers in the rest that sum to `-nums[i]` using
   opposite-ends pointers:
   ```
   left  = i + 1
   right = last index
   ```
4. For each `i`:
   - `s = nums[i] + nums[left] + nums[right]`
   - `s == 0` → record triplet, move **both** pointers inward, **skip duplicates**.
   - `s < 0` → `left += 1` (need bigger sum).
   - `s > 0` → `right -= 1` (need smaller sum).

---

## ⚠️ Handling Duplicates (the tricky part)

Dedup in **three** places:
- **Outer `i`:** `if i > 0 and nums[i] == nums[i-1]: continue`
- **Left:** after a match, skip while `nums[left] == nums[left-1]`
- **Right:** after a match, skip while `nums[right] == nums[right+1]`

---

## 💡 Tips to Remember

- **3Sum = SORT ➜ FIX one ➜ Two-Sum the rest.**
- Always sort first; it enables both pointers **and** dedup.
- Dedup in 3 spots: outer `i`, `left`, `right`.
- Speed-up: if `nums[i] > 0`, you can `break` (sorted → sum can't be 0).
- **Time:** O(n²) • **Space:** O(1) (ignoring output)

---

## 💻 Code

```python
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue           # skip duplicate first number
        if nums[i] > 0:
            break              # no triplet can sum to 0 beyond this

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return result
```
