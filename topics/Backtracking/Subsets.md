# Subsets

https://leetcode.com/problems/subsets/description/

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

 

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

 

**Constraints:**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

---

## Solution 1: backtracking

```python
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    curr = []
    
    def backtrack(i):
      if i >= len(nums):
        res.append(curr.copy())
        return
      
      # include nums[i]
      curr.append(nums[i])
      backtrack(i+1)
      curr.pop() # undo
      
      # skip nums[i]
      backtrack(i+1)
    
    backtrack(0)
    return res
```

TC: O(n * 2^n): total number of subsets=2^n, the length of each subset: n

SC: O(n)

## Solution 2: Iteration

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]
        
        return res
```

TC: $O(n * 2^n)$

SC: O(n)