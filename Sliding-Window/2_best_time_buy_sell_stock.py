"""
============================================================
 2. BEST TIME TO BUY AND SELL STOCK (LeetCode 121)
============================================================

PROBLEM
-------
You are given an array `prices` where prices[i] is the price of a
stock on day i. Buy on one day and sell on a LATER day. Return the
maximum profit. If no profit is possible, return 0.

Example:
    [7,1,5,3,6,4] -> 5   (buy at 1, sell at 6)
    [7,6,4,3,1]   -> 0   (prices only fall)


SLIDING WINDOW APPROACH (buy = left, sell = right)
--------------------------------------------------
    left  -> day we bought (the cheapest price so far)
    right -> day we are considering selling

Step by step:
    1. Start left = 0 (buy on day 0), best = 0.
    2. Move `right` forward.
    3. If prices[right] < prices[left] -> cheaper buy day,
       slide left to right.
    4. Otherwise profit = prices[right] - prices[left] -> update best.

Why it works: `left` always points at the lowest price seen so far.
Selling today against the cheapest earlier day gives the best profit
ending today; the answer is the max across all days.


💡 TIPS TO REMEMBER
-------------------
- "Buy low, sell high later" => track the minimum so far.
- The window's left only moves when a new minimum appears.
- Never sell before you buy -> right stays ahead of left.
- Time: O(n)   Space: O(1)
"""


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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
    print(max_profit([1, 2]))              # 1
    print(max_profit([2]))                 # 0
