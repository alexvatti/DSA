# 7. Longest Repeating Character Replacement — LeetCode 424

🔗 **LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/
💻 **Code file:** [`7_longest_repeating_char_replacement.py`](7_longest_repeating_char_replacement.py)
🪟 **Window type:** Variable

---

## 📝 Problem

Given an uppercase string `s` and an integer `k`, you may change **at most `k`** characters to any letter. Return the length of the **longest substring of one repeated letter** you can get.

**Examples**
```
s = "ABAB",    k = 2  -> 4
s = "AABABBA", k = 1  -> 4
```

---

## 🪟 Variable Sliding Window Approach

**Key insight**
```
replacements needed = window length - (count of the most frequent letter)
```
Keep the most frequent letter, replace everything else. The window is **valid** when `replacements needed <= k`.

```
left, right -> window edges
count       -> dict {letter: frequency in window}
```

**Steps**
1. Add `s[right]` to `count`.
2. **While** `(window length - max frequency) > k` → remove `s[left]`, move `left` forward.
3. Window is valid → update the best length.

---

## 💡 Tips to Remember

- Memorize: **`(window size - max freq) <= k`**.
- `max(count.values())` scans at most 26 letters → still O(n) overall.
- Known optimization: keep a running `max_freq` that never decreases and use `if` instead of `while`.
- **Time:** O(n) • **Space:** O(1) (26 letters)

---

## 💻 Code

```python
def character_replacement(s: str, k: int) -> int:
    count = {}
    left = 0
    best = 0

    for right in range(len(s)):
        # Expand
        count[s[right]] = count.get(s[right], 0) + 1

        # Shrink while we need more than k replacements
        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

---

## ✅ Dry Run: `s = "AABABBA"`, `k = 1`

| right | char | count | window | len - maxfreq | action | best |
|-------|------|-------|--------|---------------|--------|------|
| 0 | A | A1 | `A` | 0 | ok | 1 |
| 1 | A | A2 | `AA` | 0 | ok | 2 |
| 2 | B | A2 B1 | `AAB` | 1 | ok | 3 |
| 3 | A | A3 B1 | `AABA` | 1 | ok | 4 |
| 4 | B | A3 B2 | `AABAB` | 2 > 1 | shrink twice (left → 2) | 4 |
| 5 | B | A1 B3 | `BABB` | 1 | ok | 4 |
| 6 | A | A2 B3 | `BABBA` | 2 > 1 | shrink twice (left → 4) | 4 |

Result: `4`
