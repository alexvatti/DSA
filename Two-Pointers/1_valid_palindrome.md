# 1. Valid Palindrome — LeetCode 125

🔗 **LeetCode:** https://leetcode.com/problems/valid-palindrome/
💻 **Code file:** [`1_valid_palindrome.py`](1_valid_palindrome.py)

---

## 📝 Problem

Given a string `s`, return `True` if it reads the same forwards and backwards,
considering **only letters and numbers** and **ignoring case**.

**Examples**
```
"A man, a plan, a canal: Panama"  -> True
"race a car"                      -> False
" "                               -> True   (empty after cleaning)
```

---

## 👉👈 Two-Pointer Approach (opposite ends)

Use two pointers that start at opposite ends and move toward the center:

```
left  -> start of the string
right -> end of the string
```

**Steps**
1. Skip any character that is **not** a letter/number (use `.isalnum()`).
2. Compare `s[left]` and `s[right]` after lowercasing both.
3. If they differ → **not** a palindrome → return `False`.
4. Move `left` forward (`+1`) and `right` backward (`-1`).
5. Repeat while `left < right`.

**Why it works:** a palindrome mirrors around its center, so the 1st valid
char must match the last, the 2nd must match the 2nd-last, and so on.

---

## 💡 Tips to Remember

- "Compare **front vs back**" ⇒ opposite-ends pointers.
- Loop while `left < right`.
- Clean input on the fly with `.isalnum()` — no need to build a new string.
- Always `.lower()` before comparing.
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the two valid characters (ignore case)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

---

## ✅ Dry Run: `"0P"`

| left | right | s[left] | s[right] | equal? |
|------|-------|---------|----------|--------|
| 0 | 1 | `0` | `p` | ❌ → return False |

Result: `False`
