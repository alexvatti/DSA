# Time Complexity and Space Complexity

> 📚 **Source:** [codeanddebug.in — Time Complexity and Space Complexity](https://codeanddebug.in/blog/time-complexity-and-space-complexity/)

Understanding **Time Complexity** and **Space Complexity** is the foundation of writing efficient code. Before learning any Data Structure or Algorithm, you must understand how to measure the *efficiency* of your program.

---

## Why Do We Need Complexity Analysis?

Imagine two people solving the same problem:
- Person A writes code that runs in **1 second**.
- Person B writes code that runs in **100 seconds**.

Both give the *correct answer*, but Person A's solution is **better** because it is faster. Complexity analysis gives us a way to measure and compare solutions **without depending on the machine, programming language, or compiler**.

> We do **not** measure efficiency in seconds, because time depends on the hardware. Instead, we measure how the number of operations **grows** as the input size grows.

---

## What is Time Complexity?

**Time Complexity** is the amount of time taken by an algorithm to run, as a function of the length of the input (`n`).

It is **not** the actual running time, but rather **how the running time grows** as the input size increases.

### Example

```python
# Print all elements of a list
def print_list(arr):
    for element in arr:   # runs n times
        print(element)
```

If the list has `n` elements, the loop runs `n` times. So the time complexity is **O(n)**.

---

## What is Big O Notation?

**Big O Notation** describes the **upper bound** (worst case) of an algorithm's growth rate. It tells us how the algorithm behaves when the input becomes very large.

We ignore constants and lower-order terms because, for large `n`, they do not matter much.

```
O(2n)        -> O(n)
O(n² + n)    -> O(n²)
O(500)       -> O(1)
```

---

## Common Time Complexities (Best to Worst)

| Notation      | Name          | Example                                 |
|---------------|---------------|-----------------------------------------|
| **O(1)**      | Constant      | Accessing an array element by index     |
| **O(log n)**  | Logarithmic   | Binary Search                           |
| **O(n)**      | Linear        | Traversing a loop once                  |
| **O(n log n)**| Linearithmic  | Merge Sort, Quick Sort (average)        |
| **O(n²)**     | Quadratic     | Nested loops (Bubble Sort)              |
| **O(2ⁿ)**     | Exponential   | Recursive Fibonacci                     |
| **O(n!)**     | Factorial     | Travelling Salesman (brute force)       |

### Growth Visualization

```
Operations
   |
   |                                    O(n!)   O(2ⁿ)
   |                               /       /
   |                          /       /
   |                     /       /         O(n²)
   |                /       /         /
   |           /       /        /          O(n log n)
   |      /       /        /         ____--- O(n)
   |  /      /       ____---____-------      O(log n)
   |_/__----_______-----------------------  O(1)
   +---------------------------------------> Input size (n)
```

---

## Examples of Each Time Complexity

### O(1) — Constant Time

The operation takes the same time regardless of input size.

```python
def get_first(arr):
    return arr[0]   # Always one operation
```

### O(log n) — Logarithmic Time

The input is halved at every step (classic Binary Search).

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### O(n) — Linear Time

Time grows directly in proportion to the input size.

```python
def find_max(arr):
    maximum = arr[0]
    for num in arr:      # n iterations
        if num > maximum:
            maximum = num
    return maximum
```

### O(n²) — Quadratic Time

A loop inside a loop. Common in brute-force solutions.

```python
def print_pairs(arr):
    for i in arr:          # n times
        for j in arr:      # n times for each i
            print(i, j)    # total n * n = n² operations
```

---

## Best, Average and Worst Case

Consider searching for an element in a list:

- **Best Case (Ω)** — The element is the **first** one → O(1)
- **Average Case (Θ)** — The element is somewhere in the **middle** → O(n/2)
- **Worst Case (O)** — The element is the **last** or **not present** → O(n)

> In interviews and analysis, we usually focus on the **Worst Case (Big O)**.

---

## What is Space Complexity?

**Space Complexity** is the total amount of **memory** an algorithm uses relative to the input size.

It includes:
1. **Input Space** — Memory to store the input itself.
2. **Auxiliary Space** — Extra/temporary memory used by the algorithm.

> **Space Complexity = Input Space + Auxiliary Space**
> Often, we focus on **Auxiliary Space** when comparing algorithms.

### Example: O(1) Space

```python
def sum_array(arr):
    total = 0          # only one extra variable
    for num in arr:
        total += num
    return total
```
Uses a single variable → **O(1)** auxiliary space.

### Example: O(n) Space

```python
def double_array(arr):
    result = []              # new list grows with input
    for num in arr:
        result.append(num * 2)
    return result
```
Creates a new list of size `n` → **O(n)** auxiliary space.

---

## Rules to Calculate Time Complexity

1. **Drop the constants:** `O(2n)` becomes `O(n)`.
2. **Drop lower-order terms:** `O(n² + n + 100)` becomes `O(n²)`.
3. **Add complexities of sequential loops:** `O(n) + O(n) = O(2n) = O(n)`.
4. **Multiply complexities of nested loops:** `O(n) * O(n) = O(n²)`.

### Worked Example

```python
def example(arr):
    # Block 1: O(n)
    for x in arr:
        print(x)

    # Block 2: O(n²)
    for i in arr:
        for j in arr:
            print(i, j)
```

Total = `O(n) + O(n²)` = **O(n²)** (we keep the dominant term).

---

## Key Takeaways

- Complexity analysis helps compare algorithms **independent of hardware**.
- **Big O** describes the worst-case growth rate.
- Always aim for the **lowest** possible time and space complexity.
- There is often a **trade-off**: using more memory (space) can reduce time, and vice versa.

---

[🔙 Back to Basics Of Programming](../README.md)
