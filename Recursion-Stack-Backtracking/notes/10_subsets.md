# 10. Subsets

📌 **Pattern:** Backtracking: choose / explore / undo &nbsp;•&nbsp; **Level:** LeetCode 78 · Medium
🔗 **LeetCode:** [LC 78 · Subsets](https://leetcode.com/problems/subsets/)
🌐 **Web page (step by step):** [`pages/10_subsets.html`](../pages/10_subsets.html)
💻 **Code file (all 4 methods):** [`code/10_subsets.py`](../code/10_subsets.py)
📦 **Our stack:** methods 3 and 4 use `Stack` → [`code/stack_base.py`](../code/stack_base.py)

---

## 📝 Problem

Given a list of distinct numbers, return all possible subsets (the power set).

```
subsets([1, 2]) = [[], [1], [2], [1, 2]]
subsets([1, 2, 3]) has 8 subsets
```

## 🧭 The 4 methods at a glance

| Method | Idea |
|--------|------|
| 🔁 Loop | Start with [[]]. For every number, copy all subsets found so far and add the number to each copy. |
| 🔂 Recursion | For each number there are two choices: SKIP it or TAKE it. When all numbers are decided, the path is a subset. |
| 📚 Recursion + own Stack | The stack holds (i, path) pairs: "numbers decided so far" and "what I picked". Pop one; if every number is decided save it, else push TAKE and SKIP. |
| 🧭 Own Stack + Backtracking | The LeetCode template. ONE shared path. 'go' j = CHOOSE nums[j] (append), record the path, leave a 'back' frame, then push the next choices. 'back' = UNDO (pop). |

---

## 1. 🔁 Loop

Start with [[]]. For every number, copy all subsets found so far and add the number to each copy.

```python
def subsets_loop(nums):
    result = [[]]
    for x in nums:
        for i in range(len(result)):
            result.append(result[i] + [x])     # copy an old subset + x
    return result
```

**Flow:** `[1,2]:  [[]] → add 1 to each → [[],[1]] → add 2 to each → [[],[1],[2],[1,2]]`

---

## 2. 🔂 Recursion

For each number there are two choices: SKIP it or TAKE it. When all numbers are decided, the path is a subset.

```python
def subsets_recursion(nums, i=0, path=()):
    if i == len(nums):                 # base case: every number decided
        return [list(path)]
    skip = subsets_recursion(nums, i + 1, path)
    take = subsets_recursion(nums, i + 1, path + (nums[i],))
    return skip + take
```

**Calls and returns (nums = [1, 2]):**
```
call   subsets_recursion([1, 2], 0, ())
  call   subsets_recursion([1, 2], 1, ())
    call   subsets_recursion([1, 2], 2, ())
    return [[]]
    call   subsets_recursion([1, 2], 2, (2,))
    return [[2]]
  return [[], [2]]
  call   subsets_recursion([1, 2], 1, (1,))
    call   subsets_recursion([1, 2], 2, (1,))
    return [[1]]
    call   subsets_recursion([1, 2], 2, (1, 2))
    return [[1, 2]]
  return [[1], [1, 2]]
return [[], [2], [1], [1, 2]]
```

---

## 3. 📚 Recursion + own Stack

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

The stack holds (i, path) pairs: "numbers decided so far" and "what I picked". Pop one; if every number is decided save it, else push TAKE and SKIP.

```python
def subsets_stack(nums):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, []))
    result = []
    while not stack.is_empty():
        i, path = stack.pop()
        if i == len(nums):
            result.append(path)                    # every number decided
        else:
            stack.push((i + 1, path + [nums[i]]))  # TAKE nums[i]
            stack.push((i + 1, path))              # SKIP nums[i]
    return result
```

**Stack operations (nums = [1, 2]):**
```
push (0, [])  pop (0, [])  push (1, [1])  push (1, [])
pop (1, [])  push (2, [2])  push (2, [])  pop (2, [])
pop (2, [2])  pop (1, [1])  push (2, [1, 2])  push (2, [1])
pop (2, [1])  pop (2, [1, 2])
```
Result: `[[], [2], [1], [1, 2]]`

---

## 4. 🧭 Own Stack + Backtracking

> 📦 Uses **our own Stack** — see [`stack_base.py`](../code/stack_base.py) (`push`, `pop`, `is_empty`).

The LeetCode template. ONE shared path. 'go' j = CHOOSE nums[j] (append), record the path, leave a 'back' frame, then push the next choices. 'back' = UNDO (pop).

```python
def subsets_backtrack(nums):
    stack = Stack()                    # our own stack -> see stack_base.py
    path = []                          # the subset we are building (shared)
    result = [[]]                      # the empty subset
    for j in range(len(nums) - 1, -1, -1):
        stack.push((j, "go"))          # first choices
    while not stack.is_empty():
        j, phase = stack.pop()
        if phase == "go":
            path.append(nums[j])                   # CHOOSE
            result.append(path[:])                 # every path is a subset
            stack.push((j, "back"))                # UNDO later
            for k in range(len(nums) - 1, j, -1):
                stack.push((k, "go"))              # choices after j
        else:                                      # "back": UNDO
            path.pop()
    return result
```

**Stack operations (nums = [1, 2]):**
```
push (1, 'go')  push (0, 'go')  pop (0, 'go')  push (0, 'back')
push (1, 'go')  pop (1, 'go')  push (1, 'back')  pop (1, 'back')
pop (0, 'back')  pop (1, 'go')  push (1, 'back')  pop (1, 'back')
```
Result: `[[], [1], [1, 2], [2]]`

---

## 💡 Takeaway

Every LeetCode backtracking problem is this loop: choose → record → explore → UNDO. With your own stack, "back" frames do the undo.

## 🚀 Next on LeetCode

- [LC 46 · Permutations](https://leetcode.com/problems/permutations/)
- [LC 39 · Combination Sum](https://leetcode.com/problems/combination-sum/)
- [LC 90 · Subsets II](https://leetcode.com/problems/subsets-ii/)
