# 1. Reverse Linked List — LeetCode 206

🔗 **LeetCode:** https://leetcode.com/problems/reverse-linked-list/
💻 **Code file:** [`1_reverse_linked_list.py`](1_reverse_linked_list.py)
🔗 **Pattern:** 🔄 Prev / Curr

---

## 📝 Problem

Given the head of a singly linked list, reverse the list and return the new head.

**Examples**
```
1 -> 2 -> 3 -> 4 -> 5 -> None   =>  5 -> 4 -> 3 -> 2 -> 1 -> None
1 -> 2 -> None                  =>  2 -> 1 -> None
None                            =>  None
```

---

## ✅ When to use it

- You must **change the direction** of the links, or read the list backwards
- Only `next` pointers may change (no extra array)
- 🔍 Keywords: *reverse, backwards, flip, in-place*

---

## 🔗 Approach — Prev / Curr

Flip every `next` arrow so it points backwards. Walk the list once, remembering the previous node.

**Steps**
1. `prev = None`, `curr = head`.
2. Save `nxt = curr.next` (or you lose the rest of the list!).
3. Flip the arrow: `curr.next = prev`.
4. Move both forward: `prev = curr`, `curr = nxt`.
5. When `curr` is `None`, `prev` is the new head.

---

## 💡 Tips to Remember

- Always save `next` **before** you overwrite it.
- Return `prev`, not `curr`.
- Time **O(n)** • Space **O(1)**.

---

## 💻 Code

```python
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next     # 1. remember the next node
        curr.next = prev    # 2. flip the arrow
        prev = curr         # 3. move prev forward
        curr = nxt          # 4. move curr forward

    return prev             # prev is the new head
```

---

## ✅ Dry run on `1 -> 2 -> 3`:

| step | prev | curr | action |
|------|------|------|--------|
| start | None | 1 | — |
| 1 | 1 | 2 | `1.next = None` |
| 2 | 2 | 3 | `2.next = 1` |
| 3 | 3 | None | `3.next = 2` |

`curr` is None → return `prev` = `3 -> 2 -> 1 -> None`
