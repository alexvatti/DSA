"""
============================================================
 3. COPY LIST WITH RANDOM POINTER (LeetCode 138)
============================================================

PROBLEM
-------
Each node has a next pointer and a random pointer (to any node in the list, or None). Return a deep copy: a brand-new list whose nodes copy the values and whose pointers point only to new nodes.

Example:
    [[7,None],[13,0],[11,4],[10,2],[1,0]]  =>  a new list with the same values and pointers
    (pair = [value, index of the random target])


WHEN TO USE
-----------
- A node has an extra pointer (random) and you need a deep copy
- Pointers may refer to nodes that do not exist yet
- 🔍 Keywords: copy, clone, deep copy, random pointer


APPROACH — OLD → NEW MAP
------------------------
Each node has an extra random pointer. Make a deep copy: the new list must use brand-new nodes. Keep a dictionary old → new so any pointer of an old node can be translated into the matching new node.

Step by step:
    1. Pass 1: walk the list and store old_to_new[node] = Node(node.val).
    2. Pass 2: walk again and set each copy's next and random using the map.
    3. Return old_to_new[head].


💡 TIPS TO REMEMBER
-------------------
- old_to_new.get(None) gives None, so the end of the list needs no special case.
- Two passes are needed because random may point forward to a copy that does not exist yet.
- Time O(n) • Space O(n) for the map (an O(1) interleaving trick exists, but this is the clear one).
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_random(values, random_index):
    """node i.random = node random_index[i]  (-1 means None)"""
    nodes = [Node(v) for v in values]
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.next = nodes[i + 1]
        if random_index[i] >= 0:
            node.random = nodes[random_index[i]]
    return nodes[0] if nodes else None


def to_pairs(head):
    """Node list -> [[val, index_of_random_or_None], ...]"""
    order, curr, i = {}, head, 0
    while curr:
        order[curr] = i
        curr = curr.next
        i += 1
    out, curr = [], head
    while curr:
        out.append([curr.val, order[curr.random] if curr.random else None])
        curr = curr.next
    return out


# ----------------------------------------------------------
# Solution
# ----------------------------------------------------------
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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    head = build_random([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
    copy = copy_random_list(head)
    print(to_pairs(copy))         # [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    print(copy is not head)       # True  (new nodes, not the originals)
    print(copy_random_list(None)) # None
