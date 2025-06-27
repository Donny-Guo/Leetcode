# Combination Sum II

https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

 

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

 

**Constraints:**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`



**Reflections**:

- similar to "Combination Sum"
- differences:
  - Candidate numbers not unique
  - each element can only be used once
- how to remove duplicates:
  - Method 1: use hash map to count -> pick another number
  - method 2: sort the array + use while loop to curr number



## Solution 1: hashmap

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = [0] * 51
        for candidate in candidates:
            counter[candidate] += 1
        res = []
        curr = []

        def backtrack(i):
            # base case:
            if sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target or i >= 51:
                return
            elif counter[i] == 0:
                backtrack(i+1)
                return
            else:
                # include i
                counter[i] -= 1
                curr.append(i)
                backtrack(i)
                curr.pop()
                counter[i] += 1
                
                # skip i
                backtrack(i+1)
        backtrack(1)

        return res
```

TC: $O(n * 2^n)$

SC: O(n)



## Solution 2: backtrack with while loop

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target or i >= len(candidates):
                return
            else:
              	# include candidates[i]
                curr.append(candidates[i])
                backtrack(i+1)
                curr.pop()
                
                # skip candadates[i]
                curr_item = candidates[i]
                while i < len(candidates) and candidates[i] == curr_item:
                    i += 1
                backtrack(i)
            
        backtrack(0)
        return res
```

TC: $O(n * 2^n)$

SC: O(n)