# 🗂️ Hashing — Pattern Guide

This folder teaches the **Hashing** technique through 5 classic problems.
Each file explains the **approach**, **tips to remember**, and a clean **solution** with comments.

---

## 🤔 What is Hashing?

Hashing is the go-to technique when you need **fast lookups, counting, or tracking elements**.
A hash map (Python `dict`) or hash set (Python `set`) stores items so you can find,
add or check them in **O(1)** average time — turning slow `O(n)` searches inside loops
into instant lookups.

Two main tools:
- **Hash map (`dict`)** — store elements with a property: index, frequency, running sum…
- **Hash set (`set`)** — only track *"have I seen this?"* / *"does this exist?"*

---

## 🧭 Problems in this folder (easy → harder)

| # | Problem | Tool | Notes (MD) | Code |
|---|---------|------|------------|------|
| 1 | Two Sum | Map: value → index | [notes](1_two_sum.md) | [`1_two_sum.py`](1_two_sum.py) |
| 2 | Valid Anagram | Map: char → count | [notes](2_valid_anagram.md) | [`2_valid_anagram.py`](2_valid_anagram.py) |
| 3 | Valid Sudoku | Sets: rows / cols / boxes | [notes](3_valid_sudoku.md) | [`3_valid_sudoku.py`](3_valid_sudoku.py) |
| 4 | Longest Consecutive Sequence | Set: start of runs | [notes](4_longest_consecutive_sequence.md) | [`4_longest_consecutive_sequence.py`](4_longest_consecutive_sequence.py) |
| 5 | Subarray Sum Equals K | Map: prefix sum → count | [notes](5_subarray_sum_equals_k.md) | [`5_subarray_sum_equals_k.py`](5_subarray_sum_equals_k.py) |

🔗 LeetCode: [Two Sum](https://leetcode.com/problems/two-sum/) ·
[Valid Anagram](https://leetcode.com/problems/valid-anagram/) ·
[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) ·
[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) ·
[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

NeetCode 150 list: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

---

## ✅ When to use it

- Need **O(1) lookup**
- Counting **frequency** of elements
- Checking if something **exists**

## 💡 Key idea

Use a hash map (dictionary) to store elements and their properties (index, frequency, etc.),
converting slow lookups into **O(1)** operations.

## ⚠️ Watch out for

Worst-case hash collisions — but in interviews, **average O(1)** is what matters.

---

## 🧠 Golden tips to recognize Hashing

- ✅ "Find a **pair** that sums to X" on an **unsorted** array → map of value → index.
- ✅ "**Same characters / counts**" → frequency map.
- ✅ "**No duplicates** in a group" → one set per group.
- ✅ "**Consecutive** values in O(n)" → set + start only at run beginnings.
- ✅ "**Count subarrays** with a sum" (negatives allowed) → prefix sum + frequency map.
- ✅ Goal: turn an **O(n²)** nested search into **O(n)** with one pass.

---

## 🔁 Hashing vs Two Pointers

| Situation | Pick |
|-----------|------|
| Array is **sorted**, need a pair | Two Pointers (O(1) space) |
| Array is **unsorted**, need a pair | Hashing (O(n) space) |
| Need **counts / existence** | Hashing |
| Modify array **in place** | Two Pointers |

---

## ▶️ How to run any file

```bash
python3 Hashing/1_two_sum.py
```

Every file has test cases at the bottom so you can see the output immediately.
Open `hashing.html` in a browser for the interactive visual playground.
