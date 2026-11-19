"""
============================================================
 6. INTERSECTION OF TWO LINKED LISTS (LeetCode 160)
============================================================

PROBLEM
-------
Given the heads of two linked lists, return the node where they start to share the same tail (the same node object), or None if they never meet.

Example:
    A: a1 -> a2 -> c1 -> c2,  B: b1 -> c1 -> c2   =>  c1
    A: 1 -> 2,  B: 3                              =>  None


WHEN TO USE
-----------
- Two lists may join into the same tail
- Lengths differ and you want O(1) space
- 🔍 Keywords: intersection, merge point, shared node


APPROACH — TWO POINTERS
-----------------------
Two lists may merge into a shared tail (amber nodes). Lengths differ, so walk pointer a along A then B, and pointer b along B then A. Both travel the same total distance, so they meet at the intersection.

Step by step:
    1. a = headA, b = headB.
    2. Move both one step at a time.
    3. When a pointer reaches the end, send it to the head of the other list.
    4. Stop when a is b — that node is the intersection, or both are None (no intersection).


💡 TIPS TO REMEMBER
-------------------
- The shared tail means the same node object, not just equal values.
- After switching, both pointers have walked lenA + lenB, so they line up.
- Time O(n + m) • Space O(1).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    """[1, 2, 3] -> 1 -> 2 -> 3 -> None"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    """1 -> 2 -> 3 -> None -> [1, 2, 3]"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ----------------------------------------------------------
# Solution
# ----------------------------------------------------------
def get_intersection_node(headA, headB):
    a, b = headA, headB

    while a is not b:
        a = a.next if a else headB    # fell off A -> jump to B
        b = b.next if b else headA    # fell off B -> jump to A

    return a    # intersection node, or None


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    shared = build([8, 4, 5])
    a = ListNode(4, ListNode(1, shared))
    b = ListNode(5, ListNode(6, ListNode(1, shared)))
    print(get_intersection_node(a, b).val)                     # 8
    print(get_intersection_node(build([1, 2]), build([3])))    # None
