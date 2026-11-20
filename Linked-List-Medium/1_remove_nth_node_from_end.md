# 1. Remove Nth Node From End of List — LeetCode 19

🔗 **LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/
💻 **Code file:** [`1_remove_nth_node_from_end.py`](1_remove_nth_node_from_end.py)
🔗 **Pattern:** 📏 Gap Pointers

---

## 📝 Problem

Given the head of a linked list, remove the n-th node from the END of the list and return its head.

**Examples**
```
1 -> 2 -> 3 -> 4 -> 5, n = 2   =>  1 -> 2 -> 3 -> 5
1, n = 1                       =>  None
1 -> 2, n = 1                  =>  1
```

---

## ✅ When to use it

- You need the **nth node from the end** but do not know the length
- You want **one pass** and O(1) space
- 🔍 Keywords: *nth from the end, remove, last k nodes*

---

## 🔗 Approach — Gap Pointers

Walk the list **once**: put `fast` exactly `n` steps ahead of `slow`. When `fast` reaches the last node, `slow` is right before the node to delete. A **dummy** head makes removing the first node easy.

**Steps**
1. Create `dummy` before `head`; set `slow = fast = dummy`.
2. Move `fast` forward `n` steps (this builds the gap).
3. Move `slow` and `fast` together until `fast.next` is `None`.
4. `slow` is just before the target: `slow.next = slow.next.next`.
5. Return `dummy.next`.

---

## 💡 Tips to Remember

- The dummy node handles "remove the head" with no special case.
- A gap of `n` between the pointers means `n` from the end.
- Time **O(n)** • Space **O(1)** — one pass, no length counting.

---

## 💻 Code

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)       # fake head, so removing the first node is easy
    slow = fast = dummy

    for _ in range(n):              # 1. fast goes n steps ahead
        fast = fast.next

    while fast.next:                # 2. move both until fast is on the last node
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next      # 3. skip the target node
    return dummy.next
```

---

## ✅ Dry run on `1 -> 2 -> 3 -> 4 -> 5`, `n = 2` (D = dummy):

| step | slow | fast |
|------|------|------|
| start | D | D |
| gap 1 | D | 1 |
| gap 2 | D | 2 |
| both +1 | 1 | 3 |
| both +1 | 2 | 4 |
| both +1 | 3 | 5 (`fast.next` is None → stop) |

`slow` = 3, so `slow.next = slow.next.next` skips `4` → `1 -> 2 -> 3 -> 5`
