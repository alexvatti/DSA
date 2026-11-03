"""
============================================================
 3. OrderedDict  —  A dict that remembers order
============================================================

QUICK HISTORY
-------------
In old Python (before 3.7), normal dictionaries did NOT
guarantee the order of items. `OrderedDict` was created to
remember the exact order you inserted keys.

In modern Python (3.7+), normal dicts ALSO keep insertion
order. So you may not need OrderedDict as often today.

BUT it still has some special powers that normal dicts lack,
which is why it's good to know.
"""

from collections import OrderedDict


# ----------------------------------------------------------
# Example 1: It keeps insertion order
# ----------------------------------------------------------
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

print("OrderedDict keeps order:")
for key, value in od.items():
    print(f"  {key} = {value}")
# first = 1
# second = 2
# third = 3


# ----------------------------------------------------------
# Example 2: move_to_end() — a special power
# ----------------------------------------------------------
# You can move an existing key to the end (or beginning).
od.move_to_end("first")
print("\nAfter moving 'first' to the end:", list(od.keys()))
# ['second', 'third', 'first']

od.move_to_end("first", last=False)  # last=False -> move to front
print("After moving 'first' to the front:", list(od.keys()))
# ['first', 'second', 'third']


# ----------------------------------------------------------
# Example 3: popitem() — remove from either end
# ----------------------------------------------------------
od.popitem(last=True)    # removes the LAST item
print("\nAfter popitem(last=True):", list(od.keys()))
# ['first', 'second']

od.popitem(last=False)   # removes the FIRST item
print("After popitem(last=False):", list(od.keys()))
# ['second']


# ----------------------------------------------------------
# Example 4: Order matters in equality
# ----------------------------------------------------------
a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print("\nAre the two OrderedDicts equal?", a == b)  # False (order differs)

# (Normal dicts would say True here, ignoring order.)


# ----------------------------------------------------------
# 🧠 WHEN TO USE:
#   Use OrderedDict when you need move_to_end(), ordered
#   equality, or want to be explicit that order matters
#   (great for building LRU caches in DSA!).
#
#   Run with:  python3 collections/3_ordereddict.py
# ----------------------------------------------------------
