# 2. Two Sum II — Input Array Is Sorted — LeetCode 167 / 1

🔗 **LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
🔗 **Reference blog:** https://codeanddebug.in/blog/two-sum-leetcode-1/
💻 **Code file:** [`2_two_sum_sorted.py`](2_two_sum_sorted.py)

---

## 📝 Problem

Given a **sorted** array `numbers` and a `target`, find the **two numbers**
that add up to `target`. Return their **1-indexed** positions.

**Examples**
```
numbers = [2, 7, 11, 15], target = 9   ->  [1, 2]   (2 + 7 = 9)
numbers = [2, 3, 4],       target = 6   ->  [1, 3]
numbers = [-1, 0],         target = -1  ->  [1, 2]
```

---

## 👉👈 Two-Pointer Approach (opposite ends)

Because the array is **sorted**, start wide and squeeze inward:

```
left  -> smallest value (start)
right -> largest value (end)
```

**Steps**
1. `current_sum = numbers[left] + numbers[right]`.
2. If `current_sum == target` → found it → return `[left+1, right+1]`.
3. If `current_sum < target` → need a **bigger** sum → `left += 1`.
4. If `current_sum > target` → need a **smaller** sum → `right -= 1`.
5. Repeat while `left < right`.

**Why it works:** sorting means moving `left` right **increases** the sum and
moving `right` left **decreases** it — so we can steer precisely to the target.

---

## 💡 Tips to Remember

- **Sorted array + find a pair** ⇒ opposite-ends two pointers.
- Sum too **small** → move **left**. Sum too **big** → move **right**.
- Beats the hash-map approach on **space: O(1)**.
- Don't forget the `+1` for 1-based indexing.
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]   # 1-based indexing
        elif current_sum < target:
            left += 1     # need a bigger sum
        else:
            right -= 1    # need a smaller sum

    return []
```

---

## ✅ Dry Run: `[2, 7, 11, 15], target = 9`

| left | right | sum | action |
|------|-------|-----|--------|
| 0 | 3 | 2+15=17 | 17 > 9 → right-- |
| 0 | 2 | 2+11=13 | 13 > 9 → right-- |
| 0 | 1 | 2+7=9  | match → return `[1, 2]` |
