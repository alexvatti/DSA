# Problem-Solving Fundamentals

A beginner-friendly guide to the foundations of Data Structures and
Algorithms (DSA) using Python.

## 1. Logical Thinking and Problem-Solving

Problem-solving is the process of understanding a problem, planning a
solution, implementing it, and checking that the result is correct.

### A practical problem-solving process

1.  **Understand the problem** -- Read it carefully. Identify what is
    given and what must be produced.
2.  **Identify inputs and outputs** -- Note the input type, expected
    output, and constraints.
3.  **Work through an example** -- Solve a small example manually.
4.  **Break the problem into steps** -- Convert the solution into
    simple, ordered instructions.
5.  **Choose an approach** -- Decide whether a loop, function, data
    structure, or recursion is suitable.
6.  **Write the code** -- Implement the steps in Python.
7.  **Test the solution** -- Check normal cases, boundary cases, and
    invalid or unusual inputs.
8.  **Improve the solution** -- Consider whether it can be made simpler
    or more efficient.

### Example: Find the largest number in a list

**Problem:** Given a list of numbers, return the largest value.

``` python
numbers = [12, 5, 27, 9, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)  # 27
```

**Logic:** Start by treating the first element as the largest. Visit
each remaining element and update the largest value whenever a bigger
number is found.

**Important habits** - Do not start coding before understanding the
problem. - Trace the logic with a small example. - Consider empty input,
one element, duplicates, and negative values. - Prefer clear and correct
code before trying to optimize it.

## 2. Time and Space Complexity

Complexity describes how an algorithm's resource requirements grow as
the input size increases.

-   **Time complexity:** How the number of operations grows with input
    size.
-   **Space complexity:** How the extra memory used by an algorithm
    grows with input size.

Here, `n` usually represents the number of input elements.

### Time complexity examples

**O(1) -- Constant time**

The number of operations does not grow with `n`.

``` python
def first_element(items):
    return items[0]
```

Accessing one list element by index takes constant time.

**O(n) -- Linear time**

The work grows proportionally with the number of elements.

``` python
def print_items(items):
    for item in items:
        print(item)
```

The loop visits each element once.

**O(n²) -- Quadratic time**

A nested loop may perform approximately `n × n` operations.

``` python
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)
```

For `n` elements, the inner operation runs `n²` times.

### Space complexity examples

**O(1) auxiliary space:** Uses a fixed amount of extra memory.

``` python
total = 0
for number in numbers:
    total += number
```

The variable `total` is the only additional storage, regardless of list
length.

**O(n) auxiliary space:** Extra memory grows with input size.

``` python
squares = []

for number in numbers:
    squares.append(number * number)
```

The new list stores one result for every input element.

> Note: Space complexity is often discussed as *auxiliary space* (extra
> memory used by the algorithm), excluding the input itself. Always
> check which convention a question uses.

## 3. Big O Notation

Big O notation describes an upper-bound growth rate for an algorithm as
input size becomes large. It helps compare algorithms independently of a
particular computer or programming language.

### Common complexity classes

  Complexity   Name           Typical example
  ------------ -------------- --------------------------------------------
  O(1)         Constant       Access an array element by index
  O(log n)     Logarithmic    Binary search on sorted data
  O(n)         Linear         Scan a list once
  O(n log n)   Linearithmic   Merge sort
  O(n²)        Quadratic      Compare every pair using nested loops
  O(2ⁿ)        Exponential    Some recursive subset-generation solutions

### Rules for estimating Big O

1.  **Ignore constant factors:** `O(2n)` becomes `O(n)`.
2.  **Keep the fastest-growing term:** `O(n² + n + 5)` becomes `O(n²)`.
3.  **Sequential operations:** Add their costs, then keep the dominant
    term. For example, `O(n) + O(n²) = O(n²)`.
4.  **Nested loops:** Multiply iteration counts when the loops each
    depend on the input size. Two full `n` loops usually give `O(n²)`.
