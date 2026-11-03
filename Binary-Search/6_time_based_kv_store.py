"""
============================================================
 6. TIME BASED KEY-VALUE STORE   (LeetCode 981)
============================================================
 Reference: https://codeanddebug.in/blog/time-based-key-value-store-leetcode-981/

PROBLEM
-------
Design a store with:
    - set(key, value, timestamp): store value at the given timestamp.
    - get(key, timestamp): return the value with the LARGEST timestamp
      that is <= the query timestamp. If none, return "".

Timestamps for each key are strictly increasing across set() calls.

Example:
    set("foo", "bar", 1)
    get("foo", 3)  -> "bar"
    set("foo", "bar2", 4)
    get("foo", 4)  -> "bar2"
    get("foo", 5)  -> "bar2"


APPROACH — binary search on timestamps
---------------------------------------
Store each key's history as a list of [timestamp, value] pairs. Because
timestamps arrive increasing, the list is already sorted -> set is O(1)
append. For get, binary search for the RIGHTMOST timestamp <= query
(a "floor" / upper-bound search).

get(key, t) steps:
    1. If key absent -> return "".
    2. Binary search pairs for the largest timestamp <= t.
    3. Track the best candidate; move low/high accordingly.
    4. Return the best value found, else "".


💡 TIPS TO REMEMBER
-------------------
- "Latest value at or before a time" => binary search for the FLOOR.
- Appends come sorted, so no re-sorting needed.
- Upper-bound pattern: find rightmost element <= target.
- Keep a result variable; update when pairs[mid].ts <= t, then go right.
- set: O(1)   get: O(log n)   Space: O(n)
"""


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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # "bar"
    print(tm.get("foo", 3))   # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # "bar2"
    print(tm.get("foo", 5))   # "bar2"
    print(tm.get("foo", 0))   # ""  (nothing at or before ts 0)
    print(tm.get("missing", 1))  # ""
