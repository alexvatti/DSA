# 9. Minimum Window Substring — LeetCode 76

🔗 **LeetCode:** https://leetcode.com/problems/minimum-window-substring/
💻 **Code file:** [`9_minimum_window_substring.py`](9_minimum_window_substring.py)
🪟 **Window type:** Variable

---

## 📝 Problem

Given strings `s` and `t`, return the **smallest substring of `s`** that contains every character of `t` (duplicates included). Return `""` if none exists.

**Examples**
```
s = "ADOBECODEBANC", t = "ABC"  -> "BANC"
s = "a",             t = "a"    -> "a"
s = "a",             t = "aa"   -> ""
```

---

## 🪟 Variable Sliding Window Approach

```
need     -> dict {char: required count} (from t)
window   -> dict {char: count in current window}
have     -> number of distinct chars whose requirement is met
required -> len(need)
```

**Steps**
1. **Expand** `right`: add `s[right]` to `window`. If its count now equals `need[char]` → `have += 1`.
2. **While `have == required`** (window is valid):
   - record the window if it is the smallest so far
   - remove `s[left]`; if it breaks a requirement → `have -= 1`
   - move `left` forward (try to shrink)
3. Continue until `right` reaches the end.

**Why it works:** expand until valid, then shrink as far as possible while still valid — every smallest candidate gets checked.

---

## 💡 Tips to Remember

- "**Smallest window containing …**" ⇒ expand to be valid, then shrink.
- `have` vs `required` makes the validity check **O(1)**.
- Use strict `<` when comparing lengths to keep the first best window.
- **Time:** O(n + m) • **Space:** O(m)

---

## 💻 Code

```python
def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    have = 0
    required = len(need)

    best_len = float("inf")
    best_start = 0
    left = 0

    for right in range(len(s)):
        # Expand: add the new character
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1

        # Shrink while the window is valid
        while have == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left

            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                have -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_start:best_start + best_len]
```

---

## ✅ Dry Run: `s = "ADOBECODEBANC"`, `t = "ABC"`

Key moments (indices in `s`):

| Event | Window | Valid? | Best so far |
|-------|--------|--------|-------------|
| right = 5 (`C`) | `ADOBEC` [0..5] | ✅ first valid | `ADOBEC` (6) |
| shrink: remove `A` | `DOBEC` | ❌ | `ADOBEC` |
| right = 10 (`A`) | `DOBECODEBA` [1..10] | ✅ | `ADOBEC` (10 is bigger) |
| shrink to left = 5 | `CODEBA` [5..10] | ✅ (6, not smaller) | `ADOBEC` |
| shrink: remove `C` | `ODEBA` | ❌ | `ADOBEC` |
| right = 12 (`C`) | `ODEBANC` [6..12] | ✅ | `ADOBEC` |
| shrink to left = 8 | `EBANC` | ✅ (5) | `EBANC` |
| shrink to left = 9 | `BANC` | ✅ (4) | **`BANC`** |
| shrink: remove `B` | `ANC` | ❌ | `BANC` |

Result: `"BANC"`
