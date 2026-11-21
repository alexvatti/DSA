# 01. Factorial

📌 **Pattern:** Linear recursion (1 branch) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** no direct LeetCode problem — it is the warm-up
🌐 **Web page (step by step):** [`pages/01_factorial.html`](../pages/01_factorial.html)
💻 **Code file (all 4 methods):** [`code/01_factorial.py`](../code/01_factorial.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return n! = 1 × 2 × 3 × … × n  (and 0! = 1).

```
factorial(4) = 24
factorial(5) = 120
factorial(0) = 1
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Multiply 1 × 2 × … × n with a loop. Simple, fast, no extra memory. |
| 🔂 Recursion | n! = n × (n−1)!. Stop at the base case. Python keeps the pending multiplications on its own call stack. |
| 📚 Recursion + own Stack | Do what Python does, ourselves. Going DOWN: push every pending n. At the base case start with 1. Going UP: pop and multiply. |
| 🧭 Own Stack + Backtracking | One loop. Each stack item is (n, phase). 'go' = dive deeper and leave a 'back' note. 'back' = we are returning, do the work now. go / back = enter / leave: the template for backtracking. |

---

## 1. 🔁 Loop

Multiply 1 × 2 × … × n with a loop. Simple, fast, no extra memory.

```python
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
```

**Flow:** `n = 4:  result 1 → ×2 = 2 → ×3 = 6 → ×4 = 24`

---

## 2. 🔂 Recursion

n! = n × (n−1)!. Stop at the base case. Python keeps the pending multiplications on its own call stack.

```python
def factorial_recursion(n):
    if n <= 1:                         # base case
        return 1
    return n * factorial_recursion(n - 1)
```

**Calls and returns (n = 4):**
```
call   factorial_recursion(4)
  call   factorial_recursion(3)
    call   factorial_recursion(2)
      call   factorial_recursion(1)
      return 1
    return 2
  return 6
return 24
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

Do what Python does, ourselves. Going DOWN: push every pending n. At the base case start with 1. Going UP: pop and multiply.

```python
def factorial_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 1:                       # going DOWN: push the pending work
        stack.push(n)
        n = n - 1
    result = 1                         # base case
    while not stack.is_empty():        # coming UP: pop and finish the work
        result = result * stack.pop()
    return result
```

**Stack operations (n = 4):**
```
push 4  push 3  push 2  pop 2
pop 3  pop 4
```
Result: `24`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

One loop. Each stack item is (n, phase). 'go' = dive deeper and leave a 'back' note. 'back' = we are returning, do the work now. go / back = enter / leave: the template for backtracking.

```python
def factorial_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER this level
            if n > 1:
                stack.push((n, "back"))    # remember to come back here
                stack.push((n - 1, "go"))  # dive deeper first
        else:                          # "back": LEAVE this level
            result = result * n
    return result
```

**Stack operations (n = 4):**
```
push (4, 'go')  pop (4, 'go')  push (4, 'back')  push (3, 'go')
pop (3, 'go')  push (3, 'back')  push (2, 'go')  pop (2, 'go')
push (2, 'back')  push (1, 'go')  pop (1, 'go')  pop (2, 'back')
pop (3, 'back')  pop (4, 'back')
```
Result: `24`

---

## 💡 Takeaway

Recursion is just a stack of pending work. Going DOWN pushes the pending multiplications, coming UP pops and finishes them.

## 🚀 Next on LeetCode

- [LC 172 · Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
