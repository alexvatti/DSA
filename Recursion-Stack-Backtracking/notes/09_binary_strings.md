# 09. Binary Strings of Length n

📌 **Pattern:** Backtracking: choose / explore / undo &nbsp;•&nbsp; **Level:** Backtracking intro
🔗 **LeetCode:** no direct LeetCode problem — it is the warm-up
🌐 **Web page (step by step):** [`pages/09_binary_strings.html`](../pages/09_binary_strings.html)
💻 **Code file (all 4 methods):** [`code/09_binary_strings.py`](../code/09_binary_strings.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return every binary string of length n.  At each position you CHOOSE "0" or "1", EXPLORE further, then UNDO the choice.

```
binary_strings(2) = ["00", "01", "10", "11"]
binary_strings(1) = ["0", "1"]
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Start with a list holding one empty string. Repeat n times: every string gets a "0" and a "1" added. |
| 🔂 Recursion | Grow a path one character at a time. When the path has length n it is a finished answer; otherwise try "0" and try "1". |
| 📚 Recursion + own Stack | The stack holds unfinished paths. Pop a path: if complete save it, else push the path with "1" and with "0" added. |
| 🧭 Own Stack + Backtracking | ONE shared path list. 'go' = CHOOSE a character (append). A finished path is saved and undone at once. Otherwise a 'back' frame is left, so when the choices below are done we UNDO (pop). |

---

## 1. 🔁 Loop

Start with a list holding one empty string. Repeat n times: every string gets a "0" and a "1" added.

```python
def binary_strings_loop(n):
    result = [""]
    for _ in range(n):
        new_result = []
        for s in result:
            new_result.append(s + "0")
            new_result.append(s + "1")
        result = new_result
    return result
```

**Flow:** `n = 2:  ["" ] → ["0","1"] → ["00","01","10","11"]   (every old string gets "0" and "1")`

---

## 2. 🔂 Recursion

Grow a path one character at a time. When the path has length n it is a finished answer; otherwise try "0" and try "1".

```python
def binary_strings_recursion(n, path=""):
    if len(path) == n:                 # base case: a complete string
        return [path]
    return (binary_strings_recursion(n, path + "0")
            + binary_strings_recursion(n, path + "1"))
```

**Calls and returns (n = 2):**
```
call   binary_strings_recursion(2, '')
  call   binary_strings_recursion(2, '0')
    call   binary_strings_recursion(2, '00')
    return ['00']
    call   binary_strings_recursion(2, '01')
    return ['01']
  return ['00', '01']
  call   binary_strings_recursion(2, '1')
    call   binary_strings_recursion(2, '10')
    return ['10']
    call   binary_strings_recursion(2, '11')
    return ['11']
  return ['10', '11']
return ['00', '01', '10', '11']
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

The stack holds unfinished paths. Pop a path: if complete save it, else push the path with "1" and with "0" added.

```python
def binary_strings_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push("")
    result = []
    while not stack.is_empty():
        path = stack.pop()
        if len(path) == n:
            result.append(path)        # a complete string
        else:
            stack.push(path + "1")     # pushed first -> comes out last
            stack.push(path + "0")
    return result
```

**Stack operations (n = 2):**
```
push ''  pop ''  push '1'  push '0'
pop '0'  push '01'  push '00'  pop '00'
pop '01'  pop '1'  push '11'  push '10'
pop '10'  pop '11'
```
Result: `['00', '01', '10', '11']`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

ONE shared path list. 'go' = CHOOSE a character (append). A finished path is saved and undone at once. Otherwise a 'back' frame is left, so when the choices below are done we UNDO (pop).

```python
def binary_strings_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    path = []                          # the string we are building (shared)
    result = []
    stack.push(("1", "go"))            # second choice (comes out last)
    stack.push(("0", "go"))            # first choice
    while not stack.is_empty():
        choice, phase = stack.pop()
        if phase == "go":
            path.append(choice)                # CHOOSE
            if len(path) == n:
                result.append("".join(path))   # a complete string
                path.pop()                     # UNDO right away
            else:
                stack.push((choice, "back"))   # UNDO later
                stack.push(("1", "go"))        # next position: try 1 ...
                stack.push(("0", "go"))        # ... and 0 (explored first)
        else:                                  # "back": UNDO
            path.pop()
    return result
```

**Stack operations (n = 2):**
```
push ('1', 'go')  push ('0', 'go')  pop ('0', 'go')  push ('0', 'back')
push ('1', 'go')  push ('0', 'go')  pop ('0', 'go')  pop ('1', 'go')
pop ('0', 'back')  pop ('1', 'go')  push ('1', 'back')  push ('1', 'go')
push ('0', 'go')  pop ('0', 'go')  pop ('1', 'go')  pop ('1', 'back')
```
Result: `['00', '01', '10', '11']`

---

## 💡 Takeaway

This is the real backtracking pattern: choose → explore → UNDO. In method 4 the shared path list and the "back" frames do the undo.

## 🚀 Next on LeetCode

- [LC 17 · Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [LC 22 · Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
