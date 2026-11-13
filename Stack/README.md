# 🥞 Stack — Pattern Guide

This folder teaches the **Stack** technique through a set of classic problems, starting from plain
bracket matching and building up to the hard monotonic-stack problem.
Each file explains the **approach**, **tips to remember**, and a clean **solution** with comments.
Open [`stack.html`](stack.html) in a browser for an interactive, step-by-step visual playground.

---

## 🤔 What is the Stack technique?

A stack is **Last-In-First-Out (LIFO)**: you only ever touch the **top**. It shines when the
**most recent unfinished item** must be handled first — matching brackets, undo-style bookkeeping,
or finding the **next greater / smaller** element.

Instead of re-scanning the array for every element (nested loops, O(n²)), each element is
**pushed once and popped once**:

- **push** an item that is still *waiting* for something
- **pop** it the moment the thing it waits for arrives, and resolve it

Nothing is revisited — usually giving **O(n)** time.

### When to use it
- ✅ Things must be **matched or closed in reverse order** (brackets, tags, nesting)
- ✅ You need the **next greater / smaller** element for each position
- ✅ You must keep an **aggregate (min / max) after every pop**
- ✅ Keywords: *valid, nested, next warmer, next greater, largest rectangle, undo*

---

## 🔑 Key idea

**Keep only the items that are still unresolved, and always resolve from the top.**

### Plain stack vs monotonic stack

| | Plain stack | Monotonic stack |
|---|-------------|-----------------|
| Order inside | Whatever order things arrive | Kept **sorted** (increasing or decreasing) |
| Pop when | Item is matched / undone | A new element **beats** the top |
| Goal | Match pairs, support O(1) queries | Next greater / smaller, spans, areas |
| Problems here | #1, #2 | #3, #4, #5 |

---

## 🧩 Templates

**Plain stack — match and pop**
```python
stack = []
for x in items:
    if is_opener(x):
        stack.append(x)                 # wait for its partner
    else:
        if not stack or not matches(stack[-1], x):
            return False
        stack.pop()                     # partner arrived
return not stack
```

**Monotonic DECREASING stack — "next greater element"**
```python
stack = []                              # indices, values decreasing
for i, x in enumerate(arr):
    while stack and x > arr[stack[-1]]:
        j = stack.pop()
        answer[j] = i - j               # j is resolved by i
    stack.append(i)
```

**Monotonic INCREASING stack — "next smaller element" / areas**
```python
stack = []                              # (start, value), values increasing
for i, x in enumerate(arr):
    start = i
    while stack and stack[-1][1] > x:
        idx, val = stack.pop()
        best = max(best, val * (i - idx))
        start = idx                     # x can stretch back this far
    stack.append((start, x))
# then flush what is left on the stack against the end of the array
```

**Stack with extra state — O(1) min / max**
```python
current_min = min(val, stack[-1][1]) if stack else val
stack.append((val, current_min))        # store the aggregate next to the value
```

---

## 🧭 Problems in this folder (easy → harder)

| # | Problem | Difficulty | Stack type | Tracks | Notes (MD) | Code |
|---|---------|-----------|------------|--------|------------|------|
| 1 | Valid Parentheses | Easy | Plain stack | stack of openers | [notes](1_valid_parentheses.md) | [`1_valid_parentheses.py`](1_valid_parentheses.py) |
| 2 | Min Stack | Medium | Stack with extra state | (value, min) pairs | [notes](2_min_stack.md) | [`2_min_stack.py`](2_min_stack.py) |
| 3 | Daily Temperatures | Medium | Monotonic decreasing stack | stack of indices | [notes](3_daily_temperatures.md) | [`3_daily_temperatures.py`](3_daily_temperatures.py) |
| 4 | Car Fleet | Medium | Monotonic stack | stack of arrival times | [notes](4_car_fleet.md) | [`4_car_fleet.py`](4_car_fleet.py) |
| 5 | Largest Rectangle in Histogram | Hard | Monotonic increasing stack | stack of (start, height) | [notes](5_largest_rectangle_histogram.md) | [`5_largest_rectangle_histogram.py`](5_largest_rectangle_histogram.py) |

---

## 🧠 Golden tips to recognize Stack

- ✅ **Nested / paired / most recent first** → plain stack.
- ✅ "**Next greater / warmer / taller**" → monotonic **decreasing** stack of indices.
- ✅ "**Next smaller** / largest rectangle" → monotonic **increasing** stack.
- ✅ "O(1) min / max after push and pop" → store the aggregate **with each element**.
- ✅ "Can't overtake / blocked by the one ahead" → sort, then a stack of the **pace-setters**.
- ✅ Goal: turn an **O(n²)** rescan into **O(n)** — every element is pushed and popped once.

---

## ⚠️ Common mistakes

- Using `if` instead of `while` when popping (one new element can resolve many waiting ones).
- Storing **values** instead of **indices** when you need distances or widths.
- Forgetting the **final check or cleanup** after the loop (`not stack`, or the leftover bars in #5).
- Calling `stack[-1]` / `pop()` on an **empty** stack — always test `stack and ...` first.
- Using `>=` where `>` is needed (equal times in #4 are *one* fleet).

---

## ▶️ How to run any file

```bash
python3 Stack/3_daily_temperatures.py
```

Every file has test cases at the bottom so you can see the output immediately.
To see the animation, open `Stack/stack.html` in your browser.
