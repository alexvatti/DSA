# 02. Fibonacci

📌 **Pattern:** Tree recursion (2 branches) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 509 · Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
🌐 **Web page (step by step):** [`pages/02_fibonacci.html`](../pages/02_fibonacci.html)
💻 **Code file (all 4 methods):** [`code/02_fibonacci.py`](../code/02_fibonacci.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

fib(0) = 0, fib(1) = 1, and fib(n) = fib(n−1) + fib(n−2). Return fib(n).

```
fib(4) = 3
fib(5) = 5
sequence: 0 1 1 2 3 5 8 13 …
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Keep only the last two numbers (a, b) and slide forward n times. |
| 🔂 Recursion | fib(n) = fib(n−1) + fib(n−2). Two calls per call, so the calls form a tree (slow for big n, but very clear). |
| 📚 Recursion + own Stack | A stack of pending sub-problems. Pop k: if k < 2 it is a base case, add k to the total; otherwise push the two smaller problems k−1 and k−2. |
| 🧭 Own Stack + Backtracking | Two stacks: 'work' holds (k, phase) frames, 'values' holds finished answers. 'go' with k ≥ 2 leaves a 'back' frame. When we come 'back', pop two answers and push their sum. |

---

## 1. 🔁 Loop

Keep only the last two numbers (a, b) and slide forward n times.

```python
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**Flow:** `(a, b): (0,1) → (1,1) → (1,2) → (2,3) → (3,5)  ... after n steps a = fib(n)`

---

## 2. 🔂 Recursion

fib(n) = fib(n−1) + fib(n−2). Two calls per call, so the calls form a tree (slow for big n, but very clear).

```python
def fib_recursion(n):
    if n < 2:                          # base cases: fib(0)=0, fib(1)=1
        return n
    return fib_recursion(n - 1) + fib_recursion(n - 2)
```

**Calls and returns (n = 4):**
```
call   fib_recursion(4)
  call   fib_recursion(3)
    call   fib_recursion(2)
      call   fib_recursion(1)
      return 1
      call   fib_recursion(0)
      return 0
    return 1
    call   fib_recursion(1)
    return 1
  return 2
  call   fib_recursion(2)
    call   fib_recursion(1)
    return 1
    call   fib_recursion(0)
    return 0
  return 1
return 3
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

A stack of pending sub-problems. Pop k: if k < 2 it is a base case, add k to the total; otherwise push the two smaller problems k−1 and k−2.

```python
def fib_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push(n)
    total = 0
    while not stack.is_empty():
        k = stack.pop()
        if k < 2:
            total = total + k          # base case: fib(k) = k
        else:
            stack.push(k - 1)          # two smaller problems
            stack.push(k - 2)
    return total
```

**Stack operations (n = 4):**
```
push 4  pop 4  push 3  push 2
pop 2  push 1  push 0  pop 0
pop 1  pop 3  push 2  push 1
pop 1  pop 2  push 1  push 0
pop 0  pop 1
```
Result: `3`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

Two stacks: 'work' holds (k, phase) frames, 'values' holds finished answers. 'go' with k ≥ 2 leaves a 'back' frame. When we come 'back', pop two answers and push their sum.

```python
def fib_backtrack(n):
    work = Stack()                     # our own stack -> see stack_base.py
    values = Stack()                   # finished answers waiting to be combined
    work.push((n, "go"))
    while not work.is_empty():
        k, phase = work.pop()
        if phase == "go":              # ENTER
            if k < 2:
                values.push(k)         # base case: the answer is k
            else:
                work.push((k, "back"))     # combine later
                work.push((k - 2, "go"))
                work.push((k - 1, "go"))   # this one is explored first
        else:                          # "back": LEAVE, combine two answers
            values.push(values.pop() + values.pop())
    return values.pop()
```

**Stack operations (n = 4):**
```
push (4, 'go')  pop (4, 'go')  push (4, 'back')  push (2, 'go')
push (3, 'go')  pop (3, 'go')  push (3, 'back')  push (1, 'go')
push (2, 'go')  pop (2, 'go')  push (2, 'back')  push (0, 'go')
push (1, 'go')  pop (1, 'go')  push 1  pop (0, 'go')
push 0  pop (2, 'back')  pop 0  pop 1
push 1  pop (1, 'go')  push 1  pop (3, 'back')
pop 1  pop 1  push 2  pop (2, 'go')
push (2, 'back')  push (0, 'go')  push (1, 'go')  pop (1, 'go')
push 1  pop (0, 'go')  push 0  pop (2, 'back')
pop 0  pop 1  push 1  pop (4, 'back')
pop 1  pop 2  push 3  pop 3
```
Result: `3`

---

## 💡 Takeaway

Two recursive calls make a TREE. With our own stack we walk the same tree depth-first ourselves.

## 🚀 Next on LeetCode

- [LC 70 · Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
