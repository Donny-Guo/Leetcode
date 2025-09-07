# Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

 

**Example 1:**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

 

**Constraints:**

- `1 <= nums.length <= 2 * 104`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.



**Reflections**:

1. use curMin, curMax to store min/max started from the beginning

## Solution

```python
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = nums[0]
    curMax, curMin = nums[0], nums[0]
    for i in range(1, len(nums)):
      tempMax = curMax * nums[i]
      tempMin = curMin * nums[i]
      curMax = max(tempMax, tempMin, nums[i])
      curMin = max(tempMin, tempMax, nums[i])
      res = max(res, curMax)
     return res
```

TC: O(n)

SC: O(1)