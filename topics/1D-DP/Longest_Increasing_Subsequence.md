# Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an integer array `nums`, return *the length of the longest **strictly increasing*** ***subsequence***.

 

**Example 1:**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2:**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3:**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

 

**Constraints:**

- `1 <= nums.length <= 2500`
- `-104 <= nums[i] <= 104`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

---

## Solution: top down recursion

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        def dfs(i) -> int:
            if memo[i] > 0: return memo[i]

            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        for i in range(len(nums)):
            dfs(i)
        return max(memo)
```

TC: O(N^2)

SC: O(N)



## Solution: bottom up

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) + 1)
        memo[-1] = 0
        for i in range(len(nums)-1, -1, -1):
            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + memo[j])
            memo[i] = res
        return max(memo)
```

TC: O(n^2)

SC: O(n)