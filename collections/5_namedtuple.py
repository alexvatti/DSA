"""
============================================================
 5. namedtuple  —  A tuple with NAMES for its fields
============================================================

THE PROBLEM WITH NORMAL TUPLES
------------------------------
A tuple stores data by POSITION:

    point = (3, 5)
    print(point[0])   # 3 ... but what is index 0? x? y? who knows!

Using numbers (point[0], point[1]) is confusing and easy to
get wrong.

THE SOLUTION
------------
`namedtuple` lets you give each position a NAME. Now you can
write point.x instead of point[0]. Much clearer! 🎉

It's like a lightweight, read-only mini-class.
"""

from collections import namedtuple


# ----------------------------------------------------------
# Step 1: Define the structure (like a blueprint)
# ----------------------------------------------------------
# namedtuple("Name", [list of field names])
Point = namedtuple("Point", ["x", "y"])


# ----------------------------------------------------------
# Step 2: Create instances
# ----------------------------------------------------------
p1 = Point(3, 5)
p2 = Point(x=10, y=20)   # you can also use the names

print("p1:", p1)   # Point(x=3, y=5)
print("p2:", p2)   # Point(x=10, y=20)


# ----------------------------------------------------------
# Step 3: Access fields by NAME (the whole point!)
# ----------------------------------------------------------
print("\np1.x =", p1.x)   # 3   <- clear and readable!
print("p1.y =", p1.y)     # 5

# It still works like a tuple by index too, if you want:
print("p1[0] =", p1[0])   # 3


# ----------------------------------------------------------
# Example: A more real-world use
# ----------------------------------------------------------
Student = namedtuple("Student", ["name", "age", "grade"])

alice = Student(name="Alice", age=20, grade="A")
print("\nStudent info:")
print("  Name:", alice.name)
print("  Age:", alice.age)
print("  Grade:", alice.grade)


# ----------------------------------------------------------
# Handy feature: _asdict() turns it into a dictionary
# ----------------------------------------------------------
print("\nAs a dictionary:", alice._asdict())
# {'name': 'Alice', 'age': 20, 'grade': 'A'}


# ----------------------------------------------------------
# Handy feature: _replace() makes a NEW copy with a change
# ----------------------------------------------------------
# (namedtuples can't be changed directly — they're read-only)
older_alice = alice._replace(age=21)
print("\nOriginal:", alice)        # age still 20
print("Updated copy:", older_alice)  # age now 21


# ----------------------------------------------------------
# 🧠 KEY IDEA:
#   namedtuple = readable tuples. Use .name instead of [0].
#   Great for returning multiple values with clear meaning.
#
#   Run with:  python3 collections/5_namedtuple.py
# ----------------------------------------------------------
