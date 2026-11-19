# 🔗 Linked List — Pattern Guide (Part 1: Easy)

This folder teaches the **Linked List** technique through the six classic easy problems.
Each problem has **notes** (`.md`) with *when to use it*, the approach, tips and a dry run, and a clean **solution** (`.py`) with test cases.
Open [`linked_list_easy.html`](linked_list_easy.html) in a browser for an interactive, step-by-step visual playground (one tab per problem).

---

## 🤔 What is the Linked List technique?

A linked list is a chain of **nodes**: each holds a `val` and a `next` pointer, and the last `next` is `None`.
You cannot jump to index `i` — you must **walk** from the head. So almost every problem is solved by moving
**one or two pointers** along the chain and re-linking `next` arrows, in **O(n)** time and **O(1)** extra space.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### When to use it
- ✅ You need the **middle**, a **cycle**, or a node **from the end**
- ✅ You must **reverse** or re-link nodes **in place**
- ✅ You **merge** or compare two chains
- ✅ Extra memory (array / set) is **not allowed**
- ✅ Keywords: *reverse, middle, cycle, merge, palindrome, intersection*

---

## 🔑 Key idea

**Never lose the rest of the list: save `next` before you change it.**

| Pattern | Pointers | Use it for |
|---|---|---|
| Prev / Curr | `prev`, `curr`, `nxt` | Reversing, re-linking |
| Slow & Fast | `slow` +1, `fast` +2 | Middle, cycle, halves |
| Dummy node | `dummy`, `tail` | Building a new list (merge) |
| Switch heads | `a`, `b` | Two lists of different length (intersection) |

---

## 🧩 Templates

**Reverse (prev / curr)**
```python
prev, curr = None, head
while curr:
    nxt = curr.next      # save
    curr.next = prev     # flip
    prev, curr = curr, nxt
return prev
```

**Slow & Fast (middle / cycle)**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    # cycle check: if slow is fast: return True
return slow              # middle
```

**Dummy node (build a list)**
```python
dummy = ListNode()
tail = dummy
# ... tail.next = chosen_node; tail = tail.next
return dummy.next
```

---

## 🧭 Problems in this folder (easy)

| # | Problem | LeetCode | Pattern | Notes (MD) | Code |
|---|---------|----------|---------|------------|------|
| 1 | Reverse Linked List | 206 | Prev / Curr | [notes](1_reverse_linked_list.md) | [`1_reverse_linked_list.py`](1_reverse_linked_list.py) |
| 2 | Linked List Cycle | 141 | Slow & Fast | [notes](2_linked_list_cycle.md) | [`2_linked_list_cycle.py`](2_linked_list_cycle.py) |
| 3 | Middle of the Linked List | 876 | Slow & Fast | [notes](3_middle_of_linked_list.md) | [`3_middle_of_linked_list.py`](3_middle_of_linked_list.py) |
| 4 | Merge Two Sorted Lists | 21 | Dummy node | [notes](4_merge_two_sorted_lists.md) | [`4_merge_two_sorted_lists.py`](4_merge_two_sorted_lists.py) |
| 5 | Palindrome Linked List | 234 | Slow & Fast + Reverse | [notes](5_palindrome_linked_list.md) | [`5_palindrome_linked_list.py`](5_palindrome_linked_list.py) |
| 6 | Intersection of Two Linked Lists | 160 | Two pointers, switch heads | [notes](6_intersection_of_two_lists.md) | [`6_intersection_of_two_lists.py`](6_intersection_of_two_lists.py) |

---

## 🧠 Golden tips to recognize Linked List patterns

- ✅ "Reverse / flip / backwards" → **prev / curr**.
- ✅ "Middle / half / cycle / loop" → **slow & fast**.
- ✅ "Merge / build a new list" → **dummy node**.
- ✅ "Compare front and back" → find middle, **reverse the second half**, compare.
- ✅ "Two lists, different lengths, shared tail" → **switch heads**.

---

## ⚠️ Common mistakes

- Overwriting `curr.next` **before** saving it — the rest of the list is lost.
- Returning `curr` instead of `prev` after reversing.
- Calling `fast.next.next` without checking `fast and fast.next` first.
- Comparing nodes by **value** instead of identity (`is`) when detecting cycles / intersections.
- Forgetting the `dummy` node, then special-casing the head.
- Forgetting the leftover list after the merge loop (`tail.next = l1 or l2`).

---

## ▶️ How to run any file

```bash
python3 LinkedList/1_reverse_linked_list.py
```

Every file has test cases at the bottom so you can see the output immediately.
To see the animation, open `LinkedList/linked_list_easy.html` in your browser.
