# 7. Median of Two Sorted Arrays — LeetCode 4

🔗 **LeetCode:** https://leetcode.com/problems/median-of-two-sorted-arrays/
🔗 **Reference blog:** https://codeanddebug.in/blog/median-of-two-sorted-arrays/
💻 **Code file:** [`7_median_two_sorted.py`](7_median_two_sorted.py)

---

## 📝 Problem

Given two sorted arrays `nums1` and `nums2`, return the **median** of the
combined sorted array in **O(log(m + n))**.

**Example**
```
nums1 = [1, 3], nums2 = [2]        ->  2.0
nums1 = [1, 2], nums2 = [3, 4]     ->  2.5   ((2 + 3) / 2)
```

---

## 🔎 Approach — binary search the partition

We don't merge the arrays. Instead we **partition** both so that the left
side contains exactly half the total elements, with **everything on the left
≤ everything on the right**.

Binary search the **smaller** array for a cut `i`; the cut `j` in the other
array is forced by `j = half - i`. At each cut define:

```
L1 = nums1[i-1]  (or -inf)      R1 = nums1[i]  (or +inf)
L2 = nums2[j-1]  (or -inf)      R2 = nums2[j]  (or +inf)
```

- If `L1 <= R2` **and** `L2 <= R1` → correct partition found.
- If `L1 > R2` → cut `i` is too far right → move left (`high = i - 1`).
- If `L2 > R1` → cut `i` is too far left → move right (`low = i + 1`).

**Median**
- Total even → `(max(L1, L2) + min(R1, R2)) / 2`.
- Total odd → `max(L1, L2)`.

---

## 💡 Tips to Remember

- Always binary search the **smaller** array to keep it O(log(min(m, n))).
- Use `-inf` / `+inf` sentinels for cuts at the array edges (no edge-case spaghetti).
- Correct partition condition: `L1 <= R2 and L2 <= R1`.
- `half = (m + n + 1) // 2` makes the odd case put the extra element on the left.
- **Time:** O(log(min(m, n))) • **Space:** O(1)

---

## 💻 Code

```python
def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    low, high = 0, m
    while low <= high:
        i = (low + high) // 2     # cut in nums1
        j = half - i              # cut in nums2

        L1 = nums1[i - 1] if i > 0 else float('-inf')
        R1 = nums1[i]     if i < m else float('inf')
        L2 = nums2[j - 1] if j > 0 else float('-inf')
        R2 = nums2[j]     if j < n else float('inf')

        if L1 <= R2 and L2 <= R1:
            if total % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            return float(max(L1, L2))
        elif L1 > R2:
            high = i - 1          # move cut left
        else:
            low = i + 1           # move cut right

    return 0.0  # inputs guaranteed valid; unreachable
```

---

## ✅ Dry Run: `nums1 = [1, 2], nums2 = [3, 4]`

```
m=2, n=2, total=4, half=2
low=0, high=2, i=1, j=1
  L1=nums1[0]=1, R1=nums1[1]=2
  L2=nums2[0]=3, R2=nums2[1]=4
  L1(1)<=R2(4) ? yes ; L2(3)<=R1(2) ? NO  -> L2 > R1 -> low = 2

low=2, high=2, i=2, j=0
  L1=nums1[1]=2, R1=+inf
  L2=-inf,       R2=nums2[0]=3
  L1(2)<=R2(3) yes ; L2(-inf)<=R1(+inf) yes -> partition!
  total even -> (max(2,-inf) + min(+inf,3)) / 2 = (2 + 3)/2 = 2.5
```
