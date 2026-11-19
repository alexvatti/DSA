"""
============================================================
 1. REVERSE LINKED LIST (LeetCode 206)
============================================================

PROBLEM
-------
Given the head of a singly linked list, reverse the list and return the new head.

Example:
    1 -> 2 -> 3 -> 4 -> 5 -> None   =>  5 -> 4 -> 3 -> 2 -> 1 -> None
    1 -> 2 -> None                  =>  2 -> 1 -> None
    None                            =>  None


WHEN TO USE
-----------
- You must change the direction of the links, or read the list backwards
- Only next pointers may change (no extra array)
- 🔍 Keywords: reverse, backwards, flip, in-place


APPROACH — PREV / CURR
----------------------
Flip every next arrow so it points backwards. Walk the list once, remembering the previous node.

Step by step:
    1. prev = None, curr = head.
    2. Save nxt = curr.next (or you lose the rest of the list!).
    3. Flip the arrow: curr.next = prev.
    4. Move both forward: prev = curr, curr = nxt.
    5. When curr is None, prev is the new head.


💡 TIPS TO REMEMBER
-------------------
- Always save next before you overwrite it.
- Return prev, not curr.
- Time O(n) • Space O(1).
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
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next     # 1. remember the next node
        curr.next = prev    # 2. flip the arrow
        prev = curr         # 3. move prev forward
        curr = nxt          # 4. move curr forward

    return prev             # prev is the new head


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(to_list(reverse_list(build([1, 2, 3, 4, 5]))))   # [5, 4, 3, 2, 1]
    print(to_list(reverse_list(build([1, 2]))))            # [2, 1]
    print(to_list(reverse_list(build([]))))                # []
