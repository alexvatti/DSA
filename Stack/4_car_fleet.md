# 4. Car Fleet — LeetCode 853

🔗 **LeetCode:** https://leetcode.com/problems/car-fleet/
💻 **Code file:** [`4_car_fleet.py`](4_car_fleet.py)
🥞 **Stack type:** Monotonic stack (arrival times)

---

## 📝 Problem

`n` cars drive toward the same `target` on a one-lane road. `position[i]` and `speed[i]` are given.
A car **cannot pass** another; if it catches up it slows down and **joins that car's fleet**.
Return the number of **fleets** that arrive at the target.

**Examples**
```
target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
target=10, position=[3],            speed=[3]         -> 1
target=100, position=[0,2,4],       speed=[4,2,1]     -> 1
```

---

## 🥞 Approach — Sort by position + stack of arrival times

Process cars from **closest to the target to farthest**. A car's solo arrival time is `(target - position) / speed`. If it would arrive **no later** than the fleet right ahead, it catches up and merges; if it arrives **later**, it forms a new fleet.

```
stack -> arrival time of each fleet (front fleet first)
```

**Steps**
1. Sort cars by position, **largest first**.
2. For each car compute `time = (target - pos) / speed`.
3. If the stack is empty or `time` is **greater** than the top → push (a **new fleet**).
4. Otherwise (`time ≤ top`) it merges into the fleet ahead → do nothing.
5. Answer = `len(stack)`.

**Why it works:** A car can only be blocked by the fleet directly ahead, whose pace is that fleet's slowest (largest) time. Arriving sooner than that is impossible, so it merges.

---

## 💡 Tips to Remember

- "Cannot overtake" ⇒ the slower car ahead sets the pace for everything behind it.
- Sort by position first — the logic only works front → back.
- Use `>` not `>=`: equal arrival times reach the target together, so they are **one** fleet.
- Only the last time matters, but keeping the stack makes the pattern clear.
- **Time: O(n log n) (sorting) • Space: O(n)**

---

## 💻 Code

```python
def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    # Closest to the target first
    cars = sorted(zip(position, speed), reverse=True)
    stack = []  # arrival time of each fleet

    for pos, spd in cars:
        time = (target - pos) / spd
        # Arrives later than the fleet ahead -> cannot catch it -> new fleet
        if not stack or time > stack[-1]:
            stack.append(time)
        # else: catches up and merges, nothing to push

    return len(stack)
```

---

## ✅ Dry Run: `target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]`

| car (pos, speed) | time | vs top | action | stack after |
|------------------|------|--------|--------|-------------|
| (10, 2) | 1 | empty | push | `[1]` |
| (8, 4) | 1 | 1 ≤ 1 | merge | `[1]` |
| (5, 1) | 7 | 7 > 1 | push | `[1, 7]` |
| (3, 3) | 3 | 3 ≤ 7 | merge | `[1, 7]` |
| (0, 1) | 12 | 12 > 7 | push | `[1, 7, 12]` |

`len(stack)` = `3` fleets
