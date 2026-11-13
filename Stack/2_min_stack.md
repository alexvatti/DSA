# 2. Min Stack — LeetCode 155

🔗 **LeetCode:** https://leetcode.com/problems/min-stack/
💻 **Code file:** [`2_min_stack.py`](2_min_stack.py)
🥞 **Stack type:** Stack with extra state (value, min so far)

---

## 📝 Problem

Design a stack that supports `push`, `pop`, `top` and `getMin` — every operation in **O(1)** time.

**Examples**
```
push(-2), push(0), push(-3)
getMin() -> -3
pop()
top()    -> 0
getMin() -> -2
```

---

## 🥞 Approach — Stack of pairs `(value, min_so_far)`

Every time we push, we also remember **the minimum of everything at or below this element**. The min never needs recomputing — it sits right next to the element.

```
stack -> list of (value, min of the stack up to this point)
```

**Steps**
1. `push(x)`: new min = `x` if the stack is empty, else `min(x, current min)`. Push `(x, new_min)`.
2. `pop()`: remove the top pair — the min of what remains is already stored below it.
3. `top()`: return the **value** of the top pair.
4. `getMin()`: return the **min** of the top pair.

**Why it works:** The min at any moment depends only on the elements underneath, and those never change while they stay underneath. So we can store the answer at push time.

---

## 💡 Tips to Remember

- Need an aggregate (min / max / sum) after every pop ⇒ **store it alongside each element**.
- Alternative: a second stack that only holds mins — same idea, two lists instead of pairs.
- Never scan the stack for the min — that makes `getMin` O(n).
- **Time: O(1) per operation • Space: O(n)**

---

## 💻 Code

```python
class MinStack:
    def __init__(self):
        self.stack = []  # each entry: (value, min so far)

    def push(self, val: int) -> None:
        # min of everything below, or the value itself if the stack is empty
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]
```

---

## ✅ Dry Run: `push -2, push 0, push -3, getMin, pop, top, getMin`

| op | stack after `(value, min)` | output |
|----|----------------------------|--------|
| push -2 | `(-2,-2)` | — |
| push 0 | `(-2,-2) (0,-2)` | — |
| push -3 | `(-2,-2) (0,-2) (-3,-3)` | — |
| getMin | unchanged | **-3** |
| pop | `(-2,-2) (0,-2)` | — |
| top | unchanged | **0** |
| getMin | unchanged | **-2** |

Outputs: `-3, 0, -2`
