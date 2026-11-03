# 6. Time Based Key-Value Store — LeetCode 981

🔗 **LeetCode:** https://leetcode.com/problems/time-based-key-value-store/
🔗 **Reference blog:** https://codeanddebug.in/blog/time-based-key-value-store-leetcode-981/
💻 **Code file:** [`6_time_based_kv_store.py`](6_time_based_kv_store.py)

---

## 📝 Problem

Design a store with two operations:
- `set(key, value, timestamp)` — store the value at the given timestamp.
- `get(key, timestamp)` — return the value with the **largest timestamp ≤ the
  query timestamp**. If none exists, return `""`.

Timestamps for each key are **strictly increasing** across `set` calls.

**Example**
```
set("foo", "bar", 1)
get("foo", 1)   -> "bar"
get("foo", 3)   -> "bar"   (latest with ts <= 3)
set("foo", "bar2", 4)
get("foo", 4)   -> "bar2"
get("foo", 5)   -> "bar2"
```

---

## 🔎 Approach — binary search on timestamps

Store each key's history as a list of `(timestamp, value)` pairs. Since
timestamps arrive increasing, the list is **already sorted** → `set` is O(1)
append. For `get`, binary search for the **rightmost** timestamp `<= query`
(a "floor" / upper-bound style search).

**get(key, t) steps**
1. If key absent → return `""`.
2. Binary search the pairs for the largest `timestamp <= t`.
3. Track the best candidate as you go; move `low`/`high` accordingly.
4. Return the best value found, else `""`.

---

## 💡 Tips to Remember

- "Latest value at or before a time" ⇒ binary search for the **floor**.
- Appends come sorted, so no re-sorting needed — just append.
- This is the **upper-bound** pattern: find rightmost element `<= target`.
- Keep a `result` variable and update it whenever `pairs[mid].ts <= t`.
- **set:** O(1) • **get:** O(log n) • **Space:** O(n)

---

## 💻 Code

```python
class TimeMap:
    def __init__(self):
        self.store = {}   # key -> list of [timestamp, value]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        pairs = self.store.get(key, [])
        result = ""
        low, high = 0, len(pairs) - 1

        while low <= high:
            mid = (low + high) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]   # candidate; look for a later one
                low = mid + 1
            else:
                high = mid - 1

        return result
```

---

## ✅ Dry Run

```
set("foo","bar",1); set("foo","bar2",4)
pairs = [[1,"bar"], [4,"bar2"]]

get("foo", 3):
  low=0, high=1, mid=0 -> ts 1 <= 3 -> result="bar", low=1
  low=1, high=1, mid=1 -> ts 4 > 3  -> high=0
  loop ends -> return "bar"

get("foo", 5):
  mid=0 -> 1<=5 -> result="bar", low=1
  mid=1 -> 4<=5 -> result="bar2", low=2
  loop ends -> return "bar2"
```
