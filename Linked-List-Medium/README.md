# 🔗 Linked List — Pattern Guide (Part 2: Medium)

Part 1 taught the basic pointer tools. A **Medium** problem usually **glues two or three of them together** (or adds a hash map).
Each problem has **notes** (`.md`) with *when to use it*, the approach, tips and a dry run, and a clean **solution** (`.py`) with test cases.
Open [`linked_list_medium.html`](linked_list_medium.html) in a browser for the interactive, step-by-step playground (one tab per problem).

---

## 🤔 What makes a Medium problem?

Same tools as Part 1 — `next` pointers, `prev / curr`, `slow / fast`, a `dummy` head — but combined:

| Pattern | Building blocks | Problem |
|---|---|---|
| Gap pointers | `fast` starts `n` steps ahead + `dummy` | Remove Nth Node From End |
| Middle + Reverse + Weave | slow/fast + prev/curr + interleave | Reorder List |
| Old → New map | dictionary `old_to_new` | Copy List With Random Pointer |
| Dummy + carry | `dummy`, `tail`, `carry` | Add Two Numbers |
| Floyd on an array | index `i` points to `nums[i]` | Find the Duplicate Number |
| Map + doubly linked list | `dict` + `prev/next` nodes + dummy ends | LRU Cache |

### When to use it
- ✅ You need the **nth node from the end** without knowing the length
- ✅ The new order **alternates** between the front and the back
- ✅ You must **clone** nodes that have extra pointers
- ✅ Numbers are **digit lists** with a carry
- ✅ An array secretly forms a **linked list / cycle**
- ✅ You need an **LRU cache** with O(1) get / put

---

## 🔑 Key idea

**Break it into easy blocks, name each one, and save `next` before every re-link.**

---

## 🧩 Templates

**Gap pointers (nth from end)**
```python
dummy = ListNode(0, head)
slow = fast = dummy
for _ in range(n):
    fast = fast.next          # build the gap
while fast.next:
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next    # slow is just before the target
```

**Old → New map (copy / clone)**
```python
old_to_new = {}
# pass 1: create a copy of every node
# pass 2: old_to_new[node].next = old_to_new.get(node.next)
```

**Dummy + carry (build a number)**
```python
while l1 or l2 or carry:
    total = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
    carry, digit = divmod(total, 10)
    tail.next = ListNode(digit)
    tail = tail.next
```

**Floyd on an array (hidden cycle)**
```python
slow = fast = 0
while True:                     # phase 1: meet inside the cycle
    slow, fast = nums[slow], nums[nums[fast]]
    if slow == fast: break
slow = 0
while slow != fast:             # phase 2: meet at the entrance
    slow, fast = nums[slow], nums[fast]
```

---

## 🧭 Problems in this folder (medium)

| # | Problem | LeetCode | Pattern | Notes (MD) | Code |
|---|---------|----------|---------|------------|------|
| 1 | Remove Nth Node From End of List | 19 | Gap pointers | [notes](1_remove_nth_node_from_end.md) | [`1_remove_nth_node_from_end.py`](1_remove_nth_node_from_end.py) |
| 2 | Reorder List | 143 | Middle + Reverse + Weave | [notes](2_reorder_list.md) | [`2_reorder_list.py`](2_reorder_list.py) |
| 3 | Copy List With Random Pointer | 138 | Old → New map | [notes](3_copy_list_with_random_pointer.md) | [`3_copy_list_with_random_pointer.py`](3_copy_list_with_random_pointer.py) |
| 4 | Add Two Numbers | 2 | Dummy + carry | [notes](4_add_two_numbers.md) | [`4_add_two_numbers.py`](4_add_two_numbers.py) |
| 5 | Find the Duplicate Number | 287 | Floyd on an array | [notes](5_find_the_duplicate_number.md) | [`5_find_the_duplicate_number.py`](5_find_the_duplicate_number.py) |
| 6 | LRU Cache | 146 | Map + doubly linked list | [notes](6_lru_cache.md) | [`6_lru_cache.py`](6_lru_cache.py) |

---

## 🧠 Golden tips to recognize them

- ✅ "nth from the **end**" → **gap** between two pointers.
- ✅ "front, back, front, back" → **middle + reverse + weave**.
- ✅ "copy / clone with extra pointers" → **old → new map**.
- ✅ "digits stored in reverse" → **dummy + carry**.
- ✅ "n + 1 numbers in 1..n, find the repeat, O(1) space" → **Floyd's cycle**.
- ✅ "O(1) get/put + evict the oldest" → **hash map + doubly linked list**.

---

## ⚠️ Common mistakes

- Forgetting the **dummy** node, so removing the head needs a special case.
- Not cutting the first half (`slow.next = None`) before weaving in Reorder List.
- Overwriting `first.next` / `second.next` **before** saving them.
- Copying only `next` and forgetting `random`, or pointing a copy back at an **old** node.
- Stopping the loop when the lists end but a **carry** is still left.
- In LRU Cache: forgetting to delete the evicted key from the **map**, or not storing `key` inside the node.
- Starting Floyd at `nums[0]` instead of a node outside the cycle, or moving `fast` 2 steps in phase 2.

---

## ▶️ How to run any file

```bash
python3 LinkedListMedium/1_remove_nth_node_from_end.py
```

Every file has test cases at the bottom so you can see the output immediately.
To see the animation, open `LinkedListMedium/linked_list_medium.html` in your browser.