5.  **Halving the search space:** Repeatedly dividing the problem size
    by two usually gives `O(log n)`.

### Example: Estimate the complexity

``` python
def find_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

The loop runs once for each of the `n` elements. Therefore:

-   Time complexity: **O(n)**
-   Auxiliary space complexity: **O(1)**

### Why Big O matters

Suppose two solutions both produce the correct answer. One takes O(n)
time and another takes O(n²) time. For small inputs, the difference may
be minor. For large inputs, the O(n) solution will generally scale much
better.

Big O describes growth, not exact execution time. Actual performance
also depends on implementation, hardware, input data, and constant
factors.

## 4. Iterative vs Recursive Approaches

An algorithm can solve a problem using repetition (iteration) or by
calling itself on smaller versions of the problem (recursion).

### Iteration

Iteration uses loops such as `for` and `while`.

**Example: Sum numbers from 1 to n**

``` python
def sum_iterative(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total

print(sum_iterative(5))  # 15
```

-   Uses a loop.
-   Usually uses O(1) auxiliary space for this example.
-   Avoids recursive function-call overhead.

### Recursion

Recursion occurs when a function calls itself. A recursive solution
needs:

-   **Base case:** The condition that stops further calls.
-   **Recursive case:** The step that reduces the problem toward the
    base case.

**Example: Sum numbers from 1 to n**

``` python
def sum_recursive(n):
    if n == 0:              # Base case
        return 0

    return n + sum_recursive(n - 1)  # Recursive case

print(sum_recursive(5))  # 15
```

The calls reduce the problem as follows:

``` text
sum_recursive(5)
5 + sum_recursive(4)
5 + 4 + sum_recursive(3)
5 + 4 + 3 + sum_recursive(2)
5 + 4 + 3 + 2 + sum_recursive(1)
5 + 4 + 3 + 2 + 1 + sum_recursive(0)
5 + 4 + 3 + 2 + 1 + 0
15
```

For this example: - Time complexity: **O(n)** - Auxiliary space
complexity: **O(n)** because the call stack holds up to `n` function
calls.

### Iteration vs Recursion

  -----------------------------------------------------------------------
  Feature                 Iteration               Recursion
  ----------------------- ----------------------- -----------------------
  Main mechanism          Loops                   Function calls

  Stopping condition      Loop condition          Base case

  Memory                  Often lower             Uses call stack

  Best suited for         Repeated steps and      Naturally recursive
                          simple traversal        structures and
                                                  divide-and-conquer

  Common risk             Infinite loop           Missing base case or
                                                  excessive call depth
  -----------------------------------------------------------------------

### Python recursion note

Python limits the depth of recursive calls. Deep recursion can raise a
`RecursionError`. When a loop is simpler or safer, prefer iteration.
Recursion is especially useful for understanding tree traversal,
backtracking, and divide-and-conquer algorithms.

## 5. Quick Practice Questions

1.  What are the input and output of a function that finds the minimum
    value in a list?
2.  What is the time complexity of accessing `items[3]` in a Python
    list?
3.  What is the time complexity of a loop that visits all `n` elements
    once?
4.  What is the time complexity of two nested loops that each run `n`
    times?
5.  What is the difference between time complexity and space complexity?
6.  Why does binary search require sorted data?
7.  What is the base case in a recursive function?
8.  Why can deep recursion be a problem in Python?
9.  Write iterative and recursive solutions to calculate the factorial
    of a positive integer.
10. Estimate the time and auxiliary space complexity of each solution.

## 6. Key Takeaways

-   Understand the problem and plan before coding.
-   Test logic with examples and edge cases.
-   Time complexity describes growth in work; space complexity describes
    growth in memory.
-   Big O helps compare how algorithms scale.
-   Iteration uses loops; recursion uses function calls and requires a
    base case.
-   Correctness comes first; optimize after understanding the solution.

------------------------------------------------------------------------

**Recommended learning order:** Logical problem-solving → Time and space
complexity → Big O analysis → Iteration → Recursion → Practice problems.
