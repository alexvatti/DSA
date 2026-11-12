"""
============================================================
 3. VALID SUDOKU   (LeetCode 36)
============================================================

PROBLEM
-------
Given a 9x9 board (digits '1'-'9' or '.' for empty), decide whether the
FILLED cells are valid:
    - each ROW has no repeated digit
    - each COLUMN has no repeated digit
    - each 3x3 BOX has no repeated digit
(You only validate — you do NOT need to solve the puzzle.)


HASH SET APPROACH
-----------------
Keep one set per row, per column and per box:
    rows[r]   = digits seen in row r
    cols[c]   = digits seen in column c
    boxes[b]  = digits seen in 3x3 box b

Box index:   b = (r // 3) * 3 + (c // 3)      ->  0..8

Step by step:
    1. Visit every cell once; skip '.'.
    2. If the digit is already in its row set, column set OR box set
       -> invalid -> return False.
    3. Otherwise add it to all three sets.
    4. No conflicts after all 81 cells -> True.


💡 TIPS TO REMEMBER
-------------------
- "No duplicates in a group" => HASH SET per group.
- Three groups => three collections of sets (rows, cols, boxes).
- Box formula: (r // 3) * 3 + c // 3  (or use the key (r // 3, c // 3)).
- One pass over the board is enough.
- Time: O(81) = O(1)   Space: O(81) = O(1)
"""


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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    valid = [
        list("53..7...."), list("6..195..."), list(".98....6."),
        list("8...6...3"), list("4..8.3..1"), list("7...2...6"),
        list(".6....28."), list("...419..5"), list("....8..79"),
    ]
    print(is_valid_sudoku(valid))      # True

    invalid = [row[:] for row in valid]
    invalid[0][0] = "8"                # now two 8s in the top-left box
    print(is_valid_sudoku(invalid))    # False
