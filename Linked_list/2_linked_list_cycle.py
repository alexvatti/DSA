"""
============================================================
 2. LINKED LIST CYCLE (DETECT CYCLE) (LeetCode 141)
============================================================

PROBLEM
-------
Given head, return True if the list has a cycle (some node's next points back to an earlier node), otherwise False.

Example:
    3 -> 2 -> 0 -> -4, tail points back to node 2   =>  True
    1 -> 2 -> None                                  =>  False
    None                                            =>  False


WHEN TO USE
-----------
- You must detect a loop in a chain using no extra memory
- A plain walk might never end
- 🔍 Keywords: cycle, loop, repeats, never terminates


APPROACH — SLOW & FAST
----------------------
If there is a loop, a fast runner will eventually lap the slow runner — they must meet. If there is no loop, fast falls off the end.

Step by step:
    1. Start slow and fast at the head.
    2. Each round: slow moves 1 step, fast moves 2 steps.
    3. If slow is fast → cycle → True.
    4. If fast (or fast.next) becomes None → False.


💡 TIPS TO REMEMBER
-------------------
- Check fast and fast.next before moving 2 steps.
- Compare nodes with is, not by value.
- Time O(n) • Space O(1) (a set would be O(n) space).
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
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        if slow is fast:          # they met -> loop exists
            return True

    return False                  # fast reached the end


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    head = build([3, 2, 0, -4])
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head.next                  # tail points back to node 2 -> cycle
    print(has_cycle(head))                 # True
    print(has_cycle(build([1, 2])))        # False
    print(has_cycle(build([])))            # False
