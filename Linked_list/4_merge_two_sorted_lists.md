# 4. Merge Two Sorted Lists — LeetCode 21

🔗 **LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/
💻 **Code file:** [`4_merge_two_sorted_lists.py`](4_merge_two_sorted_lists.py)
🔗 **Pattern:** 🧱 Dummy Node

---

## 📝 Problem

Merge two sorted linked lists into one sorted list by splicing the existing nodes together.

**Examples**
```
[1, 2, 4] + [1, 3, 4]   =>  [1, 1, 2, 3, 4, 4]
[] + []                 =>  []
[] + [0]                =>  [0]
```

---

## ✅ When to use it

- You combine **two sorted** lists into one
- You build a **new list** piece by piece and the head is unknown
- 🔍 Keywords: *merge, combine, sorted, smallest first*

---

## 🔗 Approach — Dummy Node

Like the merge step of merge sort: always take the **smaller** front node. A **dummy** node gives `tail` a place to start.

**Steps**
1. Make `dummy` and set `tail = dummy`.
2. While both lists have nodes: attach the smaller head to `tail.next` and advance that list.
3. Move `tail` forward.
4. Attach whatever is left: `tail.next = l1 or l2`.
5. Return `dummy.next`.

---

## 💡 Tips to Remember

- The dummy node removes the "which node is the head?" headache.
- No new nodes are created — we just re-link existing ones.
- Time **O(n + m)** • Space **O(1)**.

---

## 💻 Code

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()          # fake head
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1      # take from l1
            l1 = l1.next
        else:
            tail.next = l2      # take from l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2        # attach the leftover list
    return dummy.next
```

---

## ✅ Dry run on `l1 = 1,2,4` and `l2 = 1,3,4`:

| compare | take | merged so far |
|---------|------|---------------|
| 1 vs 1 | l1 (≤) | 1 |
| 2 vs 1 | l2 | 1, 1 |
| 2 vs 3 | l1 | 1, 1, 2 |
| 4 vs 3 | l2 | 1, 1, 2, 3 |
| 4 vs 4 | l1 | 1, 1, 2, 3, 4 |
| l1 empty | attach rest of l2 | 1, 1, 2, 3, 4, 4 |
