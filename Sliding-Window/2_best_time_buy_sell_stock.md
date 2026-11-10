# 2. Best Time to Buy and Sell Stock — LeetCode 121

🔗 **LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
🔗 **NeetCode:** https://neetcode.io/problems/buy-and-sell-crypto
💻 **Code file:** [`2_best_time_buy_sell_stock.py`](2_best_time_buy_sell_stock.py)
🪟 **Window type:** Variable (expanding window with a moving left = cheapest buy)

---

## 📝 Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.
You want to **buy on one day** and **sell on a later day**. Return the **maximum
profit** you can achieve. If no profit is possible, return `0`.

**Examples**
```
[7,1,5,3,6,4] -> 5   (buy at 1, sell at 6)
[7,6,4,3,1]   -> 0   (prices only fall)
```

---

## 🪟 Sliding Window Approach (buy = left, sell = right)

Think of it as a window `[left, right]` where `left` is the **buy day** and
`right` is the **sell day**. We slide `right` forward one day at a time.

```
left  -> day we bought (the cheapest price so far)
right -> day we are considering selling
```

**Steps**
1. Start `left = 0` (buy on day 0), `best = 0`.
2. Move `right` forward.
3. If `prices[right] < prices[left]` → we found a **cheaper buy day**, so slide
   `left` to `right`.
4. Otherwise profit = `prices[right] - prices[left]` → update `best`.

**Why it works:** `left` always points at the lowest price seen so far. Selling
today against the cheapest earlier day gives the best profit ending today; the
overall answer is the max across all days.

---

## 💡 Tips to Remember

- "Buy low, sell high **later**" ⇒ track the **minimum so far**, maximise `price - min`.
- The window's `left` only moves when a **new minimum** appears.
- Never sell before you buy → `right` is always ahead of `left`.
- **Time:** O(n) • **Space:** O(1)

---

## 💻 Code

```python
def max_profit(prices: list[int]) -> int:
    left = 0            # buy day (cheapest so far)
    best = 0

    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            # Found a cheaper day to buy -> slide the window start
            left = right
        else:
            # Sell today against the cheapest buy day
            best = max(best, prices[right] - prices[left])

    return best
```

---

## ✅ Dry Run: `[7,1,5,3,6,4]`

| right | price | < buy? | left (buy) | profit | best |
|-------|-------|--------|------------|--------|------|
| 1 | 1 | yes | 1 (idx 1) | — | 0 |
| 2 | 5 | no | 1 | 4 | 4 |
| 3 | 3 | no | 1 | 2 | 4 |
| 4 | 6 | no | 1 | 5 | 5 |
| 5 | 4 | no | 1 | 3 | 5 |

Result: `5`
