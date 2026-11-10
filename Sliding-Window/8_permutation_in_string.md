# 8. Permutation in String — LeetCode 567

🔗 **LeetCode:** https://leetcode.com/problems/permutation-in-string/
💻 **Code file:** [`8_permutation_in_string.py`](8_permutation_in_string.py)
🪟 **Window type:** Fixed

---

## 📝 Problem

Given strings `s1` and `s2`, return `True` if `s2` contains a **permutation** of `s1` (some substring of `s2` is an anagram of `s1`).

**Examples**
```
s1 = "ab", s2 = "eidbaooo"  -> True   ("ba")
s1 = "ab", s2 = "eidboaoo"  -> False
```

---

## 🪟 Fixed Sliding Window Approach

A permutation has the same **length** and **letter counts** as `s1`, so the window size is **fixed** = `len(s1)`.

```
need   -> letter counts of s1            (26 slots)
window -> letter counts of current window in s2
```

**Steps**
1. Build `need` from `s1`.
2. For each `i` in `s2`: add `s2[i]` to `window`.
3. If `i >= k` → remove `s2[i - k]` (the character that left the window).
4. Once the window is full (`i >= k - 1`), compare `window == need`. Equal → `True`.

---

## 💡 Tips to Remember

- "**Permutation / anagram in a string**" ⇒ fixed window + counts.
- Fixed window = **add one on the right, remove one on the left**.
- Comparing two 26-length lists is O(26) = O(1).
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def check_inclusion(s1: str, s2: str) -> bool:
    k = len(s1)
    if k > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26

    for ch in s1:
        need[ord(ch) - ord("a")] += 1

    for i in range(len(s2)):
        # Add the new character on the right
        window[ord(s2[i]) - ord("a")] += 1

        # Remove the character that fell out on the left
        if i >= k:
            window[ord(s2[i - k]) - ord("a")] -= 1

        # Window is full-size -> compare counts
        if i >= k - 1 and window == need:
            return True

    return False
```

---

## ✅ Dry Run: `s1 = "ab"`, `s2 = "eidbaooo"` (k = 2)

| i | add | remove | window letters | equals need (`a`,`b`)? |
|---|-----|--------|----------------|------------------------|
| 0 | e | – | e | window not full yet |
| 1 | i | – | e, i | ❌ |
| 2 | d | e | i, d | ❌ |
| 3 | b | i | d, b | ❌ |
| 4 | a | d | b, a | ✅ → return True |

Result: `True`
