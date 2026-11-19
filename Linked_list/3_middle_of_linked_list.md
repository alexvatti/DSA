# 3. Middle of the Linked List (Find Middle) — LeetCode 876

🔗 **LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/
💻 **Code file:** [`3_middle_of_linked_list.py`](3_middle_of_linked_list.py)
🔗 **Pattern:** 🐢🐇 Slow & Fast

---

## 📝 Problem

Return the middle node of the linked list. If there are two middle nodes, return the second one.

**Examples**
```
1 -> 2 -> 3 -> 4 -> 5          =>  node 3
1 -> 2 -> 3 -> 4 -> 5 -> 6     =>  node 4
```

---

## ✅ When to use it

- You need the **middle** in one pass and the length is unknown
- First step of Palindrome / Reorder List
- 🔍 Keywords: *middle, half, split in two*

---

## 🔗 Approach — Slow & Fast

Fast moves twice as quickly, so when fast reaches the end, slow is exactly halfway.

**Steps**
1. Start `slow` and `fast` at the head.
2. While `fast` and `fast.next` exist: `slow` +1, `fast` +2.
3. Return `slow`.

---

## 💡 Tips to Remember

- Even length → returns the **second** of the two middle nodes (what LeetCode asks).
- This same trick is the first step of Palindrome List.
- Time **O(n)** • Space **O(1)**.

---

## 💻 Code

```python
def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

---

## ✅ Dry run on `1 -> 2 -> 3 -> 4 -> 5`:

| round | slow | fast |
|-------|------|------|
| start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

`fast.next` is None → stop → middle = `3`
