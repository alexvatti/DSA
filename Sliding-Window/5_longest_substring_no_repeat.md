# 5. Longest Substring Without Repeating Characters — LeetCode 3

🔗 **LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/
💻 **Code file:** [`5_longest_substring_no_repeat.py`](5_longest_substring_no_repeat.py)
🪟 **Window type:** Variable

---

## 📝 Problem

Given a string `s`, return the length of the **longest substring with no repeating characters**.

**Examples**
```
"abcabcbb" -> 3   ("abc")
"bbbbb"    -> 1   ("b")
"pwwkew"   -> 3   ("wke")
""         -> 0
```

---

## 🪟 Variable Sliding Window Approach

```
left  -> start of the window
right -> end of the window (moves every step)
seen  -> set of characters inside the window
```

**Steps**
1. Move `right` forward one character at a time.
2. **While** `s[right]` is already in `seen` (duplicate) → remove `s[left]` from `seen`, move `left` forward.
3. Add `s[right]` to `seen`.
4. The window is valid now → update the best length (`right - left + 1`).

**Why it works:** the window always contains unique characters. A duplicate forces us to shrink from the left just enough to remove it — never more.

---

## 💡 Tips to Remember

- "Longest substring/subarray with a condition" ⇒ **variable window**.
- Expand with `right`, shrink with a **`while`** (not `if`) when invalid.
- A **set** answers "is it inside the window?" in O(1).
- **Time:** O(n) • **Space:** O(min(n, alphabet))

---

## 💻 Code

```python
def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        # Shrink the window until the duplicate is gone
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Expand: add the new character
        seen.add(s[right])

        # Window is valid -> update the answer
        best = max(best, right - left + 1)

    return best
```

---

## ✅ Dry Run: `"abcabcbb"`

| right | char | duplicate? | left after | window | best |
|-------|------|-----------|-----------|--------|------|
| 0 | a | no | 0 | `a` | 1 |
| 1 | b | no | 0 | `ab` | 2 |
| 2 | c | no | 0 | `abc` | 3 |
| 3 | a | yes → remove `a` | 1 | `bca` | 3 |
| 4 | b | yes → remove `b` | 2 | `cab` | 3 |
| 5 | c | yes → remove `c` | 3 | `abc` | 3 |
| 6 | b | yes → remove `a`, `b` | 5 | `cb` | 3 |
| 7 | b | yes → remove `c`, `b` | 7 | `b` | 3 |

Result: `3`
