# Largest Rectangle in Histogram

https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

 

**Example 1:**

![img](./assets/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**

![img](./assets/histogram-1.jpg)

```
Input: heights = [2,4]
Output: 4
```

 

**Constraints:**

- `1 <= heights.length <= 105`
- `0 <= heights[i] <= 104`



**Reflections**:

1. keep the stack monotonically increasing -> bar can extend to the right -> easy to compute area
2. update index after pop



## Solution:

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stack = []
        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][1] > height:
                index, tmp_height = stack.pop(-1)
                res = max(res, tmp_height * (i - index))
            stack.append((index, height))
        
        
        for index, height in stack:
            res = max(res, height * (n - index))
        return res
```

TC: O(n)

SC: O(n)