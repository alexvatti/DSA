"""
============================================================
 1. Counter  —  Count things easily
============================================================

WHAT IS IT?
-----------
`Counter` is a special dictionary whose job is to COUNT things.
You give it a list (or string), and it tells you how many times
each item appears.

WHY USE IT?
-----------
Without Counter, counting looks like this (long + error-prone):

    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

With Counter, it becomes ONE line. 🎉
"""

from collections import Counter


# ----------------------------------------------------------
# Example 1: Count letters in a word
# ----------------------------------------------------------
word = "banana"
letter_counts = Counter(word)
print("Letter counts in 'banana':", letter_counts)
# Output: Counter({'a': 3, 'n': 2, 'b': 1})


# ----------------------------------------------------------
# Example 2: Count items in a list
# ----------------------------------------------------------
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_counts = Counter(fruits)
print("\nFruit counts:", fruit_counts)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})


# ----------------------------------------------------------
# Example 3: Access a single count (like a dictionary)
# ----------------------------------------------------------
print("\nHow many apples?", fruit_counts["apple"])   # 3

# NOTE: Asking for something that doesn't exist returns 0 (not an error!)
print("How many grapes?", fruit_counts["grape"])      # 0


# ----------------------------------------------------------
# Example 4: most_common() — find the top items
# ----------------------------------------------------------
# .most_common(n) gives the n most frequent items, sorted.
print("\nTop 2 fruits:", fruit_counts.most_common(2))
# Output: [('apple', 3), ('banana', 2)]


# ----------------------------------------------------------
# Example 5: Counters can do math!
# ----------------------------------------------------------
basket1 = Counter(["apple", "apple", "banana"])
basket2 = Counter(["apple", "orange"])

print("\nCombine two baskets (add):", basket1 + basket2)
# Counter({'apple': 3, 'banana': 1, 'orange': 1})

print("Subtract baskets:", basket1 - basket2)
# Counter({'apple': 1, 'banana': 1})


# ----------------------------------------------------------
# 🧠 TRY IT YOURSELF:
#   Change `word` to your own name and run the file again!
#   Run with:  python3 collections/1_counter.py
# ----------------------------------------------------------
