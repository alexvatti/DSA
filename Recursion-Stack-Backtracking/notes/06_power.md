# 06. Power  x ^ n

📌 **Pattern:** Linear recursion (1 branch) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 50 · Pow(x, n)](https://leetcode.com/problems/powx-n/)
🌐 **Web page (step by step):** [`pages/06_power.html`](../pages/06_power.html)
💻 **Code file (all 4 methods):** [`code/06_power.py`](../code/06_power.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return x raised to the power n (n ≥ 0). Here x^n = x × x × … (n times).  LC 50 also needs the halving trick: x^n = (x^(n/2))².

```
power(2, 3) = 8
power(3, 4) = 81
power(5, 0) = 1
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Multiply x into the result n times. |
| 🔂 Recursion | x^n = x × x^(n−1). Base case: x^0 = 1. |
| 📚 Recursion + own Stack | DOWN: push one x for every pending multiplication. UP: pop and multiply into the result. |
| 🧭 Own Stack + Backtracking | (n, phase) frames. Each 'back' multiplies the result by x. |

---

## 1. 🔁 Loop

Multiply x into the result n times.

```python
def power_loop(x, n):
    result = 1
    for _ in range(n):
        result = result * x
    return result
```

**Flow:** `x=2, n=3:  result 1 → ×2 = 2 → ×2 = 4 → ×2 = 8`

---

## 2. 🔂 Recursion

x^n = x × x^(n−1). Base case: x^0 = 1.

```python
def power_recursion(x, n):
    if n == 0:                         # base case
        return 1
    return x * power_recursion(x, n - 1)
```

**Calls and returns (x = 2, n = 3):**
```
call   power_recursion(2, 3)
  call   power_recursion(2, 2)
    call   power_recursion(2, 1)
      call   power_recursion(2, 0)
      return 1
    return 2
  return 4
return 8
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

DOWN: push one x for every pending multiplication. UP: pop and multiply into the result.

```python
def power_stack(x, n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: one pending multiply per step
        stack.push(x)
        n = n - 1
    result = 1                         # base case
    while not stack.is_empty():        # coming UP
        result = result * stack.pop()
    return result
```

**Stack operations (x = 2, n = 3):**
```
push 2  push 2  push 2  pop 2
pop 2  pop 2
```
Result: `8`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

(n, phase) frames. Each 'back' multiplies the result by x.

```python
def power_backtrack(x, n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n - 1, "go"))
        else:                          # "back": LEAVE -> do the work
            result = result * x
    return result
```

**Stack operations (x = 2, n = 3):**
```
push (3, 'go')  pop (3, 'go')  push (3, 'back')  push (2, 'go')
pop (2, 'go')  push (2, 'back')  push (1, 'go')  pop (1, 'go')
push (1, 'back')  push (0, 'go')  pop (0, 'go')  pop (1, 'back')
pop (2, 'back')  pop (3, 'back')
```
Result: `8`

---

## 💡 Takeaway

The count n drives the depth. Once this is easy, the halving trick (n // 2) is a one-line change for LC 50.

## 🚀 Next on LeetCode

- Go to the next problem in the folder.
