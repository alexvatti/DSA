"""
============================================================
 3. MIDDLE OF THE LINKED LIST (FIND MIDDLE) (LeetCode 876)
============================================================

PROBLEM
-------
Return the middle node of the linked list. If there are two middle nodes, return the second one.

Example:
    1 -> 2 -> 3 -> 4 -> 5          =>  node 3
    1 -> 2 -> 3 -> 4 -> 5 -> 6     =>  node 4


WHEN TO USE
-----------
- You need the middle in one pass and the length is unknown
- First step of Palindrome / Reorder List
- 🔍 Keywords: middle, half, split in two


APPROACH — SLOW & FAST
----------------------
Fast moves twice as quickly, so when fast reaches the end, slow is exactly halfway.

Step by step:
    1. Start slow and fast at the head.
    2. While fast and fast.next exist: slow +1, fast +2.
    3. Return slow.


💡 TIPS TO REMEMBER
-------------------
- Even length → returns the second of the two middle nodes (what LeetCode asks).
- This same trick is the first step of Palindrome List.
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
def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(middle_node(build([1, 2, 3, 4, 5])).val)       # 3
    print(middle_node(build([1, 2, 3, 4, 5, 6])).val)    # 4
    print(middle_node(build([1])).val)                   # 1
