"""
============================================================
 2. SEARCH A 2D MATRIX   (LeetCode 74)
============================================================
 Reference: https://codeanddebug.in/blog/search-a-2d-matrix-leetcode-74/

PROBLEM
-------
Given an m x n matrix where:
    - each row is sorted left to right, and
    - the first value of each row > last value of the previous row,
return True if target exists in the matrix, else False.

Example:
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]
    target = 3  -> True


APPROACH — treat the matrix as ONE sorted array
------------------------------------------------
Those two sorted properties mean the whole matrix behaves like a single
sorted array of length m * n. Run ONE binary search over that virtual
array and map an index back to a 2D cell:

    row = mid // cols
    col = mid % cols
    value = matrix[row][col]

Step by step:
    1. low = 0, high = rows * cols - 1.
    2. While low <= high:
    3. mid = (low + high) // 2 -> convert to (row, col).
    4. Compare matrix[row][col] with target, move low/high normally.


💡 TIPS TO REMEMBER
-------------------
- Rows sorted AND each row starts after previous ends => one flat sorted array.
- Index mapping: row = mid // cols, col = mid % cols.
- A single binary search handles everything (no separate row search).
- Time: O(log(m*n))   Space: O(1)
"""


def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = low + (high - low) // 2
        value = matrix[mid // cols][mid % cols]   # map flat index -> cell

        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    m = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]]
    print(search_matrix(m, 3))    # True
    print(search_matrix(m, 13))   # False
    print(search_matrix(m, 60))   # True
    print(search_matrix([[1]], 1))  # True
