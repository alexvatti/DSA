"""
============================================================
 4. deque  —  Fast adding/removing at BOTH ends
============================================================
 (pronounced "deck", short for Double-Ended QUEue)

THE PROBLEM WITH LISTS
----------------------
A normal list is fast at the END:
    mylist.append(x)      # fast ✅
    mylist.pop()          # fast ✅

But SLOW at the FRONT:
    mylist.insert(0, x)   # slow ❌ (shifts everything)
    mylist.pop(0)         # slow ❌ (shifts everything)

THE SOLUTION
------------
`deque` is fast at BOTH ends. This makes it perfect for
Queues and Stacks — very common in DSA! 🚀
"""

from collections import deque


# ----------------------------------------------------------
# Example 1: Create a deque
# ----------------------------------------------------------
dq = deque([1, 2, 3])
print("Starting deque:", dq)   # deque([1, 2, 3])


# ----------------------------------------------------------
# Example 2: Add to both ends
# ----------------------------------------------------------
dq.append(4)        # add to the RIGHT end
dq.appendleft(0)    # add to the LEFT end
print("After append(4) and appendleft(0):", dq)
# deque([0, 1, 2, 3, 4])


# ----------------------------------------------------------
# Example 3: Remove from both ends
# ----------------------------------------------------------
right = dq.pop()        # remove from the RIGHT
left = dq.popleft()     # remove from the LEFT
print(f"\nRemoved {left} from left and {right} from right")
print("Deque now:", dq)   # deque([1, 2, 3])


# ----------------------------------------------------------
# Example 4: Use it as a QUEUE (First In, First Out)
# ----------------------------------------------------------
# A line at a shop: first person in is first person served.
queue = deque()
queue.append("Alice")   # Alice joins
queue.append("Bob")     # Bob joins
queue.append("Charlie") # Charlie joins

print("\n--- Queue (FIFO) ---")
print("Serving:", queue.popleft())  # Alice (joined first)
print("Serving:", queue.popleft())  # Bob
print("Still waiting:", queue)        # deque(['Charlie'])


# ----------------------------------------------------------
# Example 5: Use it as a STACK (Last In, First Out)
# ----------------------------------------------------------
# A stack of plates: last plate on is first plate off.
stack = deque()
stack.append("plate1")
stack.append("plate2")
stack.append("plate3")

print("\n--- Stack (LIFO) ---")
print("Taking:", stack.pop())   # plate3 (added last)
print("Taking:", stack.pop())   # plate2
print("Remaining:", stack)        # deque(['plate1'])


# ----------------------------------------------------------
# Example 6: maxlen — a deque with a size limit
# ----------------------------------------------------------
# When full, adding a new item drops the oldest one.
recent = deque(maxlen=3)
for number in [1, 2, 3, 4, 5]:
    recent.append(number)
    print(f"Added {number} -> {recent}")
# Keeps only the last 3: deque([3, 4, 5], maxlen=3)


# ----------------------------------------------------------
# 🧠 KEY IDEA:
#   Need a queue or stack in DSA? Use deque — it's FAST.
#
#   Run with:  python3 collections/4_deque.py
# ----------------------------------------------------------
