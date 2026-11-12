# 5. Subarray Sum Equals K — LeetCode 560

🔗 **LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/
💻 **Code file:** [`5_subarray_sum_equals_k.py`](5_subarray_sum_equals_k.py)

---

## 📝 Problem

Given an integer array `nums` (negatives allowed) and an integer `k`, return the
**number** of contiguous subarrays whose sum equals `k`.

**Examples**
```
nums = [1, 1, 1], k = 2  -> 2
nums = [1, 2, 3], k = 3  -> 2   ([1,2] and [3])
```

---

## 🗂️ Prefix Sum + Hash Map

Negatives break sliding window, so use **prefix sums**.

```
sum(j+1 .. i) = prefix[i] - prefix[j]
want = k   ⇒   prefix[j] = prefix[i] - k
```

At each `i`, ask: **"how many earlier prefixes equal `prefix - k`?"**

```
freq = { prefix_sum : times seen }      start with {0: 1}
```

**Steps**
1. `prefix += nums[i]`
2. `count += freq.get(prefix - k, 0)`
3. `freq[prefix] += 1`

`{0: 1}` is the empty prefix — it lets subarrays that start at index 0 count.

---

## 💡 Tips to Remember

- "Count subarrays with sum k" (negatives allowed) ⇒ **prefix sum + map**.
- Look up **before** inserting the current prefix.
- Never forget `freq = {0: 1}`.
- **Time:** O(n) • **Space:** O(n)

---

## 💻 Code

```python
def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    freq = {0: 1}                 # the empty prefix

    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)       # earlier prefixes that fit
        freq[prefix] = freq.get(prefix, 0) + 1

    return count
```

---

## ✅ Dry Run: `nums = [1, 2, 3]`, `k = 3`

| x | prefix | prefix − k | found | count | freq after |
|---|--------|-----------|-------|-------|------------|
| — | 0 | — | — | 0 | `{0:1}` |
| 1 | 1 | −2 | 0 | 0 | `{0:1, 1:1}` |
| 2 | 3 | 0 | 1 (`[1,2]`) | 1 | `{0:1, 1:1, 3:1}` |
| 3 | 6 | 3 | 1 (`[3]`) | 2 | `{…, 6:1}` |

Result: `2`
