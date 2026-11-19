# 2. Linked List Cycle (Detect Cycle) — LeetCode 141

🔗 **LeetCode:** https://leetcode.com/problems/linked-list-cycle/
💻 **Code file:** [`2_linked_list_cycle.py`](2_linked_list_cycle.py)
🔗 **Pattern:** 🐢🐇 Slow & Fast

---

## 📝 Problem

Given head, return True if the list has a cycle (some node's next points back to an earlier node), otherwise False.

**Examples**
```
3 -> 2 -> 0 -> -4, tail points back to node 2   =>  True
1 -> 2 -> None                                  =>  False
None                                            =>  False
```

---

## ✅ When to use it

- You must detect a **loop** in a chain using no extra memory
- A plain walk might **never end**
- 🔍 Keywords: *cycle, loop, repeats, never terminates*

---

## 🔗 Approach — Slow & Fast

If there is a loop, a fast runner will eventually **lap** the slow runner — they must meet. If there is no loop, fast falls off the end.

**Steps**
1. Start `slow` and `fast` at the head.
2. Each round: `slow` moves 1 step, `fast` moves 2 steps.
3. If `slow is fast` → cycle → `True`.
4. If `fast` (or `fast.next`) becomes `None` → `False`.

---

## 💡 Tips to Remember

- Check `fast and fast.next` before moving 2 steps.
- Compare nodes with `is`, not by value.
- Time **O(n)** • Space **O(1)** (a set would be O(n) space).

---

## 💻 Code

```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        if slow is fast:          # they met -> loop exists
            return True

    return False                  # fast reached the end
```

---

## ✅ Dry run on `3 -> 2 -> 0 -> -4` (tail points back to `2`):

| round | slow | fast |
|-------|------|------|
| start | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 |
| 3 | -4 | -4 |

`slow is fast` → cycle → `True`
