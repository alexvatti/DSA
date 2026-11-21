# 07. Reverse a String

📌 **Pattern:** Linear recursion (1 branch) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 344 · Reverse String](https://leetcode.com/problems/reverse-string/)
🌐 **Web page (step by step):** [`pages/07_reverse_string.html`](../pages/07_reverse_string.html)
💻 **Code file (all 4 methods):** [`code/07_reverse_string.py`](../code/07_reverse_string.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return the characters of s in reverse order.  (LC 344 asks to do it in place on a list.)

```
reverse("abc") = "cba"
reverse("hello") = "olleh"
reverse("") = ""
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Build the answer by putting each new character in FRONT of the result. |
| 🔂 Recursion | reverse(s) = reverse(everything after the first character) + the first character. |
| 📚 Recursion + own Stack | Push every character, then pop everything: last in, first out gives the reverse. |
| 🧭 Own Stack + Backtracking | 'go' walks the index forward. On 'back' the LAST index returns first, so adding s[i] builds the string reversed. |

---

## 1. 🔁 Loop

Build the answer by putting each new character in FRONT of the result.

```python
def reverse_string_loop(s):
    result = ""
    for ch in s:
        result = ch + result           # new character goes in front
    return result
```

**Flow:** `"abc":  result "" → "a" → "ba" → "cba"   (each new character goes in front)`

---

## 2. 🔂 Recursion

reverse(s) = reverse(everything after the first character) + the first character.

```python
def reverse_string_recursion(s):
    if len(s) <= 1:                    # base case
        return s
    return reverse_string_recursion(s[1:]) + s[0]
```

**Calls and returns (s = "abc"):**
```
call   reverse_string_recursion('abc')
  call   reverse_string_recursion('bc')
    call   reverse_string_recursion('c')
    return 'c'
  return 'cb'
return 'cba'
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

Push every character, then pop everything: last in, first out gives the reverse.

```python
def reverse_string_stack(s):
    stack = Stack()                    # our own stack -> see stack_base.py
    for ch in s:                       # going DOWN: push every character
        stack.push(ch)
    result = ""
    while not stack.is_empty():        # coming UP: the last character pops first
        result = result + stack.pop()
    return result
```

**Stack operations (s = "abc"):**
```
push 'a'  push 'b'  push 'c'  pop 'c'
pop 'b'  pop 'a'
```
Result: `'cba'`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

'go' walks the index forward. On 'back' the LAST index returns first, so adding s[i] builds the string reversed.

```python
def reverse_string_backtrack(s):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, "go"))
    result = ""
    while not stack.is_empty():
        i, phase = stack.pop()
        if phase == "go":              # ENTER
            if i < len(s):
                stack.push((i, "back"))
                stack.push((i + 1, "go"))
        else:                          # "back": LEAVE -> last index returns first
            result = result + s[i]
    return result
```

**Stack operations (s = "abc"):**
```
push (0, 'go')  pop (0, 'go')  push (0, 'back')  push (1, 'go')
pop (1, 'go')  push (1, 'back')  push (2, 'go')  pop (2, 'go')
push (2, 'back')  push (3, 'go')  pop (3, 'go')  pop (2, 'back')
pop (1, 'back')  pop (0, 'back')
```
Result: `'cba'`

---

## 💡 Takeaway

Last in, first out: pushing every character and popping them all IS the reverse.

## 🚀 Next on LeetCode

- Go to the next problem in the folder.
