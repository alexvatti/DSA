"""
============================================================
 4. MERGE TWO SORTED LISTS (LeetCode 21)
============================================================

PROBLEM
-------
Merge two sorted linked lists into one sorted list by splicing the existing nodes together.

Example:
    [1, 2, 4] + [1, 3, 4]   =>  [1, 1, 2, 3, 4, 4]
    [] + []                 =>  []
    [] + [0]                =>  [0]


WHEN TO USE
-----------
- You combine two sorted lists into one
- You build a new list piece by piece and the head is unknown
- 🔍 Keywords: merge, combine, sorted, smallest first


APPROACH — DUMMY NODE
---------------------
Like the merge step of merge sort: always take the smaller front node. A dummy node gives tail a place to start.

Step by step:
    1. Make dummy and set tail = dummy.
    2. While both lists have nodes: attach the smaller head to tail.next and advance that list.
    3. Move tail forward.
    4. Attach whatever is left: tail.next = l1 or l2.
    5. Return dummy.next.


💡 TIPS TO REMEMBER
-------------------
- The dummy node removes the "which node is the head?" headache.
- No new nodes are created — we just re-link existing ones.
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
def merge_two_lists(l1, l2):
    dummy = ListNode()          # fake head
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1      # take from l1
            l1 = l1.next
        else:
            tail.next = l2      # take from l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2        # attach the leftover list
    return dummy.next


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))))   # [1, 1, 2, 3, 4, 4]
    print(to_list(merge_two_lists(build([]), build([]))))                # []
    print(to_list(merge_two_lists(build([]), build([0]))))               # [0]
