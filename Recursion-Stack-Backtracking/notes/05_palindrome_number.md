# 05. Palindrome Number

📌 **Pattern:** Two-ended check &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 9 · Palindrome Number](https://leetcode.com/problems/palindrome-number/)
🌐 **Web page (step by step):** [`pages/05_palindrome_number.html`](../pages/05_palindrome_number.html)
💻 **Code file (all 4 methods):** [`code/05_palindrome_number.py`](../code/05_palindrome_number.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return True if the number reads the same forwards and backwards. Negative numbers are not palindromes.

```
121 → True
123 → False
-121 → False
1221 → True
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Two pointers on the digit string: compare the outer pair, then move inwards. |
| 🔂 Recursion | Palindrome if the outer two match AND the inside is a palindrome. Base case: fewer than 2 digits. |
| 📚 Recursion + own Stack | Push every digit. Popping gives the digits backwards, so compare each original digit with the popped one. |
| 🧭 Own Stack + Backtracking | 'go' walks the index i towards the middle. On 'back' (innermost pair first) compare s[i] with its mirror s[j]. A mismatch stops early. |

---

## 1. 🔁 Loop

Two pointers on the digit string: compare the outer pair, then move inwards.

```python
def palindrome_loop(n):
    s = str(n)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:        # outer pair differs
            return False
        left = left + 1
        right = right - 1
    return True
```

**Flow:** `"121":  left=0,right=2 → 1=1 ✓ → left=1,right=1 → stop → True`

---

## 2. 🔂 Recursion

Palindrome if the outer two match AND the inside is a palindrome. Base case: fewer than 2 digits.

```python
def palindrome_recursion(n, s=None):
    if s is None:
        s = str(n)                     # first call: number -> text
    if len(s) < 2:                     # base case: 0 or 1 digit
        return True
    if s[0] != s[-1]:                  # outer pair differs
        return False
    return palindrome_recursion(n, s[1:-1])    # check the inside
```

**Calls and returns (n = 121):**
```
call   palindrome_recursion(121, None)
  call   palindrome_recursion(121, '2')
  return True
return True
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

Push every digit. Popping gives the digits backwards, so compare each original digit with the popped one.

```python
def palindrome_stack(n):
    s = str(n)
    stack = Stack()                    # our own stack -> see stack_base.py
    for ch in s:                       # going DOWN: push every digit
        stack.push(ch)
    for ch in s:                       # coming UP: pop = the digits backwards
        if ch != stack.pop():
            return False
    return True
```

**Stack operations (n = 121):**
```
push '1'  push '2'  push '1'  pop '1'
pop '2'  pop '1'
```
Result: `True`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

'go' walks the index i towards the middle. On 'back' (innermost pair first) compare s[i] with its mirror s[j]. A mismatch stops early.

```python
def palindrome_backtrack(n):
    s = str(n)
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, "go"))
    while not stack.is_empty():
        i, phase = stack.pop()
        j = len(s) - 1 - i             # the mirror position of i
        if phase == "go":              # ENTER
            if i < j:
                stack.push((i, "back"))
                stack.push((i + 1, "go"))
        else:                          # "back": LEAVE -> compare the pair
            if s[i] != s[j]:
                return False
    return True
```

**Stack operations (n = 121):**
```
push (0, 'go')  pop (0, 'go')  push (0, 'back')  push (1, 'go')
pop (1, 'go')  pop (0, 'back')
```
Result: `True`

---

## 💡 Takeaway

A stack gives the digits backwards for free: compare "forwards" with "popped" and you are done.

## 🚀 Next on LeetCode

- [LC 125 · Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
