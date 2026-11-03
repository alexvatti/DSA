# 🔍 Binary Search — Pattern Guide

This folder teaches the **Binary Search** technique through 7 classic problems.
Each file explains the **approach**, **tips to remember**, and a clean **solution** with comments.

---

## 🤔 What is Binary Search really about?

Binary search is **not** just about searching in a sorted array. Its real power
is **search space reduction** — every step you throw away half of the
possibilities, giving **O(log n)** instead of O(n).

### When to use it
- The input is **sorted**, OR
- You're searching in a **monotonic space** (a condition that flips from
  false → true exactly once, i.e. increasing/decreasing feasibility).

Two flavours show up constantly:
1. **Binary search on the array** — classic "find the index/value".
2. **Binary search on the answer** — the search space is the *range of possible
   answers* (e.g. a speed, a capacity), and you test feasibility with a
   monotonic check.

---

## 🧭 Problems in this folder (easy → harder)

| # | Problem | Flavour | Notes (MD) | Code |
|---|---------|---------|------------|------|
| 1 | Binary Search | Classic on array | [notes](1_binary_search.md) | [`1_binary_search.py`](1_binary_search.py) |
| 2 | Search a 2D Matrix | Flatten + classic | [notes](2_search_2d_matrix.md) | [`2_search_2d_matrix.py`](2_search_2d_matrix.py) |
| 3 | Koko Eating Bananas | On the answer | [notes](3_koko_eating_bananas.md) | [`3_koko_eating_bananas.py`](3_koko_eating_bananas.py) |
| 4 | Find Minimum in Rotated Sorted Array | Sorted-half logic | [notes](4_find_min_rotated.md) | [`4_find_min_rotated.py`](4_find_min_rotated.py) |
| 5 | Search in Rotated Sorted Array | Sorted-half logic | [notes](5_search_rotated.md) | [`5_search_rotated.py`](5_search_rotated.py) |
| 6 | Time Based Key-Value Store | Floor / upper-bound | [notes](6_time_based_kv_store.md) | [`6_time_based_kv_store.py`](6_time_based_kv_store.py) |
| 7 | Median of Two Sorted Arrays | Partition search | [notes](7_median_two_sorted.md) | [`7_median_two_sorted.py`](7_median_two_sorted.py) |

---

## 🔗 Common problems & links

| Problem | Article | Solve | Video |
|---------|---------|-------|-------|
| Search in Rotated Sorted Array | [Read](https://codeanddebug.in/blog/search-in-rotated-sorted-array/) | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Watch](https://www.youtube.com/results?search_query=search+in+rotated+sorted+array) |
| Find Minimum in Rotated Sorted Array | [Read](https://codeanddebug.in/blog/find-minimum-in-rotated-sorted-array/) | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Watch](https://www.youtube.com/results?search_query=find+minimum+in+rotated+sorted+array) |
| Koko Eating Bananas | [Read](https://codeanddebug.in/blog/koko-eating-bananas-leetcode-875/) | [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) | – |
| Median of Two Sorted Arrays | [Read](https://codeanddebug.in/blog/median-of-two-sorted-arrays/) | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | – |
| Aggressive Cows | [Read](https://www.geeksforgeeks.org/aggressive-cows/) | [GFG](https://www.geeksforgeeks.org/problems/aggressive-cows/1) | – |
| Book Allocation Problem | [Read](https://www.geeksforgeeks.org/allocate-minimum-number-pages/) | [GFG](https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1) | – |

---

## 🧠 Golden tips to recognize Binary Search

- ✅ Input is **sorted** → classic binary search on the array.
- ✅ "Find **minimum/maximum** value such that a condition holds" → **binary
  search on the answer** (build a monotonic feasibility check).
- ✅ **Rotated** sorted array → one half is always sorted; decide which half to keep.
- ✅ "Latest value at or before X" → **floor / upper-bound** search.
- ✅ Goal: turn an **O(n)** or **O(n²)** scan into **O(log n)**.

### Loop-shape cheatsheet
- **Exact match** → `while low <= high:` and move past `mid` (`mid ± 1`).
- **Find boundary / first-true** → `while low < high:` and use `high = mid`
  (don't skip the candidate).

---

## ▶️ How to run any file

```bash
python3 Binary-Search/1_binary_search.py
```

Every file has test cases at the bottom so you can see the output immediately.
