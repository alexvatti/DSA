# 04. Reverse a Number

📌 **Pattern:** Linear recursion (1 branch) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 7 · Reverse Integer](https://leetcode.com/problems/reverse-integer/)
🌐 **Web page (step by step):** [`pages/04_reverse_number.html`](../pages/04_reverse_number.html)
💻 **Code file (all 4 methods):** [`code/04_reverse_number.py`](../code/04_reverse_number.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Reverse the digits of a non-negative integer n.  (LC 7 adds a sign and an overflow check.)

```
reverse(123) = 321
reverse(1200) = 21
reverse(7) = 7
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Peel off the last digit and append it to rev: rev = rev × 10 + digit. |
| 🔂 Recursion | Carry the answer in a parameter. When n reaches 0 the answer is ready: no work is needed on the way back. |
| 📚 Recursion + own Stack | DOWN: push the digits (the last digit goes in first). UP: the first digit pops first, so it gets place value 1, the next gets 10, and so on. |
| 🧭 Own Stack + Backtracking | On 'back' the most significant digit returns first, so give it place 1, then 10, then 100 … |

---

## 1. 🔁 Loop

Peel off the last digit and append it to rev: rev = rev × 10 + digit.

```python
def reverse_number_loop(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10        # append the last digit
        n = n // 10
    return rev
```

**Flow:** `n = 123:  rev 0 → 0×10+3 = 3 → 3×10+2 = 32 → 32×10+1 = 321`

---

## 2. 🔂 Recursion

Carry the answer in a parameter. When n reaches 0 the answer is ready: no work is needed on the way back.

```python
def reverse_number_recursion(n, rev=0):
    if n == 0:                         # base case: rev is complete
        return rev
    return reverse_number_recursion(n // 10, rev * 10 + n % 10)
```

**Calls and returns (n = 123):**
```
call   reverse_number_recursion(123, 0)
  call   reverse_number_recursion(12, 3)
    call   reverse_number_recursion(1, 32)
      call   reverse_number_recursion(0, 321)
      return 321
    return 321
  return 321
return 321
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

DOWN: push the digits (the last digit goes in first). UP: the first digit pops first, so it gets place value 1, the next gets 10, and so on.

```python
def reverse_number_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push every digit
        stack.push(n % 10)
        n = n // 10
    result = 0
    place = 1
    while not stack.is_empty():        # coming UP: the first digit comes out first
        result = result + stack.pop() * place
        place = place * 10
    return result
```

**Stack operations (n = 123):**
```
push 3  push 2  push 1  pop 1
pop 2  pop 3
```
Result: `321`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

On 'back' the most significant digit returns first, so give it place 1, then 10, then 100 …

```python
def reverse_number_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    result = 0
    place = 1
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n // 10, "go"))
        else:                          # "back": LEAVE -> first digit returns first
            result = result + (n % 10) * place
            place = place * 10
    return result
```

**Stack operations (n = 123):**
```
push (123, 'go')  pop (123, 'go')  push (123, 'back')  push (12, 'go')
pop (12, 'go')  push (12, 'back')  push (1, 'go')  pop (1, 'go')
push (1, 'back')  push (0, 'go')  pop (0, 'go')  pop (1, 'back')
pop (12, 'back')  pop (123, 'back')
```
Result: `321`

---

## 💡 Takeaway

A stack reverses order by nature (last in, first out), so reversing is its natural job.

## 🚀 Next on LeetCode

- Go to the next problem in the folder.
