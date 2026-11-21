"""
============================================================
 stack_base.py  —  OUR OWN STACK  (base code, written ONCE)
============================================================

Every problem in this folder that says "our own stack" uses THIS class:

    from stack_base import Stack

A stack is Last-In-First-Out (LIFO): you only touch the TOP.

    push(x)    -> put x on the top
    pop()      -> take the top item out and return it
    is_empty() -> True when nothing is inside

(peek and size are small extras.)
"""


class Stack:
    def __init__(self):
        self.items = []                 # the end of the list is the TOP

    def push(self, x):                  # put x on the TOP
        self.items.append(x)

    def pop(self):                      # remove and return the TOP
        return self.items.pop()

    def peek(self):                     # look at the TOP, do not remove
        return self.items[-1]

    def is_empty(self):                 # True when nothing is inside
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ----------------------------------------------------------
# Try it:  python3 stack_base.py
# ----------------------------------------------------------
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())     # True
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())         # 3   (top)
    print(s.pop())          # 3   (last in, first out)
    print(s.pop())          # 2
    print(s.is_empty())     # False  (1 is still inside)
