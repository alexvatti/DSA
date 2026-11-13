# 1. Valid Parentheses — LeetCode 20

🔗 **LeetCode:** https://leetcode.com/problems/valid-parentheses/
💻 **Code file:** [`1_valid_parentheses.py`](1_valid_parentheses.py)
🥞 **Stack type:** Plain stack (match & pop)

---

## 📝 Problem

Given a string `s` containing only the characters `( ) [ ] { }`, return `True` if it is **valid**:
every opener is closed by the **same type**, in the **correct order**.

**Examples**
```
"()"      -> True
"()[]{}"  -> True
"(]"      -> False  (wrong type)
"([)]"    -> False  (wrong order)
```

---

## 🥞 Approach — Stack (match and pop)

The **last opener we saw must be the first one closed** — that is exactly Last-In-First-Out.

```
stack -> openers still waiting for their closer
```

**Steps**
1. Walk through each character.
2. **Opener** `( [ {` → push it.
3. **Closer** → the stack must be non-empty and its **top** must be the matching opener, then pop it. Otherwise → `False`.
4. At the end the stack must be **empty** (no unmatched opener left).

**Why it works:** A closer can only legally pair with the **most recent** unmatched opener — the top of the stack. Nesting is naturally LIFO.

---

## 💡 Tips to Remember

- Nested / paired / "most recent" things ⇒ think **stack**.
- Use a dict `closer -> opener` to avoid a long if/elif chain.
- Forgetting the final `not stack` check fails inputs like `"((("`.
- Quick reject: an odd length can never be valid.
- **Time: O(n) • Space: O(n)**

---

## 💻 Code

```python
def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in pairs:
            # Closer -> top must be its matching opener
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # Opener -> wait for its closer
            stack.append(ch)

    # Every opener must have been matched
    return not stack
```

---

## ✅ Dry Run: `{[()]}`

| char | action | stack after |
|------|--------|-------------|
| `{` | push | `{` |
| `[` | push | `{ [` |
| `(` | push | `{ [ (` |
| `)` | top is `(` ✓ → pop | `{ [` |
| `]` | top is `[` ✓ → pop | `{` |
| `}` | top is `{` ✓ → pop | empty |

Stack empty → `True`
