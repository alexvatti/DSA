# 3. Koko Eating Bananas — LeetCode 875

🔗 **LeetCode:** https://leetcode.com/problems/koko-eating-bananas/
🔗 **Reference blog:** https://codeanddebug.in/blog/koko-eating-bananas-leetcode-875/
💻 **Code file:** [`3_koko_eating_bananas.py`](3_koko_eating_bananas.py)

---

## 📝 Problem

Koko has `piles` of bananas and `h` hours before the guards return.
Each hour she picks a pile and eats up to `k` bananas (if the pile has fewer,
she finishes it and waits the rest of the hour). Find the **minimum** eating
speed `k` so she finishes all bananas within `h` hours.

**Example**
```
piles = [3, 6, 7, 11], h = 8   ->  4
piles = [30, 11, 23, 4, 20], h = 5  ->  30
```

---

## 🔎 Binary Search on the ANSWER (not the array)

The array isn't the search space — the **speed `k`** is. Speed ranges from
`1` to `max(piles)`. The key insight is **monotonicity**:
- If speed `k` works (finishes in ≤ h hours), any **larger** speed also works.
- If speed `k` fails, any **smaller** speed also fails.

So the "works?" function is monotonic → binary search the smallest working `k`.

**Hours needed at speed k:** `sum(ceil(pile / k) for pile in piles)`.

**Steps**
1. `low = 1`, `high = max(piles)`.
2. While `low < high`:
3. `mid = (low + high) // 2`.
4. If `hours(mid) <= h` → `mid` might be the answer, try smaller → `high = mid`.
5. Else → too slow → `low = mid + 1`.
6. Return `low`.

---

## 💡 Tips to Remember

- "Minimum/maximum value such that a condition holds" ⇒ **binary search on answer**.
- Search space = range of possible answers (`1 .. max(piles)`), not indices.
- Build a monotonic **feasibility check** (`hours(k) <= h`).
- `ceil(a / b)` without floats: `(a + b - 1) // b`.
- **Time:** O(n · log(max pile)) • **Space:** O(1)

---

## 💻 Code

```python
import math

def min_eating_speed(piles, h):
    def hours_needed(k):
        return sum(math.ceil(pile / k) for pile in piles)

    low, high = 1, max(piles)

    while low < high:
        mid = (low + high) // 2
        if hours_needed(mid) <= h:
            high = mid        # mid works, try a slower speed
        else:
            low = mid + 1     # too slow, speed up

    return low
```

---

## ✅ Dry Run: `piles = [3, 6, 7, 11], h = 8`

| low | high | mid | hours(mid) | action |
|-----|------|-----|------------|--------|
| 1 | 11 | 6 | 1+1+2+2 = 6 ≤ 8 | high = 6 |
| 1 | 6  | 3 | 1+2+3+4 = 10 > 8 | low = 4 |
| 4 | 6  | 5 | 1+2+2+3 = 8 ≤ 8 | high = 5 |
| 4 | 5  | 4 | 1+2+2+3 = 8 ≤ 8 | high = 4 |
| 4 | 4  |   | low == high | return `4` |
