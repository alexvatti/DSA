# 👉👈 Two Pointers — Pattern Guide

This folder teaches the **Two Pointers** technique through 6 classic problems.
Each file explains the **approach**, **tips to remember**, and a clean **solution** with comments.

---

## 🤔 What is the Two Pointers technique?

Instead of using nested loops (slow, O(n²)), you use **two index variables**
("pointers") that move through the data smartly — usually making the solution
**O(n)** time and **O(1)** space.

The two pointers can:
- Start at **opposite ends** and move toward each other (converging), OR
- Both start at the **left** and move in the same direction (fast & slow).

---

## 🧭 Problems in this folder (easy → harder)

| # | Problem | Pointer style | Notes (MD) | Code |
|---|---------|---------------|------------|------|
| 1 | Valid Palindrome | Opposite ends | [notes](1_valid_palindrome.md) | [`1_valid_palindrome.py`](1_valid_palindrome.py) |
| 2 | Two Sum II (sorted) | Opposite ends | [notes](2_two_sum_sorted.md) | [`2_two_sum_sorted.py`](2_two_sum_sorted.py) |
| 3 | 3Sum | Fix one + opposite ends | [notes](3_three_sum.md) | [`3_three_sum.py`](3_three_sum.py) |
| 4 | Container With Most Water | Opposite ends | [notes](4_container_with_most_water.md) | [`4_container_with_most_water.py`](4_container_with_most_water.py) |
| 5 | Trapping Rain Water | Opposite ends | [notes](5_trapping_rain_water.md) | [`5_trapping_rain_water.py`](5_trapping_rain_water.py) |
| 6 | Remove Duplicates (sorted) | Same direction (slow/fast) | [notes](6_remove_duplicates_sorted.md) | [`6_remove_duplicates_sorted.py`](6_remove_duplicates_sorted.py) |

---

## 🧠 Golden tips to recognize Two Pointers

- ✅ The array is **sorted** → think opposite-ends pointers.
- ✅ You need a **pair/triplet** that meets a condition → opposite ends.
- ✅ You must **modify an array in place** / remove items → slow & fast pointers.
- ✅ You're comparing **front vs back** (palindrome, water) → opposite ends.
- ✅ Goal: turn an **O(n²)** brute force into **O(n)**.

---

## ▶️ How to run any file

```bash
python3 Two-Pointers/1_valid_palindrome.py
```

Every file has test cases at the bottom so you can see the output immediately.
