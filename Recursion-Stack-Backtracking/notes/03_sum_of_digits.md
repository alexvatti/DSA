# 03. Sum of Digits

📌 **Pattern:** Linear recursion (1 branch) &nbsp;•&nbsp; **Level:** Basic
🔗 **LeetCode:** [LC 1281 · Subtract the Product and Sum of Digits](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)
🌐 **Web page (step by step):** [`pages/03_sum_of_digits.html`](../pages/03_sum_of_digits.html)
💻 **Code file (all 4 methods):** [`code/03_sum_of_digits.py`](../code/03_sum_of_digits.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Return the sum of the digits of a non-negative integer n.

```
sum_digits(123) = 6
sum_digits(4506) = 15
sum_digits(0) = 0
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | n % 10 is the last digit, n // 10 removes it. Repeat until n is 0, adding each digit. |
| 🔂 Recursion | sum(n) = last digit + sum(n // 10). Base case: n == 0 gives 0. |
| 📚 Recursion + own Stack | DOWN: push each digit while chopping n. UP: pop the digits and add them. |
| 🧭 Own Stack + Backtracking | (n, phase) frames. 'go' dives to n // 10 and leaves a 'back'. On 'back', add this level's digit n % 10. |

---

## 1. 🔁 Loop

n % 10 is the last digit, n // 10 removes it. Repeat until n is 0, adding each digit.

```python
def sum_digits_loop(n):
    total = 0
    while n > 0:
        total = total + n % 10         # add the last digit
        n = n // 10                    # drop the last digit
    return total
```

**Flow:** `n = 123:  total 0 → +3 = 3 → +2 = 5 → +1 = 6`

---

## 2. 🔂 Recursion

sum(n) = last digit + sum(n // 10). Base case: n == 0 gives 0.

```python
def sum_digits_recursion(n):
    if n == 0:                         # base case: no digits left
        return 0
    return n % 10 + sum_digits_recursion(n // 10)
```

**Calls and returns (n = 123):**
```
call   sum_digits_recursion(123)
  call   sum_digits_recursion(12)
    call   sum_digits_recursion(1)
      call   sum_digits_recursion(0)
      return 0
    return 1
  return 3
return 6
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

DOWN: push each digit while chopping n. UP: pop the digits and add them.

```python
def sum_digits_stack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    while n > 0:                       # going DOWN: push every digit
        stack.push(n % 10)
        n = n // 10
    total = 0
    while not stack.is_empty():        # coming UP: pop and add
        total = total + stack.pop()
    return total
```

**Stack operations (n = 123):**
```
push 3  push 2  push 1  pop 1
pop 2  pop 3
```
Result: `6`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

(n, phase) frames. 'go' dives to n // 10 and leaves a 'back'. On 'back', add this level's digit n % 10.

```python
def sum_digits_backtrack(n):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((n, "go"))
    total = 0
    while not stack.is_empty():
        n, phase = stack.pop()
        if phase == "go":              # ENTER
            if n > 0:
                stack.push((n, "back"))
                stack.push((n // 10, "go"))
        else:                          # "back": LEAVE -> do the work
            total = total + n % 10
    return total
```

**Stack operations (n = 123):**
```
push (123, 'go')  pop (123, 'go')  push (123, 'back')  push (12, 'go')
pop (12, 'go')  push (12, 'back')  push (1, 'go')  pop (1, 'go')
push (1, 'back')  push (0, 'go')  pop (0, 'go')  pop (1, 'back')
pop (12, 'back')  pop (123, 'back')
```
Result: `6`

---

## 💡 Takeaway

Same shape as factorial. Only the work changes (add instead of multiply). n % 10 = last digit, n // 10 = the rest.

## 🚀 Next on LeetCode

- [LC 258 · Add Digits](https://leetcode.com/problems/add-digits/)
