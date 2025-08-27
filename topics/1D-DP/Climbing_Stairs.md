# Climbing Stairs

https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

 

**Constraints:**

- `1 <= n <= 45`



## Solution

### not working dfs

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        def dfs(curr):
            if curr > n: return 0
            if curr == n: return 1
            return dfs(curr+1) + dfs(curr+2)
        
        return dfs(0)
```



### top-down

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        cache[n] = 1
        def dfs(curr) -> int:
            if curr > n: return 0
            if cache[curr] != -1: return cache[curr]

            cache[curr] = dfs(curr+1) + dfs(curr+2)
            return cache[curr]
        
        return dfs(0)
```

TC: O(n)

SC: O(n)