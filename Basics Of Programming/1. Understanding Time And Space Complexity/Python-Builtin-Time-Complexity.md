# Python Built-in Operations — Time Complexity Cheat Sheet

A quick, **readable reference** for the time complexity of common operations on Python's built-in data structures. Use this while analyzing and optimizing your code.

> 📚 **Source:** [Python Official Docs — TimeComplexity](https://docs.python.org/3/builtins/time-complexity.html) · [Python Wiki — TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

---

## 📋 List (Dynamic Array)

Python lists are implemented as **dynamic arrays**.

| Operation              | Example              | Average   | Worst     |
|------------------------|----------------------|-----------|-----------|
| Index access           | `lst[i]`             | O(1)      | O(1)      |
| Store by index         | `lst[i] = x`         | O(1)      | O(1)      |
| Append                 | `lst.append(x)`      | O(1)*     | O(1)*     |
| Pop (last)             | `lst.pop()`          | O(1)      | O(1)      |
| Pop (intermediate)     | `lst.pop(i)`         | O(n)      | O(n)      |
| Insert                 | `lst.insert(i, x)`   | O(n)      | O(n)      |
| Delete                 | `del lst[i]`         | O(n)      | O(n)      |
| Membership check       | `x in lst`           | O(n)      | O(n)      |
| Iteration              | `for x in lst`       | O(n)      | O(n)      |
| Get length             | `len(lst)`           | O(1)      | O(1)      |
| Slice                  | `lst[a:b]`           | O(b - a)  | O(b - a)  |
| Extend                 | `lst.extend(other)`  | O(k)      | O(k)      |
| Sort                   | `lst.sort()`         | O(n log n)| O(n log n)|
| Reverse                | `lst.reverse()`      | O(n)      | O(n)      |
| Min / Max              | `min(lst)`           | O(n)      | O(n)      |

> *`append` is **amortized** O(1). Occasionally the list resizes (O(n)), but averaged over many appends it is O(1).

---

## 🔗 Deque (`collections.deque`)

A **double-ended queue** — fast appends/pops from **both** ends.

| Operation              | Example                  | Average   |
|------------------------|--------------------------|-----------|
| Append right           | `dq.append(x)`           | O(1)      |
| Append left            | `dq.appendleft(x)`       | O(1)      |
| Pop right              | `dq.pop()`               | O(1)      |
| Pop left               | `dq.popleft()`           | O(1)      |
| Access middle element  | `dq[i]`                  | O(n)      |

> Use a **deque** instead of a list when you need fast operations at the **front** (lists are O(n) for `pop(0)` / `insert(0, x)`).

---

## 🗂️ Dictionary (Hash Map)

Python dictionaries are implemented as **hash tables**.

| Operation              | Example              | Average   | Worst     |
|------------------------|----------------------|-----------|-----------|
| Get item               | `d[k]`               | O(1)      | O(n)      |
| Set item               | `d[k] = v`           | O(1)      | O(n)      |
| Delete item            | `del d[k]`           | O(1)      | O(n)      |
| Membership check       | `k in d`             | O(1)      | O(n)      |
| Iteration              | `for k in d`         | O(n)      | O(n)      |
| Get length             | `len(d)`             | O(1)      | O(1)      |

> The **worst case** O(n) only happens with many hash collisions, which is **very rare** in practice. Treat dict operations as O(1).

---

## 🎯 Set (Hash Set)

Sets are also backed by **hash tables**.

| Operation              | Example              | Average   | Worst     |
|------------------------|----------------------|-----------|-----------|
| Add                    | `s.add(x)`           | O(1)      | O(n)      |
| Remove                 | `s.remove(x)`        | O(1)      | O(n)      |
| Membership check       | `x in s`             | O(1)      | O(n)      |
| Union                  | `a \| b`             | O(len(a)+len(b)) | — |
| Intersection           | `a & b`              | O(min(len(a), len(b))) | O(len(a)*len(b)) |
| Difference             | `a - b`              | O(len(a))  | —        |

> **Key tip:** Checking `x in my_set` is **O(1)**, while `x in my_list` is **O(n)**. Prefer sets for fast membership lookups.

---

## 🔤 String (Immutable)

Strings in Python are **immutable** — any "modification" creates a new string.

| Operation              | Example              | Complexity |
|------------------------|----------------------|------------|
| Index access           | `s[i]`               | O(1)       |
| Length                 | `len(s)`             | O(1)       |
| Concatenation          | `s1 + s2`            | O(n + m)   |
| Slice                  | `s[a:b]`             | O(b - a)   |
| Membership (substring) | `sub in s`           | O(n * m)   |
| Reverse                | `s[::-1]`            | O(n)       |
| `.join()` on list      | `"".join(list)`      | O(n)       |

> **Performance tip:** Building a string with `+=` inside a loop is O(n²). Instead, collect parts in a **list** and use `"".join(parts)` for O(n).

---

## ⚡ Quick Decision Guide

| If you need...                        | Use a...      | Why                         |
|---------------------------------------|---------------|-----------------------------|
| Fast index access                     | **List**      | O(1) indexing               |
| Fast membership testing               | **Set / Dict**| O(1) lookups                |
| Fast insert/remove at both ends       | **Deque**     | O(1) both ends              |
| Key → value mapping                   | **Dict**      | O(1) access                 |
| Ordered, resizable sequence           | **List**      | dynamic array               |

---

## Key Takeaways

- **List indexing** and **dict/set lookups** are the workhorses: O(1).
- Avoid `list.insert(0, x)` / `list.pop(0)` in loops → use a **deque**.
- Avoid string concatenation in loops → use `"".join()`.
- Membership (`in`) is **O(1)** for sets/dicts but **O(n)** for lists.

---

[🔙 Back to Basics Of Programming](../README.md)
