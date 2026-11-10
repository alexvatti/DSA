# 🪟 Sliding Window — Pattern Guide

This folder teaches the **Sliding Window** technique through 6 classic problems.
Each file explains the **approach**, **tips to remember**, and a clean **solution** with comments.

---

## 🤔 What is the Sliding Window technique?

Sliding window is one of the most frequently asked interview patterns. It works on problems
where you need to find something (**maximum, minimum, count**) inside a **contiguous subarray
or substring**.

Instead of re-checking every subarray from scratch (nested loops, O(n²) or worse), you keep a
**window** (two pointers, `left` and `right`) and **slide** it forward:

- **add** the new element entering on the right
- **remove** the old element leaving on the left

Nothing is recomputed — usually giving **O(n)** time.

### When to use it
- ✅ The problem involves a **subarray** or **substring** (contiguous!)
- ✅ You need to **optimize a brute-force** approach
- ✅ Keywords: *longest, shortest, maximum, minimum, at most K, exactly K, permutation/anagram*

---

## 🔑 Key idea

**Maintain a window and expand or shrink it based on a condition.**

### Fixed window vs variable window

| | Fixed window | Variable window |
|---|--------------|-----------------|
| Size | **Given** (e.g. size `K`) | **Changes** as you go |
| Goal | Value of every window (max, sum, match) | Smallest / largest window satisfying a condition |
| Move | Add one on the right, remove one on the left | Expand `right`; shrink `left` while invalid / valid |
| Problems here | #8, #10 | #5, #6, #7, #9 |

---

## 🧩 Templates

**Variable window — "longest" (shrink while INVALID)**
```python
left = 0
for right in range(len(arr)):
    add(arr[right])                 # expand
    while window_is_invalid():
        remove(arr[left])           # shrink
        left += 1
    best = max(best, right - left + 1)
```

**Variable window — "smallest" (shrink while VALID)**
```python
left = 0
for right in range(len(arr)):
    add(arr[right])                 # expand
    while window_is_valid():
        best = min(best, right - left + 1)
        remove(arr[left])           # shrink to find a smaller one
        left += 1
```

**Fixed window of size k**
```python
for i in range(len(arr)):
    add(arr[i])                     # new element on the right
    if i >= k:
        remove(arr[i - k])          # element that left the window
    if i >= k - 1:
        record_answer()             # window is full
```

---

## 🧭 Problems in this folder (easy → harder)

| # | Problem | Difficulty | Window type | Tracks | Notes (MD) | Code |
|---|---------|-----------|-------------|--------|------------|------|
| 5 | Longest Substring Without Repeating Characters | Medium | Variable (longest) | set | [notes](5_longest_substring_no_repeat.md) | [`5_longest_substring_no_repeat.py`](5_longest_substring_no_repeat.py) |
| 6 | Fruits Into Baskets | Medium | Variable (longest) | dict of counts | [notes](6_fruits_into_baskets.md) | [`6_fruits_into_baskets.py`](6_fruits_into_baskets.py) |
| 7 | Longest Repeating Character Replacement | Medium | Variable (longest) | dict + max freq | [notes](7_longest_repeating_char_replacement.md) | [`7_longest_repeating_char_replacement.py`](7_longest_repeating_char_replacement.py) |
| 8 | Permutation in String | Medium | Fixed (size = len(s1)) | 26-slot counts | [notes](8_permutation_in_string.md) | [`8_permutation_in_string.py`](8_permutation_in_string.py) |
| 9 | Minimum Window Substring | Hard | Variable (smallest) | two dicts + `have` | [notes](9_minimum_window_substring.md) | [`9_minimum_window_substring.py`](9_minimum_window_substring.py) |
| 10 | Sliding Window Maximum | Hard | Fixed (size = k) | monotonic deque | [notes](10_sliding_window_maximum.md) | [`10_sliding_window_maximum.py`](10_sliding_window_maximum.py) |

---

## 🧠 Golden tips to recognize Sliding Window

- ✅ **Contiguous** subarray / substring → think window.
- ✅ "**Longest** ... with at most/without ..." → variable window, shrink while **invalid**.
- ✅ "**Smallest** ... containing ..." → variable window, shrink while **valid**.
- ✅ Window **size K is given** → fixed window.
- ✅ "At most K distinct" → dict of counts + `len(dict)`.
- ✅ "Permutation / anagram" → fixed window + count comparison.
- ✅ "Max/min of each window" → monotonic deque.
- ✅ Goal: turn an **O(n²)** brute force into **O(n)**.

---

## ⚠️ Common mistakes

- Using `if` instead of `while` when shrinking (the window may need to shrink several times).
- Forgetting to **delete a dict key when its count hits 0** (breaks `len(dict)`).
- Off-by-one on window length: it is always `right - left + 1`.
- Storing values instead of **indices** in the deque (can't detect expired elements).

---

## ▶️ How to run any file

```bash
python3 Sliding-Window/5_longest_substring_no_repeat.py
```

Every file has test cases at the bottom so you can see the output immediately.
