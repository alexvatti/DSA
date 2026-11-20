# 3. Copy List With Random Pointer — LeetCode 138

🔗 **LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/
💻 **Code file:** [`3_copy_list_with_random_pointer.py`](3_copy_list_with_random_pointer.py)
🔗 **Pattern:** 🗺️ Old → New Map

---

## 📝 Problem

Each node has a next pointer and a random pointer (to any node in the list, or None). Return a deep copy: a brand-new list whose nodes copy the values and whose pointers point only to new nodes.

**Examples**
```
[[7,None],[13,0],[11,4],[10,2],[1,0]]  =>  a new list with the same values and pointers
(pair = [value, index of the random target])
```

---

## ✅ When to use it

- A node has an extra pointer (`random`) and you need a **deep copy**
- Pointers may refer to nodes that **do not exist yet**
- 🔍 Keywords: *copy, clone, deep copy, random pointer*

---

## 🔗 Approach — Old → New Map

Each node has an extra `random` pointer. Make a **deep copy**: the new list must use **brand-new nodes**. Keep a dictionary `old → new` so any pointer of an old node can be translated into the matching new node.

**Steps**
1. Pass 1: walk the list and store `old_to_new[node] = Node(node.val)`.
2. Pass 2: walk again and set each copy's `next` and `random` using the map.
3. Return `old_to_new[head]`.

---

## 💡 Tips to Remember

- `old_to_new.get(None)` gives `None`, so the end of the list needs no special case.
- Two passes are needed because `random` may point **forward** to a copy that does not exist yet.
- Time **O(n)** • Space **O(n)** for the map (an O(1) interleaving trick exists, but this is the clear one).

---

## 💻 Code

```python
def copy_random_list(head):
    if not head:
        return None

    old_to_new = {}

    # pass 1: create a copy of every node (no links yet)
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # pass 2: wire next and random using the map
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]
```

---

## ✅ Dry run on `1 -> 2 -> 3` with `1.random = 3`, `2.random = 1`, `3.random = None`:

| pass | curr | action |
|------|------|--------|
| 1 | 1 | `map[1] = 1'` |
| 1 | 2 | `map[2] = 2'` |
| 1 | 3 | `map[3] = 3'` |
| 2 | 1 | `1'.next = 2'`, `1'.random = 3'` |
| 2 | 2 | `2'.next = 3'`, `2'.random = 1'` |
| 2 | 3 | `3'.next = None`, `3'.random = None` |

Return `map[head]` = `1'`
