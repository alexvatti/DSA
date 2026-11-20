"""
============================================================
 4. ADD TWO NUMBERS (LeetCode 2)
============================================================

PROBLEM
-------
Two non-empty linked lists hold the digits of two non-negative integers in REVERSE order (head = ones place). Add the numbers and return the sum as a linked list in the same format.

Example:
    [2, 4, 3] + [5, 6, 4]   =>  [7, 0, 8]     (342 + 465 = 807)
    [0] + [0]               =>  [0]
    [9,9,9,9,9,9,9] + [9,9,9,9]  =>  [8,9,9,9,0,0,0,1]


WHEN TO USE
-----------
- Numbers are stored as digit lists and may be too big for an int
- You must do schoolbook addition with a carry
- 🔍 Keywords: add two numbers, digits, reverse order, carry


APPROACH — DUMMY + CARRY
------------------------
Digits are stored in reverse order, so the head is the ones place — exactly how you add by hand. Add digit by digit, pass the carry along, and build the answer with a dummy head.

Step by step:
    1. Make dummy, tail and carry = 0.
    2. While l1 or l2 or carry remains: total = carry + digit1 + digit2 (a missing digit counts as 0).
    3. Append a node with total % 10 and set carry = total // 10.
    4. Move l1, l2 and tail forward. Return dummy.next.


💡 TIPS TO REMEMBER
-------------------
- Keep looping while carry is non-zero, or 9 + 1 would lose a digit.
- A shorter list simply contributes 0.
- Time O(max(n, m)) • Space O(1) extra (the output list is the answer).
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
def add_two_numbers(l1, l2):
    dummy = ListNode()
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next

        carry = total // 10                 # 0 or 1
        tail.next = ListNode(total % 10)    # the digit to keep
        tail = tail.next

    return dummy.next


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(to_list(add_two_numbers(build([2, 4, 3]), build([5, 6, 4]))))   # [7, 0, 8]
    print(to_list(add_two_numbers(build([0]), build([0]))))              # [0]
    print(to_list(add_two_numbers(build([9, 9, 9, 9, 9, 9, 9]), build([9, 9, 9, 9]))))   # [8, 9, 9, 9, 0, 0, 0, 1]
