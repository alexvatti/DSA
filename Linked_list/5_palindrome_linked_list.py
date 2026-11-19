"""
============================================================
 5. PALINDROME LINKED LIST (LeetCode 234)
============================================================

PROBLEM
-------
Return True if the linked list reads the same forwards and backwards.

Example:
    1 -> 2 -> 2 -> 1   =>  True
    1 -> 2 -> 3 -> 2 -> 1   =>  True
    1 -> 2                 =>  False


WHEN TO USE
-----------
- You must compare the list front vs back but can only move forward
- Only O(1) extra space is allowed
- 🔍 Keywords: palindrome, symmetric, same forwards and backwards


APPROACH — + 🔄 COMBO
--------------------
Combine two earlier tricks: find the middle, reverse the second half, then compare both halves from the outside in.

Step by step:
    1. Find the middle with slow / fast.
    2. Reverse the list starting from slow.
    3. Walk left from the head and right from the reversed half together.
    4. Any mismatch → False. If right runs out → True.


💡 TIPS TO REMEMBER
-------------------
- For odd length the middle node is compared with itself — harmless.
- Reversing in place keeps space at O(1).
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
def is_palindrome(head):
    # 1. find the middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse the second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # 3. compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(is_palindrome(build([1, 2, 2, 1])))      # True
    print(is_palindrome(build([1, 2, 3, 2, 1])))   # True
    print(is_palindrome(build([1, 2])))            # False
    print(is_palindrome(build([1])))               # True
