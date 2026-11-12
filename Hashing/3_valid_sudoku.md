# 3. Valid Sudoku — LeetCode 36

🔗 **LeetCode:** https://leetcode.com/problems/valid-sudoku/
💻 **Code file:** [`3_valid_sudoku.py`](3_valid_sudoku.py)

---

## 📝 Problem

Given a 9×9 board (digits `1-9` or `.` for empty), check that the **filled** cells are valid:
each **row**, each **column** and each **3×3 box** has no repeated digit.
You only validate — you do not solve.

**Example (valid)**
```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
```
(first three rows of the standard LeetCode example)

---

## 🗂️ Hash Set Approach (one set per group)

```
rows[r]  = digits seen in row r
cols[c]  = digits seen in column c
boxes[b] = digits seen in 3×3 box b      b = (r // 3) * 3 + (c // 3)
```

**Steps**
1. Visit each cell once; skip `.`.
2. If the digit is already in its **row**, **column** or **box** set → `False`.
3. Otherwise add it to all three sets.
4. No conflict after all 81 cells → `True`.

---

## 💡 Tips to Remember

- "No duplicates in a group" ⇒ **hash set per group**.
- Three kinds of groups ⇒ three lists of 9 sets.
- Box id: `(r // 3) * 3 + c // 3` (or the tuple key `(r // 3, c // 3)`).
- One pass over the board is enough.
- **Time:** O(81) = O(1) • **Space:** O(81) = O(1)

---

## 💻 Code

```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue

            b = (r // 3) * 3 + c // 3        # which 3x3 box?

            if v in rows[r] or v in cols[c] or v in boxes[b]:
                return False                  # duplicate found

            rows[r].add(v)
            cols[c].add(v)
            boxes[b].add(v)

    return True
```

---

## ✅ Dry Run: Standard board, but `board[0][0]` changed from `5` to `8`

| Cell | digit | row set | col set | box set | verdict |
|------|-------|---------|---------|---------|---------|
| (0,0) | 8 | {} | {} | {} | add all three |
| (0,1) | 3 | {8} | {} | {8} | add |
| … | | | | | … |
| (2,2) | 8 | {9} | {} | {8,3,6,9} | 8 already in **box 0** ❌ |

Result: `False`
