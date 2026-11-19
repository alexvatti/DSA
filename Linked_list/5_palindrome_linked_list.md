# 5. Palindrome Linked List — LeetCode 234

🔗 **LeetCode:** https://leetcode.com/problems/palindrome-linked-list/
💻 **Code file:** [`5_palindrome_linked_list.py`](5_palindrome_linked_list.py)
🔗 **Pattern:** 🐢🐇 + 🔄 Combo

---

## 📝 Problem

Return True if the linked list reads the same forwards and backwards.

**Examples**
```
1 -> 2 -> 2 -> 1   =>  True
1 -> 2 -> 3 -> 2 -> 1   =>  True
1 -> 2                 =>  False
```

---

## ✅ When to use it

- You must compare the list **front vs back** but can only move forward
- Only **O(1)** extra space is allowed
- 🔍 Keywords: *palindrome, symmetric, same forwards and backwards*

---

## 🔗 Approach — + 🔄 Combo

Combine two earlier tricks: find the **middle**, **reverse** the second half, then compare both halves from the outside in.

**Steps**
1. Find the middle with slow / fast.
2. Reverse the list starting from `slow`.
3. Walk `left` from the head and `right` from the reversed half together.
4. Any mismatch → `False`. If `right` runs out → `True`.

---

## 💡 Tips to Remember

- For odd length the middle node is compared with itself — harmless.
- Reversing in place keeps space at **O(1)**.
- Time **O(n)** • Space **O(1)**.

---

## 💻 Code

```python
def is_palindrome(head):
    # 1. find the middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse the second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # 3. compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

---

## ✅ Dry run on `1 -> 2 -> 2 -> 1`:

| step | what happens | state |
|------|--------------|-------|
| 1 | slow / fast find the middle | slow stops at the 2nd `2` |
| 2 | reverse from slow | second half becomes `1 -> 2` |
| 3 | `left=1`, `right=1` | match ✓ |
| 4 | `left=2`, `right=2` | match ✓ |
| 5 | `right` is None | all matched → `True` |
