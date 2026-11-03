"""
============================================================
 2. defaultdict  —  A dictionary that never crashes
============================================================

THE PROBLEM
-----------
With a normal dict, reading a missing key gives an ERROR:

    d = {}
    d["x"] += 1        # ❌ KeyError: 'x' does not exist yet!

You always have to check "does this key exist?" first. Annoying.

THE SOLUTION
------------
`defaultdict` automatically creates a default value for any
missing key. No more KeyError! 🎉

You tell it what the default should be by passing a "type":
    defaultdict(int)   -> missing keys default to 0
    defaultdict(list)  -> missing keys default to []
    defaultdict(set)   -> missing keys default to set()
"""

from collections import defaultdict


# ----------------------------------------------------------
# Example 1: Counting with defaultdict(int)
# ----------------------------------------------------------
# int() returns 0, so every new key starts at 0 automatically.
counts = defaultdict(int)

for letter in "mississippi":
    counts[letter] += 1   # no KeyError, even on first time!

print("Letter counts:", dict(counts))
# Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}


# ----------------------------------------------------------
# Example 2: Grouping with defaultdict(list)
# ----------------------------------------------------------
# list() returns [], so we can .append() right away.
students = [
    ("Math", "Alice"),
    ("Science", "Bob"),
    ("Math", "Charlie"),
    ("Science", "Dave"),
    ("Math", "Eve"),
]

groups = defaultdict(list)
for subject, name in students:
    groups[subject].append(name)   # no need to create the list first

print("\nStudents grouped by subject:")
for subject, names in groups.items():
    print(f"  {subject}: {names}")
# Math: ['Alice', 'Charlie', 'Eve']
# Science: ['Bob', 'Dave']


# ----------------------------------------------------------
# Example 3: defaultdict(set) — group unique values
# ----------------------------------------------------------
# set() avoids duplicates automatically.
owners = defaultdict(set)
owners["cat"].add("Alice")
owners["cat"].add("Alice")   # duplicate ignored
owners["dog"].add("Bob")

print("\nPet owners (no duplicates):", dict(owners))
# {'cat': {'Alice'}, 'dog': {'Bob'}}


# ----------------------------------------------------------
# 🧠 KEY IDEA:
#   Normal dict  -> missing key = CRASH
#   defaultdict  -> missing key = safe default value
#
#   Run with:  python3 collections/2_defaultdict.py
# ----------------------------------------------------------
