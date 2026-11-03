# 📦 Python `collections` Module — Beginner's Guide

Welcome! This folder teaches you the Python **`collections`** module step by step, from absolute basics to confident usage. Every topic has a simple explanation + runnable code.

---

## 🤔 What is `collections`?

Python gives you built-in data containers like `list`, `dict`, `set`, and `tuple`.
They are great — but sometimes you need **more powerful, specialized versions** of them.

The `collections` module is part of Python's **standard library** (already installed, nothing to download). It provides extra container data types that make your code **shorter, faster, and cleaner**.

Think of it like this:

> `list` and `dict` are like a basic toolbox 🔨
> `collections` gives you the **power tools** 🛠️⚡

You use it by importing it:

```python
import collections
# or import only what you need:
from collections import Counter, defaultdict, deque
```

---

## 🧭 What's inside this module?

| Tool | One-line purpose | File to learn |
|------|------------------|---------------|
| `Counter` | Count how many times things appear | [`1_counter.py`](1_counter.py) |
| `defaultdict` | A dict that never gives "KeyError" | [`2_defaultdict.py`](2_defaultdict.py) |
| `OrderedDict` | A dict that remembers insertion order | [`3_ordereddict.py`](3_ordereddict.py) |
| `deque` | A super-fast list for adding/removing at both ends | [`4_deque.py`](4_deque.py) |
| `namedtuple` | A tuple with named fields (like a mini class) | [`5_namedtuple.py`](5_namedtuple.py) |
| `ChainMap` | Combine many dicts into one view | [`6_chainmap.py`](6_chainmap.py) |

---

## 🚀 How to use this folder

1. Read this `README.md` first (you're doing it! ✅)
2. Open each numbered `.py` file in order.
3. Run each file to see the output:

   ```bash
   python3 collections/1_counter.py
   ```

4. Read the comments inside each file — they explain every line.
5. Try changing the values and run again to experiment!

---

## 📚 Learning order (recommended)

```
1. Counter       ← easiest, most useful, start here!
2. defaultdict   ← saves you from errors
3. OrderedDict   ← understand dict ordering
4. deque         ← important for DSA (queues/stacks)
5. namedtuple    ← cleaner than plain tuples
6. ChainMap      ← advanced, nice to know
```

---

## 💡 Why should a beginner learn this?

- ✅ Used **everywhere** in real Python code and interviews
- ✅ Makes DSA problems (like this repo!) much easier
- ✅ Writes less code and fewer bugs
- ✅ `Counter` and `deque` show up in **tons** of LeetCode problems

Happy learning! 🎉
