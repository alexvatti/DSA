"""
============================================================
 2. REORDER LIST (LeetCode 143)
============================================================

PROBLEM
-------
Reorder L0 -> L1 -> ... -> Ln into L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... Do it in place (change the links, not the values).

Example:
    1 -> 2 -> 3 -> 4         =>  1 -> 4 -> 2 -> 3
    1 -> 2 -> 3 -> 4 -> 5    =>  1 -> 5 -> 2 -> 4 -> 3


WHEN TO USE
-----------
- The new order alternates between the front and the back
- You can only move forward through the list
- 🔍 Keywords: reorder, interleave, first-last-second-second last


APPROACH — MIDDLE + REVERSE + WEAVE
-----------------------------------
Reorder L0 → L1 → … → Ln into L0 → Ln → L1 → Ln-1 → …. It glues three easy tricks together: find the middle, reverse the second half, then weave the two halves one node at a time.

Step by step:
    1. Find the middle with slow / fast (stop when fast.next.next is None).
    2. Cut the list after slow and reverse the second half.
    3. Weave: take one node from the first half, then one from the reversed second half.
    4. Repeat until the second half is finished.


💡 TIPS TO REMEMBER
-------------------
- Cut with slow.next = None so the first half ends cleanly.
- Save both next pointers (n1, n2) before re-linking.
- Time O(n) • Space O(1). It changes the list in place and returns nothing.
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
def reorder_list(head):
    if not head or not head.next:
        return

    # 1. find the middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. cut after slow, then reverse the second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    # 3. weave the two halves together
    first, second = head, prev
    while second:
        n1, n2 = first.next, second.next
        first.next = second         # first -> second
        second.next = n1            # second -> next of first
        first, second = n1, n2


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    reorder_list(head)
    print(to_list(head))      # [1, 5, 2, 4, 3]

    head = build([1, 2, 3, 4])
    reorder_list(head)
    print(to_list(head))      # [1, 4, 2, 3]

    head = build([1])
    reorder_list(head)
    print(to_list(head))      # [1]
