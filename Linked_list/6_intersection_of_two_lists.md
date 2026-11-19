# 6. Intersection of Two Linked Lists — LeetCode 160

🔗 **LeetCode:** https://leetcode.com/problems/intersection-of-two-linked-lists/
💻 **Code file:** [`6_intersection_of_two_lists.py`](6_intersection_of_two_lists.py)
🔗 **Pattern:** 🔁 Two Pointers

---

## 📝 Problem

Given the heads of two linked lists, return the node where they start to share the same tail (the same node object), or None if they never meet.

**Examples**
```
A: a1 -> a2 -> c1 -> c2,  B: b1 -> c1 -> c2   =>  c1
A: 1 -> 2,  B: 3                              =>  None
```

---

## ✅ When to use it

- Two lists may **join into the same tail**
- Lengths differ and you want **O(1)** space
- 🔍 Keywords: *intersection, merge point, shared node*

---

## 🔗 Approach — Two Pointers

Two lists may **merge into a shared tail** (amber nodes). Lengths differ, so walk pointer `a` along A then B, and pointer `b` along B then A. Both travel the same total distance, so they meet at the intersection.

**Steps**
1. `a = headA`, `b = headB`.
2. Move both one step at a time.
3. When a pointer reaches the end, send it to the **head of the other list**.
4. Stop when `a is b` — that node is the intersection, or both are `None` (no intersection).

---

## 💡 Tips to Remember

- The shared tail means the **same node object**, not just equal values.
- After switching, both pointers have walked `lenA + lenB`, so they line up.
- Time **O(n + m)** • Space **O(1)**.

---

## 💻 Code

```python
def get_intersection_node(headA, headB):
    a, b = headA, headB

    while a is not b:
        a = a.next if a else headB    # fell off A -> jump to B
        b = b.next if b else headA    # fell off B -> jump to A

    return a    # intersection node, or None
```

---

## ✅ Dry run: `A = a1,a2,c1,c2` and `B = b1,c1,c2` (lenA=4, lenB=3):

| step | a | b |
|------|---|---|
| 0 | a1 | b1 |
| 1 | a2 | c1 |
| 2 | c1 | c2 |
| 3 | c2 | None |
| 4 | None | a1 (jumped to headA) |
| 5 | b1 (jumped to headB) | a2 |
| 6 | c1 | c1 ← **same node** |

`a is b` → return `c1`
