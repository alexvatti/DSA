# 08. Numbers 1 to N  (before vs after)

📌 **Pattern:** Work BEFORE vs AFTER the call &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** no direct LeetCode problem — it is the warm-up
🌐 **Web page (step by step):** [`pages/08_numbers_1_to_n.html`](../pages/08_numbers_1_to_n.html)
💻 **Code file (all 4 methods):** [`code/08_numbers_1_to_n.py`](../code/08_numbers_1_to_n.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return the list [1, 2, …, n] in order.  The point: the work done AFTER the recursive call happens on the way back.

```
numbers(3) = [1, 2, 3]
numbers(5) = [1, 2, 3, 4, 5]
numbers(0) = []
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Loop from 1 to n and add each number. |
| 🔂 Recursion | First solve for n−1, THEN add n. The adding happens after the call returns (on the way back). |
| 📚 Recursion + own Stack | DOWN: push n, n−1, …, 1. UP: pop. The number 1 sits on top, so it comes out first. |
| 🧭 Own Stack + Backtracking | 'back' adds n. The deepest level (n = 1) comes back first, so the list is in order. |

---

## 1. 🔁 Loop

Loop from 1 to n and add each number.

```python
def numbers_loop(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result
```

**Flow:** `n = 3:  add 1 → [1] → add 2 → [1, 2] → add 3 → [1, 2, 3]`

---

## 2. 🔂 Recursion

First solve for n−1, THEN add n. The adding happens after the call returns (on the way back).

```python
def numbers_recursion(n):
    if n == 0:                         # base case: nothing to list
        return []
    return numbers_recursion(n - 1) + [n]     # add n AFTER the smaller answer
```

**Calls and returns (n = 3):**
```
call   numbers_recursion(3)
  call   numbers_recursion(2)
    call   numbers_recursion(1)
      call   numbers_recursion(0)
      return []
    return [1]
  return [1, 2]
return [1, 2, 3]
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

DOWN: push n, n−1, …, 1. UP: pop. The number 1 sits on top, so it comes out first.

```python
def numbers_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push n, n-1, ... 1
        stack.push(n)
        n = n - 1
    result = []
    while not stack.is_empty():        # coming UP: 1 comes out first
        result.append(stack.pop())
    return result
```

**Stack operations (n = 3):**
```
push 3  push 2  push 1  pop 1
pop 2  pop 3
```
Result: `[1, 2, 3]`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

'back' adds n. The deepest level (n = 1) comes back first, so the list is in order.

```python
def numbers_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = []
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n - 1, "go"))
        else:                          # "back": LEAVE -> do the work
            result.append(n)
    return result
```

**Stack operations (n = 3):**
```
push (3, 'go')  pop (3, 'go')  push (3, 'back')  push (2, 'go')
pop (2, 'go')  push (2, 'back')  push (1, 'go')  pop (1, 'go')
push (1, 'back')  push (0, 'go')  pop (0, 'go')  pop (1, 'back')
pop (2, 'back')  pop (3, 'back')
```
Result: `[1, 2, 3]`

---

## 💡 Takeaway

Work BEFORE the call = going down (gives n … 1). Work AFTER the call = coming back (gives 1 … n). Moving one line changes the order.

## 🚀 Next on LeetCode

- [LC 344 · Reverse String](https://leetcode.com/problems/reverse-string/)
