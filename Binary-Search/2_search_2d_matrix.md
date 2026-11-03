# 2. Search a 2D Matrix — LeetCode 74

🔗 **LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/
🔗 **Reference blog:** https://codeanddebug.in/blog/search-a-2d-matrix-leetcode-74/
💻 **Code file:** [`2_search_2d_matrix.py`](2_search_2d_matrix.py)

---

## 📝 Problem

Given an `m x n` matrix where:
- Each row is sorted left → right.
- The first value of each row is greater than the last value of the previous row.

Return `True` if `target` is in the matrix, else `False`.

**Example**
```
matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3   ->  True
target = 13  ->  False
```

---

## 🔎 Approach — Treat the matrix as one sorted array

Because of the two sorted properties, the whole matrix behaves like a single
sorted array of length `m * n`. So we can run **one binary search** over the
"virtual" flattened array and map an index back to a 2D cell:

```
row = mid // n
col = mid % n
value = matrix[row][col]
```

**Steps**
1. `low = 0`, `high = m * n - 1`.
2. While `low <= high`:
3. `mid = (low + high) // 2`, convert to `(row, col)`.
4. Compare `matrix[row][col]` with `target` and move `low`/`high` like normal binary search.

---

## 💡 Tips to Remember

- Rows sorted **and** each row starts after the previous ends ⇒ one flat sorted array.
- The magic mapping: `row = mid // cols`, `col = mid % cols`.
- No need to search for the row first — a single binary search is enough.
- **Time:** O(log(m·n)) • **Space:** O(1)

---

## 💻 Code

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = low + (high - low) // 2
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
```

---

## ✅ Dry Run: target = 3 in the example matrix (cols = 4)

| low | high | mid | (row,col) | value | action |
|-----|------|-----|-----------|-------|--------|
| 0 | 11 | 5 | (1,1) | 11 | 11 > 3 → high = 4 |
| 0 | 4 | 2 | (0,2) | 5  | 5 > 3 → high = 1 |
| 0 | 1 | 0 | (0,0) | 1  | 1 < 3 → low = 1 |
| 1 | 1 | 1 | (0,1) | 3  | match → return `True` |
