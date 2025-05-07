### Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

 

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

 

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `1 <= k <= nums.length`



**Reflections**:

- use monotonic queue with deque



## Solution

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # store index
        res = []

        for i in range(len(nums)):
            # pop if curr is greater than value at dq[-1]
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            # add to dq
            dq.append(i)

            # pop left when it reaches window size k
            if i >= k and dq[0] == i - k:
                dq.popleft()

            if i >= k-1:
                res.append(nums[dq[0]])
        return res
```

TC: O(n)

SC: O(n)