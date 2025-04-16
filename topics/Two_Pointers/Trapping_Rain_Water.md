# Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/description/

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

**Example 1:**

![img](./assets/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

 

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`



Reflections:

1. move the smaller side



## Solution

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        max_of_left = height[left]
        max_of_right = height[right]
    
        while left < right:
            if height[left] <= height[right]:
                left += 1
                # update max_of_left
                if height[left] > max_of_left:
                    max_of_left = height[left]
                else:
                    #  add to res
                    res += max_of_left - height[left]
            else:
                right -= 1
                # update max_of_right
                if height[right] > max_of_right:
                    max_of_right = height[right]
                else:
                    # add to res
                    res += max_of_right - height[right]
        
        return res
```

TC: O(n) one pass

SC: O(1)