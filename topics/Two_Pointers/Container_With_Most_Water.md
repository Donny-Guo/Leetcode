# Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

**Example 1:**

![img](./assets/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

 

**Constraints:**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`



**Reflections**:

1. use two pointers, decide which side should you move -> smaller side



## Solution 1: Brute Force

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getWater(left, right):
            return min(height[left], height[right]) * (right - left)
        
        n = len(height)
        res = 0
        for i in range(n - 1):
            for j in range(i+1, n):
                res = max(res, getWater(i, j))
        
        return res
```

TC: O(n^2)

SC: O(1)

## Solution 2: Greedy Algorithm

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getWater(left, right):
            return min(height[left], height[right]) * (right - left)
        
        res = 0
        n = len(height)
        left, right = 0, n - 1
        while left < right:
            res = max(res, getWater(left, right))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return res
```

TC: O(n)

SC: O(1)