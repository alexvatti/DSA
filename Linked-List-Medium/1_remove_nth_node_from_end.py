"""
============================================================
 1. REMOVE NTH NODE FROM END OF LIST (LeetCode 19)
============================================================

PROBLEM
-------
Given the head of a linked list, remove the n-th node from the END of the list and return its head.

Example:
    1 -> 2 -> 3 -> 4 -> 5, n = 2   =>  1 -> 2 -> 3 -> 5
    1, n = 1                       =>  None
    1 -> 2, n = 1                  =>  1


WHEN TO USE
-----------
- You need the nth node from the end but do not know the length
- You want one pass and O(1) space
- 🔍 Keywords: nth from the end, remove, last k nodes


APPROACH — GAP POINTERS
-----------------------
Walk the list once: put fast exactly n steps ahead of slow. When fast reaches the last node, slow is right before the node to delete. A dummy head makes removing the first node easy.

Step by step:
    1. Create dummy before head; set slow = fast = dummy.
    2. Move fast forward n steps (this builds the gap).
    3. Move slow and fast together until fast.next is None.
    4. slow is just before the target: slow.next = slow.next.next.
    5. Return dummy.next.


💡 TIPS TO REMEMBER
-------------------
- The dummy node handles "remove the head" with no special case.
- A gap of n between the pointers means n from the end.
- Time O(n) • Space O(1) — one pass, no length counting.
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
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)       # fake head, so removing the first node is easy
    slow = fast = dummy

    for _ in range(n):              # 1. fast goes n steps ahead
        fast = fast.next

    while fast.next:                # 2. move both until fast is on the last node
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next      # 3. skip the target node
    return dummy.next


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)))   # [1, 2, 3, 5]
    print(to_list(remove_nth_from_end(build([1]), 1)))                # []
    print(to_list(remove_nth_from_end(build([1, 2]), 1)))             # [1]
    print(to_list(remove_nth_from_end(build([1, 2]), 2)))             # [2]
