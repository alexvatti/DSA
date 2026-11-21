"""
============================================================
 10. SUBSETS   (Backtracking: choose / explore / undo)
============================================================

PROBLEM
-------
Given a list of distinct numbers, return all possible subsets (the power set).

Examples:
    subsets([1, 2]) = [[], [1], [2], [1, 2]]
    subsets([1, 2, 3]) has 8 subsets


THE 4 METHODS  (same answer, four ways)
---------------------------------------
 1. LOOP
      Start with [[]]. For every number, copy all subsets found so far
      and add the number to each copy.
 2. RECURSION
      For each number there are two choices: SKIP it or TAKE it. When
      all numbers are decided, the path is a subset.
 3. RECURSION + OUR OWN STACK
      The stack holds (i, path) pairs: "numbers decided so far" and
      "what I picked". Pop one; if every number is decided save
      it, else push TAKE and SKIP.
 4. OUR OWN STACK + BACKTRACKING
      The LeetCode template. ONE shared path. 'go' j = CHOOSE nums[j]
      (append), record the path, leave a 'back' frame, then push
      the next choices. 'back' = UNDO (pop).


💡 TAKEAWAY
-----------
Every LeetCode backtracking problem is this loop: choose → record →
explore → UNDO. With your own stack, "back" frames do the undo.

LEETCODE
--------
LC 78 · Subsets -> https://leetcode.com/problems/subsets/
also: LC 46 · Permutations -> https://leetcode.com/problems/permutations/
also: LC 39 · Combination Sum -> https://leetcode.com/problems/combination-sum/
also: LC 90 · Subsets II -> https://leetcode.com/problems/subsets-ii/
"""

from stack_base import Stack      # OUR OWN STACK: push / pop / is_empty  (see stack_base.py)

# ----------------------------------------------------------
# METHOD 1 — LOOP
# ----------------------------------------------------------
def subsets_loop(nums):
    result = [[]]
    for x in nums:
        for i in range(len(result)):
            result.append(result[i] + [x])     # copy an old subset + x
    return result


# ----------------------------------------------------------
# METHOD 2 — RECURSION
# ----------------------------------------------------------
def subsets_recursion(nums, i=0, path=()):
    if i == len(nums):                 # base case: every number decided
        return [list(path)]
    skip = subsets_recursion(nums, i + 1, path)
    take = subsets_recursion(nums, i + 1, path + (nums[i],))
    return skip + take


# ----------------------------------------------------------
# METHOD 3 — RECURSION + OUR OWN STACK
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def subsets_stack(nums):
    stack = Stack()                    # our own stack -> see stack_base.py
    stack.push((0, []))
    result = []
    while not stack.is_empty():
        i, path = stack.pop()
        if i == len(nums):
            result.append(path)                    # every number decided
        else:
            stack.push((i + 1, path + [nums[i]]))  # TAKE nums[i]
            stack.push((i + 1, path))              # SKIP nums[i]
    return result


# ----------------------------------------------------------
# METHOD 4 — OUR OWN STACK + BACKTRACKING
# (uses our own Stack -> see stack_base.py: push / pop / is_empty)
# ----------------------------------------------------------
def subsets_backtrack(nums):
    stack = Stack()                    # our own stack -> see stack_base.py
    path = []                          # the subset we are building (shared)
    result = [[]]                      # the empty subset
    for j in range(len(nums) - 1, -1, -1):
        stack.push((j, "go"))          # first choices
    while not stack.is_empty():
        j, phase = stack.pop()
        if phase == "go":
            path.append(nums[j])                   # CHOOSE
            result.append(path[:])                 # every path is a subset
            stack.push((j, "back"))                # UNDO later
            for k in range(len(nums) - 1, j, -1):
                stack.push((k, "go"))              # choices after j
        else:                                      # "back": UNDO
            path.pop()
    return result


# ----------------------------------------------------------
# Test cases   (python3 10_subsets.py)
# ----------------------------------------------------------
if __name__ == "__main__":
    norm = sorted          # the ORDER of the subsets may differ between methods
    methods = [subsets_loop, subsets_recursion, subsets_stack, subsets_backtrack]
    tests = [
        (([],), [[]]),
        (([1],), [[], [1]]),
        (([1, 2, 3],), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
    ]
    for args, expected in tests:
        results = [m(*args) for m in methods]
        print(args, "->", results[0])
        assert all(norm(r) == norm(expected) for r in results), results
    print("all four methods agree on every test ✅")
