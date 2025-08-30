# House Robber II

https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

 

**Example 1:**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

**Example 2:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
```

 

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`



**Reflections**:

- similar to House Robber
- To deal with the circle in this problem:
  - Pass a flag to each recursion to note whether it takes the first house or not OR
  - do house robber on nums[:-1] and then nums[1:] and find the max

## Solution: recursion (failed)

```python
class Solution:
  def rob(self, nums: List[int]) -> int:
    def dfs(i: int, flag: bool) -> int:
      # base case
      if i >= len(nums): return 0
    	if i == len(nums) - 1 and flag == True: return 0
    
      # general case:
      if i == 0:
        return max(nums[i] + dfs(i+2, True), dfs(i+1, False))
      return max(nums[i] + dfs(i+2, flag), dfs(i+1, flag))
   	return dfs(0, False)
```

TC: $O(2^n)$

SC: O(n)

## Solution: Top-down DP

```python
class Solution:
  def rob(self, nums: List[int]) -> int:
    memo = {} # key=(i, flag), value=int
    def dfs(i: int, flag: bool) -> int:
      # base case
      if i >= len(nums): return 0
      if i == len(nums) - 1 and flag == True: return 0
    	if (i, flag) in memo: return memo[(i, flag)]
    	
      if i == 0:
        return max(nums[i] + dfs(i+2, True), dfs(i+1, False))
     
    	memo[(i, flag)] = max(nums[i] + dfs(i+2, flag), dfs(i+1, flag))
      return memo[(i, flag)]
    return dfs(0, False)
```

TC: O(N)

SC: O(N)

## Solution: Bottom-up DP

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        return max(helper(nums[:-1]), helper(nums[1:]))
```

TC: O(n)

SC: O(1)