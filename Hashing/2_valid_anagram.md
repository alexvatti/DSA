# 2. Valid Anagram — LeetCode 242

🔗 **LeetCode:** https://leetcode.com/problems/valid-anagram/
💻 **Code file:** [`2_valid_anagram.py`](2_valid_anagram.py)

---

## 📝 Problem

Given strings `s` and `t`, return `True` if `t` is an anagram of `s`
(same letters with the same counts, any order).

**Examples**
```
s = "anagram", t = "nagaram"  -> True
s = "rat",     t = "car"      -> False
```

---

## 🗂️ Hash Map Approach (frequency count)

```
count = { character : times seen }
```

**Steps**
1. Different lengths → `False` right away.
2. Walk `s`: **add 1** to `count[char]`.
3. Walk `t`: if `count[char]` is missing/0 → `False`, else **subtract 1**.
4. Finished `t` with no problem → `True`.

**Why it works:** equal length + never going below zero means every letter of `t` was matched by a letter of `s`.

---

## 💡 Tips to Remember

- "Same characters, any order" ⇒ **frequency count**.
- Check the lengths first — a free early exit.
- Only lowercase `a-z`? A fixed array of 26 ints also works.
- Sorting both strings works too, but costs O(n log n).
- **Time:** O(n) • **Space:** O(1) (bounded by alphabet size)

---

## 💻 Code

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Pass 1: count every character of s
    for c in s:
        count[c] = count.get(c, 0) + 1

    # Pass 2: "spend" those counts using t
    for c in t:
        if count.get(c, 0) == 0:   # t has a char s can't supply
            return False
        count[c] -= 1

    return True
```

---

## ✅ Dry Run: `s = "rat"`, `t = "car"`

| Phase | char | action | count |
|-------|------|--------|-------|
| s | r | +1 | `{r:1}` |
| s | a | +1 | `{r:1, a:1}` |
| s | t | +1 | `{r:1, a:1, t:1}` |
| t | c | `count['c']` is 0 → ❌ return False | — |

Result: `False`
